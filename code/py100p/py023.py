# 计算两个日期的相隔天数
import datetime

birthday = "1994-12-17"
# str to date
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))

curr_date = datetime.datetime.now()
print(curr_date, type(curr_date))

# python中datetime对像可以直接相减
minus = curr_date - birthday_date
print(minus, type(minus))
print(minus.days)
print(minus.days / 365)
