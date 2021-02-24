import pytest

from ApiAutoTest.zonghe.baw import Member
from ApiAutoTest.zonghe.caw import ReadData, MysqlOp


# 前置条件注册的数据
@pytest.fixture(params=ReadData.read_yaml(r'test_data\login_setup.yaml'))
def setup_data(request):
    return request.param


@pytest.fixture(params=ReadData.read_yaml(r'test_data\login_data.yaml'))
def login_data(request):
    return request.param


# login的前置条件
@pytest.fixture()
def register(baserequest, url, setup_data, db_info):
    # 注册用户
    r = Member.register(baserequest, url, setup_data['data'])
    print(r.text)
    yield
    # 删除用户
    MysqlOp.delete_user(setup_data['data']['mobilephone'], db_info)


def test_login(register, baserequest, url, login_data):
    r = Member.login(baserequest, url, login_data['data'])
    assert r.json()['status'] == login_data['except']['status']
    assert r.json()['code'] == login_data['except']['code']
    assert r.json()['msg'] == login_data['except']['msg']

