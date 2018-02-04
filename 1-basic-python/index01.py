import numpy as np

print("=====================")
arr = np.arange(0,11)
print(arr)
print("=====================")
print(arr[1:5])
print("=====================")
print(arr[:5])
print("=====================")
print(arr[5:])
print("=====================")
arr[0:5] = 100
print(arr)
print("=====================")
slice_arr = arr[0:6]
print(slice_arr)
print(arr)
print("=====================")

