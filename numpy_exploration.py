import ctypes
import numpy as np

library = ctypes.CDLL("./math_functions.dll")


#Normal implementation of squaring array
numbers = [1, 2, 3, 4, 5]
squared = []
for number in numbers:
    squared.append(number * number)

#NumPy implementation of squaring array
numbers = np.array([1, 2, 3, 4, 5])
squared = numbers * numbers
print(squared)


#Very basic machine learning example 
inputs = np.array([0.5, 0.8, 0.2])

weights = np.array([
    [0.1, 0.4, 0.3],
    [0.7, 0.2, 0.5],
    [0.6, 0.9, 0.1]
])

outputs = weights @ inputs

print(outputs)

#Basic financial (stock) example
prices = np.array([100, 105, 103, 110, 115])

daily_changes = prices[1:] - prices[:-1]

print(daily_changes)