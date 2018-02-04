import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

print("labels: {}".format(labels))
print("my_data: {}".format(my_data))
print("arr: {}".format(arr))
print("d: {}".format(d))
print("----------------")
print("pd.Series(data = my_data)")
print(pd.Series(data = my_data))
print("----------------")
print("pd.Series(data = my_data, index = labels)")
print(pd.Series(data = my_data, index = labels))
print("----------------")
print("pd.Series(arr)")
print(pd.Series(arr))
print("----------------")
print("pd.Series(arr,labels)")
print(pd.Series(arr,labels))
print("----------------")

print("pd.Series(d)")
print(pd.Series(d))
print("----------------")

print("pd.Series(labels)")
print(pd.Series(labels))
print("----------------")

print("ser1 = pd.Series([1,2,3,4],['USA','Ger','Japan','USSR'])")
ser1 = pd.Series([1,2,3,4],['USA','Ger','Japan','USSR'])
print("pd.Series(ser1)")
print(pd.Series(ser1))
print("----------------")

print("ser2 = pd.Series([1,2,5,4],['USA','Ger','Italy', 'Japan'])")
ser2 = pd.Series([1,2,5,4],['USA','Ger','Italy', 'Japan'])
print("pd.Series(ser2)")
print(pd.Series(ser2))
print("----------------")
print("ser1['USA']")
print(ser1['USA'])
print("----------------")
ser3 = pd.Series([labels])
print("pd.Series(ser3)")
print(pd.Series(ser3))
print("----------------")
print("ser1 + ser2")
print(ser1 + ser2)

print("----------------")
print("ser1 + ser2")
print(ser1 + ser2)

print("----------------")

