def extract_book_data(page, url):
    """
    Extracts book data from book page
    :param page:
    :param url:
    :return:
    """
    try:
        page.goto(url)
        page.wait_for_selector(".product_main > h1", timeout=5000)
        title = page.query_selector(".product_main > h1").inner_text()

        rows = page.query_selector_all("table.table.table-striped > tbody > tr")
        product_info = {
            row.query_selector("th").inner_text().strip(): row.query_selector("td").inner_text().strip()
            for row in rows
        }

        return {
            "title": title,
            "product_type": product_info.get("Product Type", ""),
            "price_excl_tax": product_info.get("Price (excl. tax)", ""),
            "price_incl_tax": product_info.get("Price (incl. tax)", ""),
            "tax": product_info.get("Tax", ""),
            "availability": product_info.get("Availability", ""),
            "url": url
        }

    except Exception as e:
        print(f"[ERRO] Falha ao processar {url}: {e}")
        return None
