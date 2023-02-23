# 数据类型转换


a=int('123')
print(a)
a=int(12.34)
print(a)
a=float('12.34')
print(a)
a=str(1.23)
print(a)
a=str(100)
print(a)
a=bool(1)
print(a)
a=bool('')
print(a)

# 自定义函数

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
x=my_abs(-100)
print(x)

# 空函数
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

def nop():
    pass

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值
# # 函数可以返回多个值吗？答案是肯定的。
# #
# # 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

x, y = move(100, 100, 60, math.pi / 6)
r= move(100, 100, 60, math.pi / 6)
print(x,y)
print(r)



# 小结
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。




# 函数的参数
# 函数的默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

x = power(10)
print(x)

# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#
# 二是如何设置默认参数。

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。

# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

x = enroll('hello','man',city='大地')

# 默认参数使用不当的问题

def add_end(L=[]):
    L.append('END')
    return L

x=add_end()
x=add_end()
print(x)

# 上述打印内容为['END', 'END']

# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# -------重要----------
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 现在，无论调用多少次，都不会有问题：

x=add_end()
x=add_end()
x=add_end()
x=add_end()
print(x)

# 可变参数
# 定义可变参数函数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4,5,6,7,8,9))
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
l=[1,2,4]
print(calc(*l))



# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Michael', 30)

# 也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

# 仍以person()函数为例，我们希望检查是否有city和job参数：

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 但是调用者仍可以传入不受限制的关键字参数：



# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('123',24,city='1',job='2')

# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
#



# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 比如定义一个函数，包含上述若干种参数：


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)