
def cal_average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for  number in numbers:
        total += number
    return total/len(numbers)

numbers = [10, 20, 30, 40, 50]
result = cal_average(numbers)
print(result)
empty_result = cal_average([])
print(empty_result)