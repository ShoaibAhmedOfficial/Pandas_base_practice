import pandas as pd
import numpy as np
# pd.set_option('display.max_rows', None)       # jitni rows hain sab dikhayega
# pd.set_option('display.max_columns', None)    # jitne columns hain sab dikhayega
# pd.set_option('display.width', None)          # line wrap nahi hogi
# pd.set_option('display.max_colwidth', None)

csv_1 =pd.read_csv("ReadPandasCVS2.csv")
print(csv_1.to_string())
# # print(csv_1)
# print(csv_1.index)
# print(csv_1.columns)
# print(csv_1.describe())
# print(csv_1.head())
# print(csv_1.tail())
# print(csv_1[:2])
# print(type(csv_1))
# print(csv_1.index.array)
# print(csv_1.to_numpy())
# v =np.asarray(csv_1)
# print(v)
# this function change order of the list
# print(csv_1.sort_index(axis=0,ascending=False))
# csv_1["SYMBOL"][0]="python"
# print(csv_1)
# csv_1.loc[[0,3],["SYMBOL","SECURITY"]]
# print(csv_1.loc[[0,1,2,3],["SYMBOL","SECURITY"]])
# print(csv_1.loc[:,["SYMBOL","SECURITY"]])
# print(csv_1.loc[[0,1,2,3],:])
# print(csv_1.iloc[0,0])
# print(csv_1.drop("SECURITY",axis=1))


