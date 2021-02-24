import pytest_check as check


def equal(real, expect, keys):
    """
    assert r.json()['status'] == login_data['except']['status']
    assert r.json()['code'] == login_data['except']['code']
    assert r.json()['msg'] == login_data['except']['msg']

    不推荐直接比较 r.json() == data['expect']
        1.结果中有一些不关键的信息，后续变化时，会导致脚本不通过
        2.结果中有时间戳之类的变化的信息，每次校验结果不同，需要变更数据
        3.结果可能很长，顺序发生变化，不方便维护
    :param real: 实际结果
    :param expect: 预期结果
    :param keys: 校验字段
    :return:
    """

    ks = keys.split(',')
    for k in ks:
        try:
            check.equal(str(real[k]), str(expect[k]))
        except Exception as e:
            print(e)
