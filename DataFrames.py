import pandas as pd

l=[1,2,3,4,5]
var = pd.DataFrame(l)
print(var)

d = {"a":[1,2,3,4,5],"s":[1,2,3.4,5.6,7]}
var1=pd.DataFrame(d)
print(var1)

z = {"a":[1,2,3,4,5],"s":[1,2,3.4,5.6,7], 1:[6,54,43,23,23]}
var1=pd.DataFrame(z,columns=["a",1],index=[4,3,2,1,0])
print(var1)

list_1 =[[1,2,3,4,5],[1,2,3,4,5]]
var2=pd.DataFrame(list_1)
print(var2)

sr = {"s":pd.Series([1,2,3,4,5]),"r":pd.Series([1,2,3,4,5])}
var3=pd.DataFrame(sr)
print(var3)