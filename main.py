# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import cx_Oracle

from study.test_selenium import Selenium

cx_Oracle.init_oracle_client(lib_dir="/Users/juxin/Downloads/instantclient_19_8")


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# connection = cx_Oracle.connect(user="party", password="party",
#                                dsn="20.26.109.144:1521/zjres")
# cursor = connection.cursor()
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
   Selenium
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
