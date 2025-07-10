import csv
from src.logger.logger import setup_logger

logger = setup_logger(__name__)


def save_to_csv(data, filename="public/books.csv"):
    """
    Writes book to a csv file
    :param data:
    :param filename:
    :return:
    """
    logger.info(f"Iniciando salvamento de dados em CSV: {filename}")
    logger.debug(f"Número total de registros para salvar: {len(data)}")

    try:
        logger.debug(f"Abrindo arquivo para escrita: {filename}")
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            logger.debug("Configurando DictWriter com fieldnames")
            writer = csv.DictWriter(file, fieldnames=[
                "title", "product_type", "price_excl_tax",
                "price_incl_tax", "tax", "availability", "rating", "url"
            ])

            logger.debug("Escrevendo cabeçalho do CSV")
            writer.writeheader()

            logger.debug("Escrevendo dados das linhas")
            writer.writerows(data)

        logger.info(f"Arquivo CSV salvo com sucesso: {filename}")
        logger.info(f"Total de {len(data)} registros salvos")

    except Exception as e:
        logger.error(f"Erro ao salvar arquivo CSV {filename}: {e}")
        logger.debug(f"Detalhes do erro: {type(e).__name__}: {str(e)}")
        raise
