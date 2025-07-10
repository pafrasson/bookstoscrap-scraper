from urllib.parse import urljoin
from src.logger.logger import setup_logger

logger = setup_logger(__name__)


def collect_book_links(page):
    """
    Collects book links from page
    :param page:
    :return: list of book links
    """
    logger.info("Iniciando coleta de links dos livros")
    links = []
    page_number = 1

    while True:
        logger.debug(f"Processando página {page_number}: {page.url}")

        logger.debug("Aguardando carregamento dos produtos na página")
        page.wait_for_selector("article.product_pod")

        logger.debug("Buscando todos os produtos na página")
        products = page.query_selector_all("article.product_pod")
        logger.debug(f"Encontrados {len(products)} produtos na página {page_number}")

        for i, product in enumerate(products, 1):
            logger.debug(f"Extraindo link do produto {i}/{len(products)}")
            link_element = product.query_selector("h3 > a")
            relative_url = link_element.get_attribute("href")
            full_url = urljoin(page.url, relative_url)
            links.append(full_url)
            logger.debug(f"Link coletado: {full_url}")

        logger.info(f"Página {page_number} processada. Total de links coletados até agora: {len(links)}")

        logger.debug("Verificando se existe próxima página")
        next_button = page.query_selector("li.next > a")
        if next_button:
            next_url = urljoin(page.url, next_button.get_attribute("href"))
            logger.debug(f"Próxima página encontrada: {next_url}")
            logger.debug("Navegando para a próxima página")
            page.goto(next_url)
            page_number += 1
        else:
            logger.debug("Não há mais páginas para processar")
            break

    logger.info(f"Coleta concluída. Total de {len(links)} links coletados em {page_number} páginas")
    return links
