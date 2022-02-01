import requests
from bs4 import BeautifulSoup

class Price_Scraper:
    def __init__(self):
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

    def get_price_alza(self,url):

        r = requests.get(url, headers= self.headers)
        soup = BeautifulSoup(r.text, "html.parser")
        # price = soup.find(id = "prices").get_text()
        price = soup.find("span", {"class": "price_withVat"}).get_text()

        return price

    def get_price_heureka(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            price = r.text.split("\"minPrice\":")[1].split(",")[0]

        except:
            return False

        return price


    """ DODAVATELIA """

    def get_price_gigastore(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"id": "product-detail-price-value"}).get_text()

            if "," in price and "." in price:
                price = price.replace(',', '')

        except:
            return False

        return price


    def get_price_prva(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"class": "price price-default"}).get_text()

        except:
            return False

        try:
            s = soup.find("a", {"id": "ctl105_i3Shop_Product_Info3Repeater_ctl01_i3Shop_Product_Info3products_spedition_days"}).get_text()

            if "(Nie je skladom)" in s:
                return "UNAVAILABLE"

            else:
                return price

        except:
            return False


    def get_price_tvojpc(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"class": "woocommerce-Price-amount amount"}).get_text()

        except:
            return False

        try:
            soup.find("p", {"class": "stock out-of-stock"}).get_text()

            return "UNAVAILABLE"

        except:
            return price


    def get_price_axdata(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"itemprop": "price"}).get_text()

        except:
            return False

        try:
            soup.find("span", {"class": "product-available"}).get_text()

        except:
            return "UNAVAILABLE"

        return price


    def get_price_datacomp(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("div", {"class": "prc wvat abs"}).get_text()

        except:
            return False

        try:
            soup.find("span", {"class": "avail_ico avail_ok"}).get_text()

        except:
            return "UNAVAILABLE"

        return price.replace('Â', '').replace('', '').replace('â', '').replace('¬', '').replace(' ', '')


    def get_price_dmcomp(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("strong", {"class": "price sub-left-position"}).get_text()

        except:
            return False

        try:
            s = soup.find("span", {"class": "strong"}).get_text().replace('Â', '').replace('', '')\
                .replace('â', '').replace('¬', '').replace(' ', '').replace('€', '').replace(' ', '').replace(' ', '').replace(',', '.')

            if "Vypredané" in s:
                return "UNAVAILABLE"

        except:
            return "UNAVAILABLE"

        return price


    def get_price_zdomu(self,url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text


            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("span", {"itemprop": "price"}).get_text()

        except:
            return False

        try:

            x = r_text.split("<span class=\"control-label\">Kód: </span>")[0].split("<div class=\"product-information\">")[1].split("TEXT")

            if "nie je skladom" in x:
                return "UNAVAILABLE"

        except:
            return "UNAVAILABLE"

        return price

    def get_price_extremecomp(self, url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("span", {"class": "cenasdph"}).get_text().replace('Â', '').replace('', '') \
                .replace('â', '').replace('¬', '').replace(' ', '').replace('€', '').replace(' ', '').replace(' ',
                                                                                                              '').replace(
                ',', '.')

        except:
            return False

        try:

            soup.find("p", {"class": "skladom"}).get_text()

        except:
            return "UNAVAILABLE"

        return price

    def get_price_hejsk(self, url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("span", {"id": "real_price"}).get_text()
        except:
            return False

        try:
            soup.find("span", {"class": "not-available"}).get_text()

            return "UNAVAILABLE"

        except:
            try:
                soup.find("span", {"class": "available supplier"}).get_text()
                return "UNAVAILABLE"

            except:
                try:
                    soup.find("span", {"class": "date-available"}).get_text()
                    return "UNAVAILABLE"

                except:
                    return price


    def remove_trash(self, price):

        number = float(price.replace('€', '').replace(' ', '').replace(' ', '').replace(',', '.'))

        return number
