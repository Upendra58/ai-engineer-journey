#set  comprehension, square of even numbers

numbers = [1, 2, 3, 4, 5, 6, 6, 4, 2]

squares= {number*number for number in numbers if number %2== 0} # use {} for set

print(squares)