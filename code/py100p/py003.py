# 计算圆的面积

import math


# r半径 limit 保留小数位数
def cal(r, limit):
    return round(math.pi * r * r, limit)


print("pi=", math.pi)
print("计算园的面积 r=3 res=", cal(3, 2))
print("计算园的面积 r=5.5 res=", cal(5.5, 2))
