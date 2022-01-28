import requests
from bs4 import BeautifulSoup

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

def get_price_alza(url):

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    # price = soup.find(id = "prices").get_text()
    price = soup.find("span", {"class": "price_withVat"}).get_text()

    return price

def get_price_heureka(url):
    
    try:
        r = requests.get(url, headers=headers)
        price = r.text.split("\"minPrice\":")[1].split(",")[0]

    except:
        return False

    return price


""" DODAVATELIA """

def get_price_gigastore(url):
    
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find("span", {"id": "product-detail-price-value"}).get_text()
        
        if "," in price and "." in price:
            price = price.replace(',', '')

    except:
        return False

    return price

def get_price_tvojpc(url):

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find("span", {"class": "woocommerce-Price-amount amount"}).get_text()

    except:
        return False

    try:
        soup.find("p", {"class": "stock out-of-stock"}).get_text()

        return "NEDOSTUPNE"

    except:
        return price


def get_price_axdata(url):

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find("span", {"itemprop": "price"}).get_text()

    except:
        return False

    try:
        soup.find("span", {"class": "product-available"}).get_text()

    except:
        return "NEDOSTUPNE"

    return price


def get_price_datacomp(url):

    try:
        r = requests.get(url, headers=headers)
        r_text = r.text
        soup = BeautifulSoup(r_text, "html.parser")
        price = soup.find("div", {"class": "prc wvat abs"}).get_text()

    except:
        return False

    try:
        soup.find("span", {"class": "avail_ico avail_ok"}).get_text()

    except:
        return "NEDOSTUPNE"

    return price.replace('Â', '').replace('', '').replace('â', '').replace('¬', '').replace(' ', '')


def remove_trash(price):

    number = float(price.replace('€', '').replace(' ', '').replace(' ', '').replace(',', '.'))

    return number
