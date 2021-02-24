"""
金融项目用户管理模块的接口
member  模块名
list    接口名
http://192.168.1.64/futureloan/mvc/api/member/list
"""
import json

from ApiAutoTest.zonghe.caw.base_requests import BaseRequests


def register(baserquests, url, data):
    """
    注册接口
    :param baserquests: BaseRequests的实例（用于发送get或post请求）
    :param url: 环境url
    :param data: 注册数据
    :return: 响应
    """
    url = url + 'futureloan/mvc/api/member/register'
    r = baserquests.post(url, data=data)
    return r


def get_list(baserquest, url):
    url = url + 'futureloan/mvc/api/member/list'
    return baserquest.get(url)


def login(baserequest, url, data):
    """
    登陆接口
    :param baserequest: BaseRequests的实例（用于发送get或post请求）
    :param url: 环境url（登陆使用的接口）
    :param data: 登录数据
    :return: 响应
    """
    url = url + 'futureloan/mvc/api/member/login'
    return baserequest.post(url, data=data)


def recharge(baserequest, url, data):
    """
    充值接口
    :param baserequest: BaseRequests的实例（用于发送get或post请求）
    :param url: 环境url（登陆使用的接口）
    :param data: 充值数据
    :return: 响应
    """
    url = url + 'futureloan/mvc/api/member/recharge'
    return baserequest.post(url, data=data)


if __name__ == '__main__':
    r = get_list(BaseRequests(), 'http://192.168.1.64:8089/').text
    a = json.loads(r)['data']
    l = [i['mobilephone'] for i in a]
    print(l)
