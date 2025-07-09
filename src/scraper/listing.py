from urllib.parse import urljoin


def collect_book_links(page):
    """
    Collects book links from page
    :param page:
    :return: list of book links
    """
    links = []
    while True:
        page.wait_for_selector("article.product_pod")
        products = page.query_selector_all("article.product_pod")

        for product in products:
            link_element = product.query_selector("h3 > a")
            relative_url = link_element.get_attribute("href")
            full_url = urljoin(page.url, relative_url)
            links.append(full_url)

        next_button = page.query_selector("li.next > a")
        if next_button:
            next_url = urljoin(page.url, next_button.get_attribute("href"))
            page.goto(next_url)
        else:
            break
    return links
