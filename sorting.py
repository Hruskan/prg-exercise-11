import random
import matplotlib.pyplot as plt

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
    return values

def bubble_sort(numbers):
    values = numbers.copy()
    plt.ion()
    plt.show()
    for u in range(len(values)-1):
        for i in range(len(values)-u-1):
            if values[i] > values[i+1]:
                values[i], values[i+1] = values[i+1], values[i]
        index_highlight1 = u
        index_highlight2 = u + 1
        colors = ["steelblue"] * len(values)
        colors[index_highlight1] = "tomato"
        colors[index_highlight2] = "tomato"
        plt.clf()
        plt.bar(range(len(values)), values, color=colors)
        plt.title("Bubble Sort")
        plt.pause(0.5)
    plt.ioff()
    plt.show()
    return values

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    print(selection_sort(values))
    print(bubble_sort(values))
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

