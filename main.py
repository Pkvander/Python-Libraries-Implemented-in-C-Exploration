import ctypes
import time
import statistics
from array import array

SIZE = 1_000_000

library = ctypes.CDLL("./math_functions.dll")

library.add.argtypes = [ctypes.c_int, ctypes.c_int]
library.add.restype = ctypes.c_int

library.square_numbers.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int
]
library.square_numbers.restype = None

def square_python(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]


#arrays for holding multiple trial results
python_times = []
c_times = []

for trial in range(5):
    python_numbers = array('i', (i % 1000 for i in range(SIZE)))
    c_numbers = array('i', (i % 1000 for i in range(SIZE)))

    #Python trial
    start = time.perf_counter()
    square_python(python_numbers)
    end = time.perf_counter()
    python_times.append(end - start)

    #C trial
    c_array = (ctypes.c_int * SIZE).from_buffer(c_numbers)
    start = time.perf_counter()
    library.square_numbers(c_array, SIZE)
    end = time.perf_counter()
    c_times.append(end - start)

python_average = statistics.median(python_times)
c_average = statistics.median(c_times)

print("Python median time:", python_average, "seconds")
print("C median time:", c_average, "seconds")

print("C is", round(python_average / c_average, 2), "times faster")


result = library.add(5, 3)
print(result)