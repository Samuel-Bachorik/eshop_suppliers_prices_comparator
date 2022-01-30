from google_sheets import get_sheet
from get_prices import get_price_alza, get_price_heureka, get_price_gigastore, get_price_axdata,get_price_tvojpc\
    ,get_price_dmcomp,get_price_datacomp,get_price_prva,get_price_zdomu,remove_trash

from concurrent.futures import ProcessPoolExecutor
import concurrent.futures

import time

ID = '114oIOb8Ml45ET3aziBiaBlOl0TpbtLMT8-fkj6xGTTM'
JSON_KLUC = "eshop-sheet-c38c9c8a59ed.json"
sheets = get_sheet(ID, JSON_KLUC)

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

    #print(stop_start_ids,"IDS")
    print("Started...")
    with ProcessPoolExecutor(max_workers=num) as executor:
        results = [None] * num
        for x in range(num):
            results[x] = executor.submit(process, sheets, stop_start_ids[x])

        errors = []
        for f in concurrent.futures.as_completed(results):
            x = f.result()
            errors.append(x)

        for i in errors:
            for x in i:
                print(x)

        print("This task took %s seconds" % (time.time() - start_time))


def process(sheet, start_stop):
    errors = []
    supplier_database = ["gigastore", "datacomp", "axdata", "tvojpc", "zdomu", "prva", "dmcomp"]
    supplier_database_f = [get_price_gigastore, get_price_datacomp, get_price_axdata, get_price_tvojpc,
                         get_price_zdomu, get_price_prva, get_price_dmcomp]

    for i in range(start_stop[0],start_stop[1]):

        margin_in_percent = 2

        supplier_price_err = False
        product_margin_err = False
        lowest_price_err = False

        for j in range(len(supplier_database)):
            if supplier_database[j] in sheet[i][1]:
                price_supplier = supplier_database_f[j](sheet[i][1])

        price_heureka = get_price_heureka(sheet[i][2])
        price_alza = get_price_alza(sheet[i][0])

        if price_supplier == "UNAVAILABLE":
            errors.append("\033[1m" + '\033[91m' + "Product " + str(i + 2) + " is unavailable" + "\033[0m")

            continue

        if price_heureka  == False or price_supplier == False:


            errors.append("\033[1m" + '\033[91m' + "Product " + str(i + 2) + " dissapeared from supplier database" + "\033[0m")

            continue

        price_supplier = remove_trash(price_supplier)
        price_heureka = remove_trash(price_heureka)
        price_alza = remove_trash(price_alza)


        if price_alza < price_supplier:
            supplier_price_err = True

        if price_heureka < price_alza:
            lowest_price_err = True

        if (abs(price_alza - price_supplier) / price_supplier) * 100.0 < margin_in_percent:
            product_margin_err = True

        error = "\033[1m" + '\033[91m' + "At product "  + str(i+2) +" - "  +"\033[0m"

        if supplier_price_err: error+= " Price of supplier is higher ||| "

        if lowest_price_err: error+= " Lower price exist ||| "

        if product_margin_err: error += " Margin is low"

        """if supplier_price_err or lowest_price_err or product_margin_err:
            errors.append("At product "+ str(i+2) + " Price of supplier is higher - " + str(supplier_price_err) +
                          "   |||   Lower price exist - " + str(lowest_price_err)+"   |||   Low margin - " + str(product_margin_err))"""

        if supplier_price_err or lowest_price_err or product_margin_err:
            errors.append(error)

    return errors


if __name__ == '__main__':
    _run_workers(processes_count= 30)


