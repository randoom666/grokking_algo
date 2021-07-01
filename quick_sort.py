import random
def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


array = [random.randrange(0, 1000) for i in range(1000)]
print('Unsorted:', array, '\nLenght:', len(array))
print('Sorted:', quick_sort(array))