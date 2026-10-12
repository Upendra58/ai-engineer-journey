import numpy as np

data = np.array(
    [
 [5, 10, 15],
 [20, 25, 30],
 [35, 40, 45]
]
)

print(data)
print(data.shape)
print(data.ndim)
print(data.size)
print(data[1,2]) # 30 # index starts from 0 so, 30 becomes 1st index( 2nd row, 2nd column)
print(data[2,1]) # 40
print(data[0:2, 0:2]) # slicing the data, data[start:stop], here data[0:2, 0:2] represents both rows and cloumns
# 0:2 start at 0th index and stop at 2nd index and in python stop is exclusive so o/p gives only two oth and 1st index
#[10 15]
print(data[0:1, 1:3])
#[[20 25 30]
#[35 40 45]]
print(data[1:4, 0:4])
#[15 30 45]
print(data[0:3, 2:3])
print(data[0, 1:3]) # 0 slects the exact row,(1st row) collapse the dimension to 1D
print(data[:, 2]) # : prnts all rows and 2 → select column index 2, which collapses that dimension → 1D