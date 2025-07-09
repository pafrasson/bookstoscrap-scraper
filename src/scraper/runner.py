from src.scraper.browser import start_browser
from src.scraper.listing import collect_book_links
from src.scraper.details import extract_book_data
from src.scraper.exporter import save_to_csv
from src.logger import setup_logger

logger = setup_logger(__name__)


def run_scraper():
    """
    Runs the scraper and csv function, stops browser after job
    :return:
    """
    playwright, browser, context, page = start_browser(headless=False)

    try:
        page.goto("http://books.toscrape.com/")
        links = collect_book_links(page)
        logger.info(f"Total de livros encontrados: {len(links)}")

        results = [data for data in map(lambda url: extract_book_data(page, url), links) if data]
        save_to_csv(results)
        logger.info("Dados salvos com sucesso.")
    finally:
        context.close()
        browser.close()
        playwright.stop()
