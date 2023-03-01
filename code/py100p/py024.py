# 计算任意日期7天前的日期

import datetime


def get_diff_date(pDate, days):
    pDate_date = datetime.datetime.strptime(pDate, "%Y-%m-%d")
    # timedelta类 时间差类
    # https://blog.csdn.net/weixin_43298886/article/details/108312568
    date_gap = datetime.timedelta(days=days)
    res_date = pDate_date - date_gap
    return res_date.strftime("%Y-%m-%d")


print(get_diff_date("2023-03-01", 1))
print(get_diff_date("2023-03-01", 3))
print(get_diff_date("2023-03-01", 7))
print(get_diff_date("2023-01-01", 7))
