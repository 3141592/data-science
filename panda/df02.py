import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z'])
print("df: ")
print(df)
print("--------------------------------------")
print("df > 0")
print(df > 0)

print("--------------------------------------")
print("booldf = df > 0")
booldf = df > 0
print("booldf")
print(booldf)
print("--------------------------------------")
print("df[booldf]")
print(df[booldf])

print("--------------------------------------")
print("df[df > 0]")
print(df[df > 0])

print("--------------------------------------")
print("df['W'] > 0")
print(df['W'] > 0)

print("--------------------------------------")
print("df[df['W'] > 0]")
print(df[df['W'] > 0])

print("--------------------------------------")
print("df[df['Z'] < 0]")
print(df[df['Z'] < 0])

print("--------------------------------------")
print("type(df['W'] > 0)")
print(type(df['W'] > 0))

print("--------------------------------------")
print("type(df[df['W'] > 0])")
print(type(df[df['W'] > 0]))

print("--------------------------------------")
print("resultdf = df[df['W'] > 0]")
resultdf = df[df['W'] > 0]
print(resultdf)

print("--------------------------------------")
print("resultdf['X']")
print(resultdf['X'])

print("--------------------------------------")
print("df[df['W'] > 0]['X']")
print(df[df['W'] > 0]['X'])

print("--------------------------------------")
print("df[df['W'] > 0][['Y','X']]")
print(df[df['W'] > 0][['Y','X']])

print("--------------------------------------")
print("df[(df['W'] > 0)]")
print(df[(df['W'] > 0)])

print("--------------------------------------")
print("df[(df['W'] > 0) & (df['Y'] > 1)]")
print(df[(df['W'] > 0) & (df['Y'] > 1)])

print("--------------------------------------")
print("df[(df['W'] > 0) | (df['Y'] > 1)]")
print(df[(df['W'] > 0) | (df['Y'] > 1)])

print("--------------------------------------")
print("df[(df['W'] > 0) | (df['Y'] > 1)]")
print(df[(df['W'] > 0) | (df['Y'] > 1)])


