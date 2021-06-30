def find_smallest(arr: list):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_idx = i
    return smallest_idx


def selection_sort(arr: list):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(smallest)
    return new_arr


unsorted_arr = [4, 5, 1, 6, 2, 3, 9]
print(unsorted_arr)
sorted_arr = selection_sort(unsorted_arr)
print(sorted_arr)
