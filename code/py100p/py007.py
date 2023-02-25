# 数字范围内的所有偶数


def get_even_numbers(begin, end):
    res = []
    # 不包括end
    for i in range(begin, end):
        if (i % 2 == 0):
            res.append(i)

    return res


begin = 4
end = 15

print(f"begin={begin},end={end}, env numbers: ", get_even_numbers(begin, end))

# 列表推导式的方式  等效上面的函数   get_even_numbers
# 推导式有点类似 java 中的list stream  将可以从一个数据序列构建另一个新的数据序列的结构体  可用于转换列表 or 筛选列表
# https://geek-docs.com/python/python-tutorial/python-listcomprehensions.html

# L = [expression for variable in sequence [if condition]]
# 它由三部分组成：表达式 ,for 循环，可选条件。 for 循环遍历整个序列。 对于每个循环，如果满足条件，则执行表达式进行求值。 如果计算出该值，它将被添加到新列表中。
# for 循环 可以有多个 , 每个for循环后面的 if 条件也可以有多个。

data = [i for i in range(begin, end) if i % 2 == 0]
print(f"begin={begin},end={end}, env numbers: ", data)

# 扩展
# 双重循环实例

a = [1, 2, 3]
b = ['A', 'B', 'C']

# 求笛卡尔积
def dikaer(listA, listB):
    res = []
    for i in listA:
        for j in listB:
            res.append(str(i) + j)
    return res

# 列表推导式写法
c = [str(i) + j for i in a for j in b]
print(dikaer(a, b))
print(c)


# python中还有
# 列表(list)推导式
# 字典(dict)推导式
# 集合(set)推导式