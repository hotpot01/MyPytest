import pytest


#没有UI的tesla
#pytest的钩子函数，对基础的测试方法做了封装？但是调用方式还是遵守基础方法，比如metafunc的参数化，也是argskey,argsvalue
def pytest_addoption(parser):
    parser.addoption("--dev", action="store_true", help="run in dev env,otherwise run in test env")
    parser.addoption("--host",action="store_false",help="host of db")
    parser.addoption("--port", action="store", default=8888,help="port of db")
#传入的函数元数据信息
# conftest.py
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    """Generate (multiple) parametrized calls to a test function."""
    #把能获取到的元数据都打印出来,\
    #这里有个问题，固件进行参数化，不是用匹配的方式，而是用统一执行的方式
    #而且这个配置文件会最先被加载
    #这里的参数不能比实际用例用到的参数多
    # 获取到模块名、函数名
    if  "param"  in metafunc.fixturenames:
        if metafunc.config.getoption("dev"):
            name = [1, 2, 3]
        else:
            name = [3, 4, 5]
        # metafunc.parametrize("names", name)
        metafunc.parametrize("param", name)
    print("函数的元信息在这里")
    print(metafunc.definition,metafunc.cls,metafunc.fixturenames)
    # cur_module = f"{str(metafunc.cls).split('.')[-2]}.yml"
    # cur_func = str(metafunc.definition).split(' ')[1][:-1]

@pytest.fixture(name="allUse")
def use_for_all(*args):
    print("所有的项目都可以调用")
    return 7*8