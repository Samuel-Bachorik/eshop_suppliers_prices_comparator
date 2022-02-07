import requests
from bs4 import BeautifulSoup


class Price_Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

    def get_price_alza(self, url):

        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.find("span", {"class": "price_withVat"}).get_text()

        return price

    def get_price_heureka(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            price = r.text.split("\"minPrice\":")[1].split(",")[0]

        except:
            return False

        return price

    """ DODAVATELIA """

    def get_price_gigastore(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"id": "product-detail-price-value"}).get_text()

            if "," in price and "." in price:
                price = price.replace(',', '')

        except:
            return False

        return price

    def get_price_prva(self, url):
        try:
            r = requests.get(url, headers= self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"class": "price price-default"}).get_text()

        except:
            return False

        try:
            s = soup.find("a", {"class": "link-spedition-days"}).get_text()

            "(Nie je skladom)"
            "Na objednávku"

            if "Do 24 hodín" in s or "Do 48 hodín" in s or "Do 72 hodín" in s:
                return price

            else:
                return "UNAVAILABLE"

        except:
            return False

    def get_price_tvojpc(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"class": "woocommerce-Price-amount amount"}).get_text()

        except:
            return False

        try:
            soup.find("p", {"class": "stock out-of-stock"}).get_text()

            return "UNAVAILABLE"

        except:
            return price

    def get_price_axdata(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find("span", {"itemprop": "price"}).get_text()

        except:
            return False

        try:
            soup.find("span", {"class": "product-available"}).get_text()

        except:
            return "UNAVAILABLE"

        return price

    def get_price_datacomp(self, url):

        try:
            r = requests.get(url, headers=self.headers)
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

    def get_price_dmcomp(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("strong", {"class": "price sub-left-position"}).get_text()

        except:
            return False

        try:
            s = soup.find("span", {"class": "strong"}).get_text().replace('Â', '').replace('', '').replace('â', '').replace('¬', '').replace(' ', '').replace('€', '').replace(' ', '').replace(' ','').replace(',', '.')

            if "Vypredané" in s:
                return "UNAVAILABLE"

        except:
            return "UNAVAILABLE"

        return price

    def get_price_zdomu(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("span", {"itemprop": "price"}).get_text()

        except:
            return False

        try:

            x = \
                r_text.split("<span class=\"control-label\">Kód: </span>")[0].split(
                    "<div class=\"product-information\">")[
                    1].split("TEXT")

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
            price = soup.find("span", {"class": "cenabezdph"}).get_text().replace('Â', '').replace('', '').replace('â','').replace('¬', '').replace(' ', '').replace('€', '').replace(' ', '').replace(' ', '').replace(',', '.').replace("bezDPH", "")
            price = float(price) * 1.2
            price = str(price)

        except:
            return False

        try:
            soup.find("p", {"class": "skladom"}).get_text()

        except:
            return "UNAVAILABLE"

        return price

    def get_price_hejsk(self, url):

        try:
            r = requests.get(url, headers=self.headers)
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

    def get_price_andreashop(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("div", {"class": "value"}).get_text()

        except:
            return False

        try:
            soup.find("div", {"class": "dostupnost stav-1 tooltip tooltip"}).get_text()


        except:
            return "UNAVAILABLE"

        return price

    def get_price_mobilonline(self, url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("div", {"class": "ProductNormal_page_price__3djvm"})
            children = price.findChildren()
            price = children[1].text


        except:
            return False

        try:
            soup.find("div", {"class": "Availability_available__1BM2E"}).get_text()
            return price

        except:
            return "UNAVAILABLE"


    def get_price_mobilecare(self, url):
        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("span", {"class": "woocommerce-Price-amount amount"}).get_text()

            if "," in price and "." in price:
                price = price.replace(',', '')

        except:
            return False

        try:
            soup.find("button", {"name": "add-to-cart"}).get_text()

        except:
            return "UNAVAILABLE"

        return price


    def get_price_danimani(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            r_text = r.text

            soup = BeautifulSoup(r_text, "html.parser")
            price = float((soup.find("li", {"class": "taxprice"}, "li").get_text().replace('€', '').replace(' ','').replace(' ', '').replace(',', '.')).replace("BezDPH:", "")) * 1.2
            price = str(price)

        except:
            return False

        try:
            soup.find("li", {"class": "stav-skladu vypredane"}).get_text()
            return "UNAVAILABLE"

        except:

            return price

    def get_price_mobilpc(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            id = url.split("p-")[1].split(".xhtml")[0]
            price = soup.find("span", {"id": "PriceWithVAT" + id}).get_text()

        except:
            return False

        try:
            soup.find("div", {"data-txt": "Vo vlastnom sklade"}).get_text()

        except:

            return "UNAVAILABLE"

        return price

    def get_price_lacnenakupy(self, url):

        try:
            r = requests.get(url, headers=self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")

            price = soup.find(class_="price price-primary text-danger").get_text()

        except:
            return False

        try:
            a = soup.find("div", {"id": "productStatus"}).get_text()

            if "Skladom" in a:
                return price

            if "Na objednávku" or "Momentálne nedostupné" or "Dočasne vypredané" or "Nedostupné" or "dodávateľa" in a:
                return "UNAVAILABLE"

        except:
            return "UNAVAILABLE"

        return price

    def get_price_datart(self, url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")

            price = soup.find("div", {"class": "price-wrap"}).get_text()

        except:
            return False

        try:
            a = soup.find("span", {"class": "product-availability-state"}).get_text()
            if "Posledný kus k odoslaniu" in a or "Ihneď k odoslaniu?" in a:
                return price

            if "U dodávateľa" in a or "Očakávame do" in a or "Nie je skladom" in a or "K vyzdvihnutiu na predajni" in a:
                return "UNAVAILABLE"

        except:
            return "UNAVAILABLE"

        return price

    def get_price_pricemarket(self, url):

        try:
            r = requests.get(url, headers= self.headers)
            r_text = r.text
            soup = BeautifulSoup(r_text, "html.parser")
            price = soup.find("span", {"itemprop": "price"}).get_text()

        except:
            return False

        try:
            s = soup.find("span", {"id": "product-availability"}).get_text().replace(' ', '').replace(' ', '').replace(
                ',', '.').replace("", "").replace("", "")

            "Dodanie1-5pracovnýchdní"
            "Ľutujeme.aletentoproduktjemomentálnevypredaný.Kontaktujtenásprosímohľadomdostupnostitohtoproduktu."
            "Naobjednávku."

            if "Dodanie" in s:
                return price

            if "Ľutujeme" in s or "vypredaný" in s or "Naobjednávku" in s or "Nedostupné":
                return "UNAVAILABLE"

        except:
            return "UNAVAILABLE"

        return price

    def remove_trash(self, price):
        number = float(price.replace('€', '').replace(' ', '').replace(' ', '').replace(',', '.'))

        return number

