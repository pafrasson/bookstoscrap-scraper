from scraper.browser import start_browser
from scraper.listing import collect_book_links
from scraper.details import extract_book_data
from scraper.exporter import save_to_csv


def run_scraper():
    """
    Runs the scraper and csv function, stops browser after job
    :return:
    """
    playwright, browser, context, page = start_browser(headless=False)

    try:
        page.goto("http://books.toscrape.com/")
        links = collect_book_links(page)
        print(f"[INFO] Total de livros encontrados: {len(links)}")

        results = [data for data in map(lambda url: extract_book_data(page, url), links) if data]
        save_to_csv(results)
        print(f"[INFO] Dados salvos com sucesso.")
    finally:
        context.close()
        browser.close()
        playwright.stop()
