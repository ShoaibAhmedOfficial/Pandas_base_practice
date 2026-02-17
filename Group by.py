import pandas as pd
var=pd.DataFrame({
    "name": ["a","b","c","d","a","b","d","c","a","b"],
    "Sub1": [12,13,14,14,15,14,16,15,16,17],
    "Sub2":[11,12,13,14,15,16,17,18,19,20]
})
# print(var)
var1 = var.groupby("name")
# print(var1)
# for x,y in var1:
#     print(x)
#     print(y)

# print(var1.get_group("a"))
# print(var1.min())
# print(var1.max())
# print(var1.mean())

li =list(var1)
print(li)