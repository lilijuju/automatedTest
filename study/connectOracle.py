# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="/Users/juxin/Downloads/instantclient_19_8")

if __name__ == '__main__':
    conn = cx_Oracle.connect('party', 'party', '20.26.109.144:1521/zjres')
    # party/party@20.26.109.144:1521/zjres
    cursor = conn.cursor()
    print('连接数据库成功！')
    sql = "select * from party.CMX_GROUP_ACCOUNT a where a.state = 'U' and a.Acct_Id = '7901166027'"
    all = cursor.execute(sql)
    for row in all:
        print(row)
    cursor.close()
    conn.close()
