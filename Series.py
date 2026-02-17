import pandas as pd

x=[1,2,3,4,5,6]
var=pd.Series(x,index=['a','b','c','d','e','f'],dtype="float",name="python")

print(var)
print(type(var))
print(var[2])

dic = {"name":['python','c','c++','java'],"por":[12,13,14,15],"rank":[1,2,3,4]}
var1=pd.Series(dic)
print(var1)

s=pd.Series(12,index=[1,2,3,4,5])
print(s)
print(type(s))

s1=pd.Series(12,index=[1,2,3,4,5])
s2=pd.Series(12,index=[1,2,3])

print(s1+s2)

