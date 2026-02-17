import pandas as pd

var =pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
# print(var)

# var["python_1"]=var["A"][:3]
# print(var)

var1= var.pop("B")
print(var1)
print(var)