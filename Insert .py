import pandas as pd

var = pd.DataFrame({"A":[1,2,3,4,5,6],"B":[6,5,4,3,2,1]})
print(var)

var.insert(1,"python",var["A"])
print(var)

var.insert(1,"python_1",[11,22,33,44,55,66])
print(var)