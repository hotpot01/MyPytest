import pytest
import pytest_check as check
import allure
@pytest.mark.dev
def test_compute(param):
    assert param < 4


# @pytest.mark.ok
# def test_anyparam(names):
#     assert names>4


#配置固件的测试

@pytest.mark.env
@pytest.mark.option
def test_option1(pytestconfig):
    print("打印环境参数信息")
    print('dev: %s' % pytestconfig.getoption('dev'))
    print('host: %s' % pytestconfig.getoption('host'))
    print('port: %s' % pytestconfig.getoption('port'))

@pytest.mark.env
@pytest.mark.all
def test_all(allUse):
    print("测试意向")
    assert allUse==56

#只会打印错误的信息
@allure.story("可持续发展")
def test_use_pytest_check():
    for i in range(5):
        check.equal(i,3)