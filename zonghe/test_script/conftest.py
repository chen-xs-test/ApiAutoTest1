"""
脚本层公共前置、后置，整个执行过程执行一次
不用import，通过conftest文件名查找

"""
import pytest

from ApiAutoTest.zonghe.caw import ReadData, base_requests


@pytest.fixture(scope='session')
def url():
    return ReadData.read_ini(r'test_env\env.ini', 'url')


@pytest.fixture(scope='session')
def baserequest():
    return base_requests.BaseRequests()


@pytest.fixture(scope='session')
def db_info():
    # ini读取后是字符串格式，但是db_info使用字典格式，使用eval解析为原本的格式
    return eval(ReadData.read_ini(r"test_env\env.ini", 'db_info'))
