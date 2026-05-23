# Algoritma Bubble Sort

def bubble_sort(arr):

    arr = arr.copy()  # menyalin array

    n = len(arr)  # jumlah data

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr