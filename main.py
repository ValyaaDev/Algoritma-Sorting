import time

from dataset import (
    best_case,
    worst_case,
    average_case
)

from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


# Menghitung waktu eksekusi
def calculate_time(sort_function, data):
    start = time.perf_counter()
    # Semua algoritma di proyek ini mengembalikan array hasil urut
    # dan (secara umum) tidak perlu melakukan in-place pada input asli.
    sort_function(data.copy())
    end = time.perf_counter()
    return (end - start) * 1000


# Ukuran dataset
dataset_sizes = [
    100000,
    200000
]


# Daftar algoritma
algorithms = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
}


# Pengujian
for size in dataset_sizes:

    print(f"\n===== DATASET {size} =====")

    datasets = {
        "Best Case": best_case(size),
        "Worst Case": worst_case(size),
        "Average Case": average_case(size)
    }

    for algo_name, algo_function in algorithms.items():

        print(f"\n{algo_name}")

        for case_name, data in datasets.items():

            times = []

            for _ in range(3):

                execution_time = calculate_time(
                    algo_function,
                    data
                )

                times.append(execution_time)

            average_time = sum(times) / len(times)

            print(
                f"{case_name}: "
                f"{average_time:.2f} ms"
            )