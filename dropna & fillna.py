import pandas as pd
var = pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadpandasCSV File.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# Axis the mutabiq agrr kare to axis ki value agrr 1 pass kare to column k according value show nhh hogi
# print(var.dropna(axis=0, how="all","any"))
# print(var.dropna(subset=["change"]))
# print(var.dropna(inplace=True))
# var.dropna(thresh=2)
# print(var.fillna({" SYMBOL":"Python","SECURITY":"Company","TODAY - VOLUME":23242324,"AVG. VOLUME":100, "CHANGE":60.23}))
# print(var.fillna(method="ffill"))
# # print(var.fillna(method="bfill", axis=1 is for columns, 0 according to rows))
# print(var.fillna(12, inplace=True))
# print(var)
print(var.fillna("Python",limit=2))

