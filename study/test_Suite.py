from XTestRunner import HTMLTestRunner

from test_unitTest import TestLogin
import unittest

# 创建测试套件
suite = unittest.TestSuite()
# 逐个添加测试用例suite.addTest(ClassName(“MethodName”))(ClassName：类名，MethodName：方法名)
suite.addTest(TestLogin('test_login_success_01'))
# suite.addTest(TestLogin('test_password_is_wrong_02'))
# suite.addTest(TestLogin('test_password_is_null_03'))
# 批量添加测试用例（将该类以test开头的方法全部加入套件）：suite.addTest(unittest.makeSuite(ClassName))
# (搜索指定ClassName内 test 开头的方法，并添加到测试套件中)
# suite.addTest(unittest.makeSuite(TestLogin))
runner = unittest.TextTestRunner()

# fp = open('my_report.html', 'wb')
# runner = HTMLTestRunner(
#     stream=fp,
#     title='随便测试的',
#     description='',
# )

# 使用外部样式表。
# 运行测试
runner.run(suite)
