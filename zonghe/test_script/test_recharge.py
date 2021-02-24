import pytest

from ApiAutoTest.zonghe.baw import Member
from ApiAutoTest.zonghe.caw import ReadData, Check


@pytest.fixture(params=ReadData.read_yaml(r"test_data\recharge_data.yaml"))
def recharge_data(request):
    return request.param


def test_recharge(baserequest, url, recharge_data):
    Member.login()
    r = Member.recharge(baserequest, url, recharge_data['data'])
    Check.equal(r.json(), recharge_data['except'], 'status,code,msg')