print('包含中文的str')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
a = ord('A')
print(a)
a = ord('中')
print(a)
# 如果知道字符的整数编码，还可以用十六进制这么写str：
a = '\u4e2d\u6587'
# 中文
print(a)


# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
x = b'ABC'
print(x)


# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
x ='ABC'.encode('ascii')
print(x)

x ='中文'.encode('utf-8')
print(x)
# x ='中文'.encode('ascii')
# print(x)


# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

x=b'ABC'.decode('ascii')
print(x)

x=b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# 打印  '中文'
print(x)



# 如果bytes中包含无法解码的字节，decode()方法会报错：
# x=b'\xe4\xb8\xad\xff'.decode('utf-8')
# print(x)

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

x = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(x)

# 要计算str包含多少个字符，可以用len()函数：
x= len('ABC')
print(x)

x=len('中文')
print(x)


# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
x=len(b'ABC')
print(x)

x=len(b'\xe4\xb8\xad\xe6\x96\x87')
print(x)

x=len('中文'.encode('utf-8'))
print(x)
# 字符串格式化1
# 你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))
x='Age: %s. Gender: %s' % (25, True)
print(x)


# format()
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
x= 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
print(x)

# f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')