from get_prices import Price_Scraper

price_scraper = Price_Scraper()

class Process:
    def __init__(self):
        self.remove_trash           = price_scraper.remove_trash
        self.get_price_heureka      = price_scraper.get_price_heureka
        self.get_price_alza         = price_scraper.get_price_alza
        self.get_price_gigastore    = price_scraper.get_price_gigastore
        self.get_price_datacomp     = price_scraper.get_price_datacomp
        self.get_price_axdata       = price_scraper.get_price_axdata
        self.get_price_tvojpc       = price_scraper.get_price_tvojpc
        self.get_price_zdomu        = price_scraper.get_price_zdomu
        self.get_price_prva         = price_scraper.get_price_prva
        self.get_price_dmcomp       = price_scraper.get_price_dmcomp
        self.get_price_extremecomp  = price_scraper.get_price_extremecomp
        self.get_price_hejsk        = price_scraper.get_price_hejsk
        self.get_price_andreashop   = price_scraper.get_price_andreashop
        self.get_price_mobilonline  = price_scraper.get_price_mobilonline
        self.get_price_mobilecare   = price_scraper.get_price_mobilecare


    def process(self,sheet, start_stop):
        errors = []
        supplier_database = ["gigastore", "datacomp", "axdata", "tvojpc", "zdomu", "prva", "dmcomp", "extremepcshop", "hej", "andreashop", "mobilonline",
                             "mobilecare"]
        supplier_database_f = [self.get_price_gigastore, self.get_price_datacomp, self.get_price_axdata, self.get_price_tvojpc,
                               self.get_price_zdomu, self.get_price_prva, self.get_price_dmcomp,self.get_price_extremecomp,self.get_price_hejsk,
                               self.get_price_andreashop,self.get_price_mobilonline,self.get_price_mobilecare]

        for i in range(start_stop[0], start_stop[1]):

            margin_in_percent = 10

            supplier_price_err = False
            product_margin_err = False
            lowest_price_err = False

            for j in range(len(supplier_database)):
                if supplier_database[j] in sheet[i][1]:
                    price_supplier = supplier_database_f[j](sheet[i][1])

            price_heureka = self.get_price_heureka(sheet[i][2])
            price_alza = self.get_price_alza(sheet[i][0])

            if price_supplier == "UNAVAILABLE":
                errors.append("\033[1m" + '\033[91m' + "Product " + str(i + 2) + " is unavailable" + "\033[0m")

                continue

            if price_heureka == False or price_supplier == False:
                errors.append("\033[1m" + '\033[91m' + "Product " + str(
                    i + 2) + " dissapeared from supplier database" + "\033[0m")

                continue

            price_supplier = self.remove_trash(price_supplier)
            price_heureka = self.remove_trash(price_heureka)
            price_alza = self.remove_trash(price_alza)

            if price_alza < price_supplier:
                supplier_price_err = True

            if price_heureka < price_alza:
                lowest_price_err = True

            if (abs(price_alza - price_supplier) / price_supplier) * 100.0 < margin_in_percent:
                product_margin_err = True

            error = "\033[1m" + '\033[91m' + "At product " + str(i + 2) + " - " + "\033[0m"

            if supplier_price_err: error += " Price of supplier is higher ||| "
            if lowest_price_err: error += " Lower price exist ||| "
            if product_margin_err: error += " Margin is low"

            if supplier_price_err or lowest_price_err or product_margin_err:
                errors.append(error)

        return errors
