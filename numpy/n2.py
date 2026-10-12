import numpy as np

numbers = np.array([5, 10, 15, 20, 25])

print(numbers) # print numbers
print(type(numbers)) # type of numbers
print(numbers[0]) # first element
print(numbers[-1]) # last element

print(numbers.shape)
print(numbers.ndim)
print(numbers.size)

#output for shape, ndim, size
#shape → (5,) → 5 elements in one dimension
#ndim → 1 → one-dimensional array
#size → 5 → total number of elements