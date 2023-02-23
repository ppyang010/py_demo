# 计算阶乘函数
def get_jiecheng(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1

    return res


print("计算3的阶乘 = ", get_jiecheng(3))
print("计算6的阶乘 = ", get_jiecheng(6))
print("计算100的阶乘 = ", get_jiecheng(100))
