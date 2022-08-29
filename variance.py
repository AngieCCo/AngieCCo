# Write a function that receives 1 list of numbers and returns their variance
from average import aver_nums
print("after import")
def var_nums(numbers: list):

    m_val = aver_nums(numbers)
    mues_total = len(numbers) - 1
    x_sigma = 0
    total = 0

    for num in numbers:
        x_sigma = (num - m_val)
        square_sum = x_sigma ** 2
        total += square_sum

    return total / mues_total


print(var_nums([5,10,15]))







