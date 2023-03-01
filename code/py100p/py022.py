# 获取当前的日期和时间

import datetime

curr_datatime = datetime.datetime.now()

print(curr_datatime, type(curr_datatime))
# 格式化时间  返回字符串
# datetime to string
curr_str = curr_datatime.strftime("%Y-%m-%d %H:%M:%S")
print(curr_str)

#
print("year=", curr_datatime.year)
print("month=", curr_datatime.month)
print("day=", curr_datatime.day)
print("hour=", curr_datatime.hour)
print("minute=", curr_datatime.minute)
print("second=", curr_datatime.second)
print("ms=", curr_datatime.microsecond/1000)
print("microsecond=", curr_datatime.microsecond)
print("timestamp=", curr_datatime.timestamp())
