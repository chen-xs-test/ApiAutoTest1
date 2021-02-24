"""
操作Mysql数据库
"""
import mysql.connector


def connect(db_info):
    host = db_info['host']
    port = db_info['port']
    user = db_info['user']
    passwd = db_info['pwd']
    database = db_info['name']
    try:
        mydb = mysql.connector.connect(host=host, user=user, passwd=passwd,
                                       database=database, port=port, charset='utf-8')
        print("连接成功")
        return mydb
    except Exception as e:
        print(e)


def disconnect(mydb):
    """
    断开连接
    :param mydb:
    :return:
    """
    try:
        mydb.close()
    except Exception as e:
        print("断开数据库连接失败", e)


def execute(mydb, sql):
    try:
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()  # 提交
        cursor.close()  # 关闭游标
        # return myresult
    except Exception as e:
        print("执行sql语句失败", e)


def delete_user(mobilephone, db_info):
    """
    根据手机号删除用户
    :param mobilephone:
    :param db_info:
    :return:
    """
    mydb = connect(db_info)
    execute(mydb, "DELETE FROM member WHERE mobilephone=%s;"%mobilephone)

    disconnect(mydb)


if __name__ == '__main__':
    db_info = {"host": "192.168.1.64", "port": 3306, "user": "root", "pwd": "123456", "name": "apple"}
    mydb = connect(db_info)
    execute(mydb, "DELETE FROM member WHERE mobilephone=18020022430;")
    # print(execute(mydb, "SELECT * FROM member;"))
    disconnect(mydb)
