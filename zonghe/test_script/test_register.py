"""
测试注册接口的脚本

原则：1.测试环境，在执行脚本前是什么状态，执行完脚本后恢复到之前的状态（清理环境）
     2.脚本依赖的环境要在脚本中自己构造
     脚本的健壮性、稳定性增高
重复注册测试逻辑：
    1.环境准备，下发注册请求，检查结果，报错重复注册
    2.恢复环境，删除数据
"""
import pytest

from ApiAutoTest.zonghe.baw import Member
from ApiAutoTest.zonghe.caw import ReadData, MysqlOp


@pytest.fixture(params=ReadData.read_yaml(r'test_data\register_fail.yaml'))
def fail_data(request):
    return request.param


@pytest.fixture(params=ReadData.read_yaml(r'test_data\register_success.yaml'))
def success_data(request):
    return request.param


def test_register_fail(fail_data, baserequest, url):
    """
    注册失败的脚本
    :return:
    """
    # 1.下发请求
    # 检查结果与预期结果是否一致

    r = Member.register(baserequest, url, fail_data['data'])
    assert r.json()['msg'] == fail_data['except']['msg']


def test_register_success(success_data, baserequest, url, db_info):
    MysqlOp.delete_user(success_data['data']['mobilephone'], db_info)
    r = Member.register(baserequest, url, success_data['data'])
    assert r.json()['msg'] == success_data['except']['msg']
    r = Member.get_list(baserequest, url)
    assert success_data['data']['mobilephone'] in r.text
    MysqlOp.delete_user(success_data['data']['mobilephone'], db_info)
