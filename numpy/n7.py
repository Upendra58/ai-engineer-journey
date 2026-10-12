# 2D Aggregation

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.sum(data))
print(np.mean(data))

print(np.sum(data, axis=0)) # sum of rows- result in column
print(np.sum(data, axis=1)) # sum of columns - result in rows