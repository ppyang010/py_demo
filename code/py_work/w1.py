import json
import jsonpath

import requests
# import pymysqlUtil
import random
import hashlib
# import Sha1Util
# import MD5Util

import time


def generate_data(id, page, break_point, secret, token, app_id, user_id):
    data = {
        'obj_id': id,
        'module_type': 1,
        'user_id': user_id,
        'comment_type': 2,
        'break_point': break_point,
        'page': page,
        'secret': secret,
        'app_id': app_id,
        'token': token
    }
    return data


def generate_header(timestamp, signature):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36',
        'timestamp': str(timestamp),
        'signature': signature,
        'client-type': 'android',
        'app-version': '218',
        'uuid': 'ef0a43be9f839750',
        'mobile-info': 'Redmi Note 4',
        'Content-type': 'application/x-www-form-urlencoded',
        'channel': '10000',
        'Content-Length': '191',
        'Host': 'api.yikaobang.com.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    return headers


def get_content(url, question_id, page, break_point, secret, token, user_id, timestamp, app_id):
    data = generate_data(question_id, page, break_point, secret, token, app_id, user_id)

    signature = getSign(break_point, question_id, page, secret, token, user_id, timestamp, app_id)
    headers = generate_header(timestamp, signature)
    proxy = {
        'http': '120.55.241.19:80'
    }

    response = requests.post(url, data=data, headers=headers, proxies=proxy)

    # 返回报文
    content = response.text
    return content


def getSign(break_point, obj_id, page, secret, token, user_id, timestamp, app_id):
    # app_id = 12
    # break_point = '2022-05-17T06:17:47Z'
    comment_type = 2
    module_type = 1
    # obj_id = 545313
    # page = 1
    # secret = '55eaf5e579f35859fa41dbee971cebc0'
    # token = '98693a85fd0969c9a6e6c1edebe17bf0'
    # user_id = 1525550
    # timestamp = 1652768267

    str1 = 'app_id=' + str(app_id) + 'break_point=' + str(break_point) + 'comment_type=' + str(
        comment_type) + 'module_type=' + str(module_type) + 'obj_id=' + str(obj_id) + 'page=' + str(
        page) + 'secret=' + secret + 'token=' + token + 'user_id=' + str(user_id) + str(app_id) + str(timestamp)

    # md5Secret = MD5Util.MD5Secret()
    # md5_str = md5Secret.md5_secret_str(str1)

    md5 = hashlib.md5()
    md5.update(str1.encode('utf-8'))
    md5_str = md5.hexdigest()

    str2 = md5_str + 'bfde83c3208f4bfe97a57765ee824e92'

    # sha1Secret = Sha1Util.Sha1Secret()
    # signature = sha1Secret.sha1_secret_str(str2)
    sha1 = hashlib.sha1()
    sha1.update(str2.encode('utf-8'))
    signature = sha1.hexdigest()
    print("signature= ", signature)
    return signature


# 获取总页数
def get_total_page_num(total, pageSize):
    return total // pageSize + 1


# 处理评论数据
def deal_comment(array, hot):
    total = []
    for i in range(len(array)):
        content = array[i]['content'][:3000]
        comment = (
            array[i]['id'], array[i]['obj_id'], array[i]['user_id'], content, array[i]['praise_num'], hot)
        total.append(comment)

    # 批量插入
    sql = "INSERT INTO question_comment (ref_id, question_id,user_id,content,praise_num,hot) VALUES (%s, %s, %s, %s, %s,%s)"
    db = pymysqlUtil.PymysqlDB()
    db.insert_list(sql, total)


# 处理热评
def save_hot_comment(questionId):
    # 处理热评
    hot_url = 'https://api.yikaobang.com.cn/index.php/Comment/Main/list'
    page = 1

    content = get_content(hot_url, questionId, page)
    print(content)

    hotList = json.loads(content)["data"]["hot"]
    print(hotList)
    deal_hot_comment(hotList, 1)

    while content != '':
        hotList = json.loads(content)["data"]["hot"]
        print(hotList)
        deal_hot_comment(hotList, 1)
        page = page + 1


def deal_hot_comment(array, hot):
    db = pymysqlUtil.PymysqlDB()

    for i in range(len(array)):
        ref_id = array[i]['id']
        print(ref_id)
        # 根据ref_id查询评论是否已经存在
        select_sql = 'select id,content,hot from question_comment where ref_id = %s'
        select_value = ref_id
        question = db.select_one(select_sql, select_value)

        if question:
            # 不为空则更新
            sql = "update question_comment set hot = %s where ref_id = %s"
            value = (hot, ref_id)
            db.update(sql, value)
        else:
            # 插入
            insert_value = (
                array[i]['id'], array[i]['obj_id'], array[i]['user_id'], array[i]['content'], array[i]['praise_num'],
                hot)
            insert_sql = "INSERT INTO question_comment (ref_id, question_id,user_id,content,praise_num,hot) VALUES (%s, %s, %s, %s, %s,%s)"

            print("insert_value= ", insert_value)
            db.insert(insert_sql, insert_value)


def save_comment(app_id, questionId):
    # 获取总页码
    url = 'https://api.yikaobang.com.cn/index.php/Comment/Main/list'
    timestamp = (int)(time.time())
    # timestamp = 1701224479
    print('timestamp=', timestamp)
    break_point = timestamp
    secret = '13b20ada6e24e099181b5c027de4c894'
    token = '44f4cb124e5076848f2b33bda6fd8202'
    user_id = 1525550
    # questionId = 946681

    page = 1
    timeLineList = []
    # 落库
    while page <= 2:
        # 1.请求数据
        content = get_content(url, questionId, page, break_point, secret, token, user_id, timestamp, app_id)
        print('page=', page)
        print('content= ', content)
        # 2.下载
        timeLineList = json.loads(content)["data"]["time_line"]
        print('timeLineList= ', timeLineList)
        if len(timeLineList) == 0:
            break
        # deal_comment(timeLineList, 0)
        page = page + 1

    # 处理热评
    page = 1
    content = get_content(url, questionId, page, break_point, secret, token, user_id, timestamp, app_id)
    hotList = json.loads(content)["data"]["hot"]
    # deal_hot_comment(hotList, 1)


if __name__ == '__main__':
    questionId = 545286
    save_comment(13,questionId)
    # select_sql = 'select id from question where exam_type = %s and year = %s'
    # select_value = (11, '2009')
    # app_id = 13
    #
    # db = pymysqlUtil.PymysqlDB()
    # questionList = db.select_list(select_sql, select_value)
    #
    # for question in questionList:
    #     questionId = question[0]
    #     print("questionId=", questionId)
    #     save_comment(app_id, questionId)
        # time.sleep(1)
    # questionId = 1638505
    # save_comment(questionId)
