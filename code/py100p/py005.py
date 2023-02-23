# 求前n个数字的平方和

def sum_of_square(n):
    res = 0;
    for idx in range(1, n + 1):
        res = res + idx * idx
    return res


print("3的平方和=", sum_of_square(3))
print("5的平方和=", sum_of_square(5))
