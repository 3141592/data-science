import numpy as np

mat = np.arange(1,26).reshape(5,5)
print(mat)

print("mat[2:5,1:5]")
print(mat[2:5,1:5])

print("mat[2:,1:]")
print(mat[2:,1:])

print(mat[3,4])

print("mat[0:3,1:2]")
print(mat[0:3,1:2])

print("mat[:3,1:2]")
print(mat[:3,1:2])

print("mat[4]")
print(mat[4])

print("mat[4,:]")
print(mat[4,:])

print("mat[3:5]")
print(mat[3:5])

print("mat[3:5,:]")
print(mat[3:5,:])

print("np.sum(mat)")
print (np.sum(mat))

print("mat.sum()")
print (mat.sum())

print("mat.std()")
print(mat.std())

print("mat.sum(axis=0))")
print(mat.sum(axis=0))

