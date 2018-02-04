import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

outside = ['G1', 'G1','G1','G2','G2','G2']
print("outside")
print(outside)
inside = [1,2,3,1,2,3]
print("inside")
print(inside)
print("--------------")
print("zip(outside, inside)")
print(zip(outside, inside))
print("list(zip(outside, inside)")
print(list(zip(outside, inside)))
hier_index = list(zip(outside, inside))
print("hier_index")
print(hier_index)
print("--------------")
hier_index = pd.MultiIndex.from_tuples(hier_index)
print("hier_index")
print(hier_index)
print("--------------")
df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
print("df")
print(df)
print("--------------")
print("df.loc['G1']")
print(df.loc['G1'])
print("--------------")
print("df.loc['G1'].loc[1]")
print(df.loc['G1'].loc[1])
print("--------------")
print("df.index")
print(df.index)
print("df.index.names")
print(df.index.names)
print("--------------")
print("df.index.names = ['Groups','Num']")
df.index.names = ['Groups','Num']
print("df.index")
print(df.index.names)
print("df")
print(df)
print("--------------")
print("df.loc['G2']")
print(df.loc['G2'])
print("df.loc['G2'].loc[2]")
print(df.loc['G2'].loc[2])
print("df.loc['G2'].loc[2]['B']")
print(df.loc['G2'].loc[2]['B'])
print("df.loc['G2'].loc[2].loc['B']")
print(df.loc['G2'].loc[2].loc['B'])
print("--------------")
print("df.loc['G1'].loc[3].loc['A']")
print(df.loc['G1'].loc[3].loc['A'])
print("--------------")
print("df.loc['G1']")
print(df.loc['G1'])
print("df.xs('G1')")
print(df.xs('G1'))
print("--------------")
print("df")
print(df)
print("df.xs(1,level='Num')")
print(df.xs(1,level='Num'))









