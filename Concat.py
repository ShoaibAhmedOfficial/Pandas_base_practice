import pandas as pd

sr1=pd.Series([1,2,3,4,5])
sr2=pd.Series([11,12,13,14,15])
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4,5],"B":[21,22,23,24,25]})

print(pd.concat([var1,var2],axis=1))

# print(pd.concat([var1,var2],axis=1, join="inner,outer,"))

print(pd.concat([var1,var2],axis=1, keys=["d1","d2"]))