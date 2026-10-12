#3 students and 3 marks frmo 3 subjets column represent subjects maths, english science
#Using NumPy:
#1. Find the total score of each student
#2. Find the average score of each student
#3. Find the highest score in each subject
#4. Find the overall average score

import numpy as np
scores = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print(np.sum(scores, axis=1))
print(np.mean(scores, axis=1))
print(np.max(scores,axis=0))
print(np.mean(scores))