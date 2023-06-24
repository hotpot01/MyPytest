import time

import pytest

#固件，固件是函数，pytest会在执行测试用例前，或者执行测试用例后使用
#理论上，测试用例也不会接受什么参数了，所以固件就是传参了
#作用域分为：函数级别，类级别，模块级别，会话级别


#最基础的固件使用方式
@pytest.fixture(scope="function")
def postcode():
    return 10

def test_postcode(postcode):
    assert postcode == 10

#预处理和后处理，使用yield来实现断点执行
@pytest.fixture()
def db():
    print('Connection successful')

    yield

    print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    #链接数据库后，里面还写了一个逻辑函数
    assert search_user('001') == 'xiaoming'

#可以对固件进行重命名
@pytest.fixture(scope="function",name="age")
def cal_age():
    return 91
def test_rename(age):
    assert age==90

#固件的自动执行，感觉有点像类的静态方法，不包含类的逻辑
#不需要显示地调用固件
@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))

#因为固件是函数，所以也可以进行参数化,和普通的测试用例形式一样，入参都是固件的函数名
#但是，固件的参数化依赖pytest的内置固件request，并通过request.param返回参数值
#应用上，多环境/db的时候可以使用

@pytest.fixture(params=[
    ('redis', '6379'),
    ('elasticsearch', '9200')
])
def params(request):
    return request.param


@pytest.fixture(autouse=True)
def db(params):
    print('\nSucceed to connect %s:%s' % params)

    yield

    print('\nSucceed to close %s:%s' % params)


def test_api():
    assert 1 == 1

#可以传个fixture，读fixture中的数据，fixture可以时读文件的入口
#1.这里request的写法就是这样的，request是pytest里面特别有用的固件：https://docs.pytest.org/en/stable/reference/reference.html#request
#2.indirect为True的时候，会把argsname解释为函数，把argsvalue解释为函数的执行参数
#3,固件的函数名需要和argsname一致,或者也可以重命名
@pytest.fixture(scope="function")
def x(request):
    print("调用的函数名:",request.function)
    return request.param*3

@pytest.fixture(scope="function")
def y(request):
    return request.param*2

@pytest.mark.parametrize("x,y",[("a","b")],indirect=True)
def test_xy(x,y):
    print(x,y)

#内置固件
#这里重写了tmpdir
@pytest.fixture()
def tmpdir():
    return "hello"
def test_dir(tmpdir):
    a_dir=tmpdir.mkdir("mytempdir")
    print(a_dir)