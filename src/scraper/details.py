from src.logger.logger import setup_logger

logger = setup_logger(__name__)

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def extract_book_data(page, url):
    """
    Extracts book data from book page
    :param page: Playwright page instance
    :param url: URL of the book
    :return: dict with book information or None
    """
    try:
        page.goto(url)
        page.wait_for_selector(".product_main > h1", timeout=1000)
        title = page.query_selector(".product_main > h1").inner_text()

        # Extração da tabela de informações
        rows = page.query_selector_all("table.table.table-striped > tbody > tr")
        product_info = {
            row.query_selector("th").inner_text().strip(): row.query_selector("td").inner_text().strip()
            for row in rows
        }

        # Extração da nota
        rating_element = page.query_selector("p.star-rating")
        rating_class = rating_element.get_attribute("class") if rating_element else ""
        rating_text = rating_class.split()[-1] if rating_class else ""
        rating = RATING_MAP.get(rating_text, None)

        return {
            "title": title,
            "product_type": product_info.get("Product Type", ""),
            "price_excl_tax": product_info.get("Price (excl. tax)", ""),
            "price_incl_tax": product_info.get("Price (incl. tax)", ""),
            "tax": product_info.get("Tax", ""),
            "availability": product_info.get("Availability", ""),
            "rating": rating,
            "url": url
        }

    except Exception as e:
        logger.error(f"[ERRO] Falha ao processar {url}: {e}")
        return None
