from google_sheets import get_sheet
import time
import math
from run_workers import _run_workers

def print_errors(errors):
    for i in errors:
        for x in i:
            print(x)

if __name__ == '__main__':

    ID = '114oIOb8Ml45ET3aziBiaBlOl0TpbtLMT8-fkj6xGTTM'
    JSON_KLUC = "eshop-sheet-c38c9c8a59ed.json"
    sheets = get_sheet(ID, JSON_KLUC)
    processes_count = 30
    odd_residue = len(sheets) - (processes_count * (math.floor(len(sheets) / processes_count)))
    start_time = time.time()

    if odd_residue != 0:
        print("Processing an odd number of products...")
        sheets0 = sheets[0:len(sheets)-odd_residue]

        errors =_run_workers(processes_count=processes_count, sheets=sheets0)

        errors0 = _run_workers(processes_count=1, sheets=sheets, odd_residue= odd_residue)

        for k in errors0:
            errors.append(k)

        print_errors(errors)

        print("\n\n--This task took %s seconds--" % (time.time() - start_time))

    else:
        print("Processing an even number of products")
        errors = _run_workers(processes_count=processes_count, sheets=sheets)

        print_errors(errors)
        print("\n\n--This task took %s seconds--" % (time.time() - start_time))
