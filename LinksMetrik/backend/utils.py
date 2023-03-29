from urllib.parse import urlparse


def domain_finder(urls: list) -> list:
    """func for find domain in url"""
    ht = 'http://'
    hts = 'https://'
    domain_list = []
    for url in urls:
        if ht in url or hts in url:
            domain = urlparse(url).netloc
        else:
            domain = url
        domain_list.append(domain)
    return domain_list
