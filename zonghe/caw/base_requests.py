"""
1.get、post方法的异常处理
2.打印日志
3.保持会话（使用session发送会话）
"""
import requests


class BaseRequests:
    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        try:
            r = self.session.get(url, **kwargs)
            return r
        except Exception as e:
            print(e)

    def post(self, url, **kwargs):
        try:
            r = self.session.post(url, **kwargs)
            return r
        except Exception as e:
            print(e)


if __name__ == '__main__':
    r = BaseRequests().get("http://192.168.1.64:8089/futureloan/mvc/api/member/list")
    print(r.text)
    r = BaseRequests().post("http://192.168.1.64:8089/futureloan/mvc/api/member/login",
                            data={"mobilephone" : "", "pwd": "123123"})
    print(r.text)
