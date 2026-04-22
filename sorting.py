import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    values = numbers.copy()
    for u in range(len(values)):
        min_index = u
        min_value = values[min_index]
        for i in range(u + 1, len(values)):
            if values[i] < min_value:
                min_index = i
                min_value = values[i]
        values[u], values[min_index] = values[min_index], values[u]
        print(values)
    return values

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    selection_sort(values)
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

