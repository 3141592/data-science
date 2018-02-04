import numpy as np

print("arr")
arr = np.arange(0,11)
print(arr)

print("=============")
print("arr[8]")
print(arr[8])

print("=============")
print("arr[1:6]: ")
print arr[1:6]

print("=============")
print "arr[:6]"
print arr[:6]

print("=============")
print "arr[0:5] = 100"
arr[0:5] = 100
print arr

print("=============")
arr_2d = np.array([[5,10,15],[20,25,30],[30,35,40]])
print "arr_2d"
print arr_2d


print("=============")
print "arr_2d[0][0]"
print arr_2d[0][0]

print "arr_2d[1][1] = 25"
print arr_2d[1][1]

print "arr_2d[0][2] = 15"
print arr_2d[0][2]


print "arr_2d[0,0]"
print arr_2d[0,0]

print "arr_2d[1,1] = 25"
print arr_2d[1,1]

print "arr_2d[0,2] = 15"
print arr_2d[0,2]

print "=============="
arr3 = (np.random.rand(1,25)*10).reshape(5,5)
print "arr3"
print arr3

print "arr3[:3,2:]"
print arr3[:3,2:]

print "arr3[:3,:2]"
print arr3[:3,:2]

print "=============="
arr = np.arange(1,11)
print "np.arange91,11)"
print arr

print "arr > 5"
print arr > 5

bool_arr = arr > 6
print "bool_arr"
print bool_arr


print "arr[bool_arr]"
print arr[bool_arr]









