import numpy as np

mymat = [[1,2,3],[4,5,6],[7,8]]
print mymat

print(np.array(mymat))
print(np.array(mymat)[2])

print(np.zeros(10))

print(np.ones(10))

print(np.ones(10)*5)
print(np.zeros(10) + 5)

print("======================")
print("np.arange")
print(np.arange(10,51))
print(np.arange(10,51,2))

print("======================")
print("np.arange.reshape")
print(np.arange(0,9).reshape(3,3))
print(np.arange(9).reshape(3,3))

print("======================")
print("np.eye")
print(np.eye(3))
print(np.eye(4))

print("======================")
print("npy.random")
print(np.random.rand(1))
print(np.random.rand(5))

print(np.random.randn(1,25))
print(np.random.randn(25))

print("======================")
print("npy.linspace")
print(np.linspace(0.01,1.,100).reshape(10,10))
print(np.arange(1.,101.).reshape(10,10)/100)

print(np.linspace(0., 1., 20))

print("======================")
print("npy.randint")
print(np.random.randint(1,100))
print(np.random.randint(1,100,10))

print("======================")
print("Arrays")
print("arr")
arr = np.arange(25)
print(arr)
print("ranarr")
ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print("arr.reshape(5,5)")
print(arr.reshape(5,5))
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())

print(arr.shape)
print(ranarr.shape)
print(arr.reshape(5,5).shape)

print(arr.dtype)




