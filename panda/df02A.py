import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z'])
print("df: ")
print(df)

print("--------------------------------------")
print("df.reset_index()")
print(df.reset_index())
print(df)

print("--------------------------------------")
print("newind = 'CA NY WY OR CO'.split()")
newind = 'CA NY WY OR CO'.split()
print(newind)

print("--------------------------------------")
print("df['States'] = newind")
df['States'] = newind
print(df)

print("--------------------------------------")
print("df.set_index('States')")
print(df.set_index('States'))
print(df)



