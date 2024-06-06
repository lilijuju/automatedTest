import unittest
import paramunittest  # 引入paramunittest参数化模块
from parameterized import parameterized


# 需要继承父类unittest.TestCase，且测试类要以大写的Test开头
# 测试用例方法以小写的test开头
# 测试文件（模块）最好以小写的test开头

class TestLogin(unittest.TestCase):
    # 通过@paramunittest.parametrized装饰器传给调用者


    # def setParameters(self, username, password):  # 通过setParameters方法接收装饰器传递过来的参数
    #     self.username = username
    #     self.password = password

    def login(self, username, password):
        if password != '123456' and password != '':
            result = {
                'userName': username,
                'password': password,
                'code': 3,
                'message': '用户名或密码错误!'
            }
        elif password == '':
            result = {
                'userName': username,
                'password': password,
                'code': 2,
                'message': '密码不能为空！'
            }
        else:
            result = {
                'userName': username,
                'password': password,
                'code': 0,
                'message': '登录成功！'
            }
        return result

# @parameterized.expand([
    #     # {'username': 'root', 'password': '123456'},
    #     # {'username': 'root', 'password': '1234567'},
    #     # {'username': 'root', 'password': ''}
    #     ('root', '123456'),
    #     ('root', '1234567'),
    #     ('root', '')
    # ])
    # case1 : 输入正确的用户名和正确的密码进行登录
    @parameterized.expand([
        ('root', '123456')
    ])
    def test_login_success_01(self,username,password):
        print(username)
        # 实际结果 ：程序的输出
        login_result = self.login(username, password)
        # 断言assertEqual(a,b)  a==b
        self.assertEqual(0, login_result.get('code'))
        self.assertEqual('登录成功！', login_result.get('message'))
        print(login_result.get('message'))

    # case2 : 输入正确的用户名和错误的密码进行登录
    # def test_password_is_wrong_02(self,username,password):
    #     login_result = self.login(username, password)
    #     self.assertEqual(3, login_result.get('code'))
    #     self.assertEqual('用户名或密码错误!', login_result.get('message'))
    #     print(login_result.get('message'))
    #
    # # case3 : 输入正确的用户名和空的密码进行登录
    # def test_password_is_null_03(self,username,password):
    #     login_result = self.login(username, password)
    #     self.assertEqual(2, login_result.get('code'))
    #     self.assertEqual('密码不能为空！', login_result.get('message'))
    #     print(login_result.get('message'))
