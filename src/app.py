"""import re, csv
from urllib.parse import urljoin
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    base_url = "http://books.toscrape.com/"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(base_url)

    links = []

    while True:
        page.wait_for_selector("article.product_pod")
        products = page.query_selector_all("article.product_pod")

        for product in products:
            link_element = product.query_selector("h3 > a")
            relative_url = link_element.get_attribute("href")
            full_url = urljoin(page.url, relative_url)  # resolve path relativo
            links.append(full_url)

        # Verifica se há próximo botão
        next_button = page.query_selector("li.next > a")
        if next_button:
            next_href = next_button.get_attribute("href")
            next_url = urljoin(page.url, next_href)
            page.goto(next_url)
        else:
            break  # Fim da paginação

    results = []

    for link in links:
        page.goto(link)
        # Título
        page.wait_for_selector(".product_main > h1")
        title = page.query_selector(".product_main > h1").inner_text()
        # Mapeia todas as linhas da tabela
        rows = page.query_selector_all("table.table.table-striped > tbody > tr")
        product_info = {}
        for row in rows:
            key = row.query_selector("th").inner_text().strip()
            value = row.query_selector("td").inner_text().strip()
            product_info[key] = value

        results.append({
            "title": title,
            "product_type": product_info.get("Product Type", ""),
            "price_excl_tax": product_info.get("Price (excl. tax)", ""),
            "price_incl_tax": product_info.get("Price (incl. tax)", ""),
            "tax": product_info.get("Tax", ""),
            "availability": product_info.get("Availability", ""),
            "url": link
        })

    with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "title", "product_type", "price_excl_tax",
            "price_incl_tax", "tax", "availability", "url"
        ])
        writer.writeheader()
        writer.writerows(results)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
"""