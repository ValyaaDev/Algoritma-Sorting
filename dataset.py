import random

# Best Case
def best_case(n):
    return list(range(n))

# Worst Case
def worst_case(n):
    return list(range(n, 0, -1))

# Average Case
def average_case(n):
    return [random.randint(1, 1000000) for _ in range(n)]