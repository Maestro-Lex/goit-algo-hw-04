def bubble_sort(data: list):
    n = len(data)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if data[j] > data[j +1 ]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def insertion_sort(data: list):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
        data[j+1] = key 
    return data


def selection_sort(data: list):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged