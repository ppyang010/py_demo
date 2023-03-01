# 计算开始结束范围内的所有日期

# 输入 开始日期  结束日期 打印两个时间时间的每一天

import datetime


def get_date_range(begin_date, end_date):
    date_list = []
    date_gap = datetime.timedelta(days=1)
    while begin_date <= end_date:
        begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        begin_date_obj = begin_date_obj + date_gap
        begin_date = begin_date_obj.strftime("%Y-%m-%d")
        date_list.append(begin_date)
    return date_list


begin_date = "2022-03-01"
end_date = "2022-05-31"

print(get_date_range(begin_date, end_date))
