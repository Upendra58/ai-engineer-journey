# numpy 2d arrays

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data) # whole array
print(data.shape) # (3,3) 3X3 matrix 3 rows and 3 columns
print(data.ndim) #(2)dimension  3x3-- 2 dimension
print(data.size) #(9) total values 