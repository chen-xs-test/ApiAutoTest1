"""
测试登陆接口的脚本
?mobilephone=18080878899&pwd=12345678
"""
import pytest

from ApiAutoTest.zonghe.baw import Member
from ApiAutoTest.zonghe.caw import ReadData


@pytest.fixture(params=ReadData.read_yaml(r"test_data\login_fail.yaml"))
def fail_data(request):
    return request.param


@pytest.fixture(params=ReadData.read_yaml(r"test_data\login_success.yaml"))
def success_data(request):
    return request.param

# class login:
def test_login_fail(fail_data, url, baserequest):
    r = Member.login(baserequest, url, fail_data['data'])
    assert r.json()['status'] == fail_data['except']['status']
    assert r.json()['msg'] == fail_data['except']['msg']
    assert r.json()['code'] == fail_data['except']['code']


def test_login_success(success_data, url, baserequest):
    r = Member.login(baserequest, url, success_data['data'])
    assert r.json()['status'] == success_data['except']['status']
    assert r.json()['msg'] == success_data['except']['msg']
    assert r.json()['code'] == success_data['except']['code']