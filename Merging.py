import pandas as pd

var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4,5],"B":[21,22,23,24,25]})
print(pd.merge(var1,var2,on="A"))
# print(pd.merge(var1,var2, how="inner,left,right,outer,", indicator=True))
print(pd.merge(var1,var2,left_index=True,right_index=True, suffixes=("name","value")))