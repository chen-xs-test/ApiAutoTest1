import pytest

from ApiAutoTest.zonghe.baw import Member
from ApiAutoTest.zonghe.caw import ReadData, MysqlOp, Check


@pytest.fixture(params=ReadData.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param


def test_login(baserequest, url, login_data, db_info):
    MysqlOp.delete_user(login_data['regdata']['mobilephone'], db_info)
    Member.register(baserequest, url, login_data['regdata'])
    r = Member.login(baserequest, url, login_data['data'])
    Check.equal(r.json(), login_data['except'], 'code,msg,status')
    MysqlOp.delete_user(login_data['regdata']['mobilephone'], db_info)