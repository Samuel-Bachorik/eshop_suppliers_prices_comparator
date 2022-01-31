from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
from run_process import Process

process = Process()

def _run_workers(processes_count, sheets, odd_residue = None):

    num = processes_count

    if odd_residue is None:
        num_for_process = int(len(sheets)/num)

        stop_start_ids = [[0 for _ in range(2)] for _ in range(num)]

        for z in range(num):
            if z == 0:
                stop_start_ids[z][1] = num_for_process

            stop_start_ids[z][0] = stop_start_ids[z-1][1]
            stop_start_ids[z][1] = stop_start_ids[z][0] + num_for_process

        print("Started...\n")

    else:
        stop_start_ids = [[len(sheets) - odd_residue ,len(sheets)]]

    with ProcessPoolExecutor(max_workers=num) as executor:
        results = [None] * num
        for x in range(num):
            results[x] = executor.submit(process.process, sheets, stop_start_ids[x])

        errors = []
        for f in concurrent.futures.as_completed(results):
            x = f.result()
            errors.append(x)

        return errors
