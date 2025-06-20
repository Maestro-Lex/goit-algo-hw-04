import random
import timeit
import matplotlib.pyplot as plt
from sorting import *


def measure_time(data: list, sort_alg) -> tuple:
    '''
    Сортуємо дані та рахуємо час виконання
    '''
    sart_time = timeit.default_timer()
    sorted_data = sort_alg(data.copy())
    end_time = timeit.default_timer() - sart_time
    return sorted_data, end_time


def diagram(db: list[tuple]):
    '''
    Малюємо порівняльну діаграму
    '''
    plt.figure(figsize=(12, 8), constrained_layout = True)
    # обираємо палітру кольорів (наприклад: 'viridis', 'plasma', 'coolwarm', 'rainbow')
    cmap = plt.get_cmap('viridis')
    colors = [cmap(i / len(db)) for i in range(len(db))]
    
    # Цикл накладає блоки діаграми для кожного блоку даних на одну поверхню
    for i in db:
        width = 0.9
        color_index = 0
        for key in i[1].keys():
            plt.bar(
                str(i[0]),
                i[1][key][1],
                color = colors[color_index],
                edgecolor = "r",
                width = width,
                # ставимо позначки тільки один раз при першому прогоні зовнішнього циклу
                label = key if db.index(i) == 0 else '',
                log = True
            )
            width -= 0.15
            color_index += 1

    plt.xlabel("Кількість елементів", fontsize="small", color="midnightblue")
    plt.ylabel("Час опрацювання (с)", fontsize="small", color="midnightblue")
    plt.title("Порівняння алгоритмів сортування", fontsize=15)
    # Зміщуємо легенду за межі діаграми
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


def data_sort(number: int) -> dict:
    '''
    Словник відсортованих даних різними методами для певної кількості даних
    '''
    result = {}
    data = [random.randint(0, 1000) for _ in range(number)]
    result['Bubble sort'] = measure_time(data, bubble_sort)
    result['Insertion sort'] = measure_time(data, insertion_sort)
    result['Merge sort'] = measure_time(data, merge_sort)
    result['Timsort'] = measure_time(data, sorted)
    return result

def main():
    '''
    Формуємо список з наборів відсортованих даних для наборів різної кількості
    '''
    db = []
    for number in [10, 100, 1000, 5000, 10000]:
        db.append(tuple((number, data_sort(number))))
    diagram(db)


def merge_k_lists(k: list[list]):
    '''
    Необов'язкове завдання, як зрозумів
    '''
    data = []
    for lst in k:
        data += merge_sort(lst.copy())
    return merge_sort(data)


if __name__ ==  "__main__":
    main()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)