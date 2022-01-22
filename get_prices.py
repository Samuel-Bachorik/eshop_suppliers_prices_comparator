import requests
from bs4 import BeautifulSoup

def get_price_alza(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    # price = soup.find(id = "prices").get_text()
    price = soup.find("span", {"class": "price_withVat"}).get_text()

    return price

def get_price_heureka(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
        r = requests.get(url, headers=headers)
        price = r.text.split("\"minPrice\":")[1].split(",")[0]

    except:
        return False

    return price

def get_price_gigastore(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        # price = soup.find(id = "prices").get_text()
        price = soup.find("span", {"id": "product-detail-price-value"}).get_text()

    except:
        return False

    return price


def remove_trash(price):

    number = float(price.replace('€', '').replace(' ', '').replace(' ', '').replace(',', '.'))



    return number
