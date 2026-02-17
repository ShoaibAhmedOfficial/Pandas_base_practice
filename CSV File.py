import pandas as pd

dis={"a":[1,2,3,4],"b":[5,6,7,8],"c":[9,1,2,3]}
d=pd.DataFrame(dis)
print(d)
d.to_csv("Test2.csv",index=False,header=["q","w","e"]) #only make the CSV file
#index=False# this command removed the index
#header=[1,2,3]# this command change the header name