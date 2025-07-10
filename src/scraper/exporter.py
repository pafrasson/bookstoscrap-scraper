import csv


def save_to_csv(data, filename="books.csv"):
    """
    Writes book to a csv file
    :param data:
    :param filename:
    :return:
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "title", "product_type", "price_excl_tax",
            "price_incl_tax", "tax", "availability", "rating","url"
        ])
        writer.writeheader()
        writer.writerows(data)
