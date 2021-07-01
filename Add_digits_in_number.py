def add_digits(number: int):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number[0])
    else:
        new_str_number = str_number[1:len(str_number)]
        return int(str_number[0]) + add_digits(int(new_str_number))


number = int(input('Enter some number: '))
print(add_digits(number))