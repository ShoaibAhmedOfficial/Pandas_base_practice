import pandas as pd
var = pd.read_csv("D:\\Python\\Libraries\\Pandas\\ReadpandasCSV File.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# print(var.interpolate(methods={'linear','time','index','values','nearest','zero','slinear','quadratic','cubic','barycentric'
#                                ,'krogh','polynomial','spline','piecewise_polynomial','from_derivatives','pchip','akima'}))
# print(var.interpolate(method="linear",axis=0))
# print(var.interpolate(limit_direction="forward, backward, both",limit=2))
# print(var.interpolate(limit_area="inside, outside , both", inplace=True))
print(var.interpolate())
