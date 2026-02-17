import pandas as pd

# This line reads your CSV file into a DataFrame
csv_1 = pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv")

# This line correctly prints the DataFrame
print(csv_1)
csv_2 = pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv",nrows=1)

# This line correctly prints the DataFrame
print(csv_2)

csv_3 = pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv",usecols=["SYMBOL"])

# This line correctly prints the DataFrame
print(csv_3)
# This code is for skip the rows in the csv file
csv_4 = pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv", skiprows=[0,4,12,13])
print(csv_4)

# This code is for change the index value in CSV file
csv_5 =pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv", index_col="SYMBOL")
print(csv_5)
# row convert into header
csv_6 =pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv", header=None, prefix="col")
print(csv_6)
# if change the header so only use names and change header name
csv_7 =pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv", names=["Hello"])
print(csv_7)

csv_8 =pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadPandasCVS2.csv", dtype={"TODAY - VOLUME": "float"} )
print(csv_8)

