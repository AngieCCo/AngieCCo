# Write a function that receives 1 list of numbers and returns their average.

def aver_nums(numbers: list):

    sum_nums = 0

    for x in numbers:
        sum_nums += x

    return sum_nums / len(numbers)


print(aver_nums([1,2,3,4,5,6,7,8,9,10]))
