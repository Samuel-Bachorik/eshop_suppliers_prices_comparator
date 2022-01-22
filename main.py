from google_sheets import get_sheet
from get_prices import get_price_alza, get_price_heureka, get_price_gigastore, remove_trash

ID = '114oIOb8Ml45ET3aziBiaBlOl0TpbtLMT8-fkj6xGTTM'
JSON_KLUC = "eshop-sheet-c38c9c8a59ed.json"
sheets = get_sheet(ID, JSON_KLUC)

for i in range(len(sheets)):
    price = False
    product_miss = False
    lowest_price = False

    price_dodavatel = get_price_gigastore(sheets[i][1])
    price_heureka = get_price_heureka(sheets[i][2])
    price_alza = get_price_alza(sheets[i][0])

    if price_heureka  == False or price_dodavatel == False:
        product_miss = True
        print("Produkt ", i+1, " zmizol")

        continue

    price_dodavatel = remove_trash(price_dodavatel)
    price_heureka = remove_trash(price_heureka)
    price_alza = remove_trash(price_alza)


    if price_alza > price_dodavatel:
        price = True

    if price_heureka < price_alza:
        lowest_price = True

    if price or lowest_price:
        print("Na produkte ",i+1, "Cena dodavatela vyššia - ",product_miss,"||| Existuje nizsia cena - ",lowest_price)
