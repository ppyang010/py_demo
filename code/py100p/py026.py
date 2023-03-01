# 将unix时间戳转换成格式化日期

import datetime

unix_time = 1677677290

datetime_obj = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
