import os
import sys
import time

# 获取项目所在文件目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 将项目添加到sys.path中
sys.path.append(BASE_DIR)

from module import management
from core import tools
from db import operate_data


def crate_manager():
    """创建管理员"""
    teacher_dicts = operate_data.r_teacher()
    school_dicts = operate_data.r_school()

    while True:
        flag = False

        if len(teacher_dicts):
            id = tools.auto_increment(teacher_dicts.values())
        else:id='1'

        name = input("请输入管理员姓名(退出:Q)：").strip()
        if tools.quit(name): break

        if teacher_dicts.get(name, None):
            name = name + time.strftime("%Y%m%d%H%M%S")
            print("该管理员已经存在，管理员更新为：%s" % (name))

        age = input("请输入老师年龄(退出:Q)：").strip()
        if tools.quit(age): break

        sex = input("请输入管理员性别(退出:Q)：").strip()
        if tools.quit(sex): break

        for school in school_dicts.values():
            print("学校编号:{} 学校名称:{} 学校地址:{}".format(school['id'],school['name'],school['address']))

        while True:
            school_name = input("请输入学校名称(退出:Q)：").strip()
            if tools.quit(school_name):
                flag = True
                break
            if tools.check_info(school_name,school_dicts.keys(),'name'):
                print('\033[1;31;0m请输入正确的学校名称！\033[0m')
            else: break

        if flag:break

        other = input("请输入管理员备注(退出:Q)：").strip()
        if tools.quit(other): break

        password = input("请输入管理员密码(退出:Q)：").strip()
        if tools.quit(password): break

        password = tools.md5(name,password)

        print('---------------------执行结果---------------------')
        management.create_manager(id,name,age,school_name,other,password,sex)
        print("%s 管理员创建成功！" % name)
        print('--------------------------------------------------')

        flag = input('是否继续管理员老师？(Y/N):').strip()

        if flag.upper() == 'Y':
            continue
        else:
            print('\033[1;31;0m欢迎使用！\033[0m')
            break
    return True

if __name__ == "__main__":
    crate_manager()



