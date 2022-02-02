from google_sheets import get_sheet
from get_prices import Price_Scraper

price_scraper = Price_Scraper()

ID = '114oIOb8Ml45ET3aziBiaBlOl0TpbtLMT8-fkj6xGTTM'
JSON_KLUC = "eshop-sheet-c38c9c8a59ed.json"
sheets = get_sheet(ID, JSON_KLUC)

for i in range(120):
    print(i+2)
    price_scraper.get_price_alza(sheets[i][0])
