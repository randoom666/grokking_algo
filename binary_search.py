def binary_search(input_list: list, searched: int):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = input_list[mid]
        if guess == searched:
            return guess, mid
        if guess > searched:
            high = mid - 1
        else:
            low = mid + 1
    return None, None


test_list = [2, 3, 5, 7, 9, 11, 13]
find1, pos1 = binary_search(test_list, 2)
find2, pos2 = binary_search(test_list, -1)
print(find1, 'is in position', pos1)
if find2 and pos2:
    print(find2, 'is in position', pos2)
else:
    print('Not found')
