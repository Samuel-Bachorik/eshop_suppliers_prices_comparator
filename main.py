from google_sheets import get_sheet
from get_prices import get_price_alza, get_price_heureka, get_price_gigastore, remove_trash
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
ID = '114oIOb8Ml45ET3aziBiaBlOl0TpbtLMT8-fkj6xGTTM'
JSON_KLUC = "eshop-sheet-c38c9c8a59ed.json"
sheets = get_sheet(ID, JSON_KLUC)
import os

import time
def _run_workers(processes_count):
    start_time = time.time()
    num = processes_count

    num_for_process = int(len(sheets)/num)

    stop_start_ids = [[0 for _ in range(2)] for _ in range(num)]

    for z in range(num):
        if z == 0:
            stop_start_ids[z][1] = num_for_process

        stop_start_ids[z][0] = stop_start_ids[z-1][1]
        stop_start_ids[z][1] = stop_start_ids[z][0] + num_for_process

    print(stop_start_ids,"IDS")

    
    with ProcessPoolExecutor(max_workers=num) as executor:
        results = [None] * num
        for x in range(num):
            results[x] = executor.submit(process, sheets, stop_start_ids[x])

        #counter = 0
        errors = []
        for f in concurrent.futures.as_completed(results):
            x = f.result()
            errors.append(x)

        for i in errors:
            for x in i:
                print(x)

        print("--- %s seconds ---" % (time.time() - start_time))

          #  counter += 1

    #return result_x, result_y


def process(sheet, start_stop):
    errors = []

    for i in range(start_stop[0],start_stop[1]):

        price = False
        product_miss = False
        lowest_price = False

        price_dodavatel = get_price_gigastore(sheet[i][1])
        price_heureka = get_price_heureka(sheet[i][2])
        price_alza = get_price_alza(sheet[i][0])

        if price_heureka  == False or price_dodavatel == False:
            product_miss = True
            errors.append("Produkt "+  str(i+2) + " zmizol")

            continue

        price_dodavatel = remove_trash(price_dodavatel)
        price_heureka = remove_trash(price_heureka)
        price_alza = remove_trash(price_alza)


        """if i == 10:
            print(price_dodavatel)
            print(price_heureka)
            print(price_alza)"""

        if price_alza < price_dodavatel:
            price = True

        if price_heureka < price_alza:
            lowest_price = True

        if price or lowest_price:
            errors.append("Na produkte "+ str(i+2) + " Cena dodavatela vyššia - " + str(price) +"   |||   Existuje nizsia cena - " + str(lowest_price))

    return errors


if __name__ == '__main__':
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    _run_workers(processes_count= 20)
