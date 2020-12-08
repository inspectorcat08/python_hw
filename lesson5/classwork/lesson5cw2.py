def my_square(num):
    if num%num==0 and num%1==0 and num%2!=0 and num%(num**0.5)!=0:
        return num**2
    elif num == 2:
        return num**2
    else:
        return num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25]

squared_numbers = list(map(my_square, numbers))

print(squared_numbers)


