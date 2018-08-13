import time
import hashlib
import os
import pickle

from db import operate_data

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db')


def md5(usr, passwd):
    md5_obj = hashlib.md5(usr.encode('utf-8'))
    md5_obj.update(passwd.encode('utf-8'))
    return md5_obj.hexdigest()


# 读取文件
def read_file_content():
    person_dicts = operate_data.r_teacher()
    student_dicts = operate_data.r_student()
    person_dicts.update(student_dicts)
    manager_dicts = operate_data.r_manager()
    person_dicts.update(manager_dicts)
    return person_dicts


# 三次登录验证
def login():
    count = 0
    while True:
        person_dicts = read_file_content()
        name = input("请输入用户名(退出：Q)：").strip()
        if name.upper() == 'Q':
            ret = {'state': False}
            ret['info'] = "退出登录！"
            return ret
        passwd = input("请输入密码：")
        passwd = md5(name, passwd)
        if person_dicts.get(name, None):
            person = person_dicts[name]
            if person['password'] == passwd:
                print('\033[1;31;0m恭喜您，登录成功！\033[0m')
                ret = person
                ret['login_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                ret['state'] = True
                return ret
            else:
                if count == 2:
                    print('\033[1;31;0m登录失败！\033[0m')
                    ret = {'name': name}
                    ret['login_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                    ret['state'] = False
                    ret['info'] = "登录失败！"
                    return ret
                print('\033[1;31;0m用户名或密码错误，您还有%s机会！\033[0m' % (2 - count))
        else:
            if count == 2:
                ret = {'name': name}
                ret['login_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                ret['state'] = False
                ret['info'] = "登录失败！"
                print('\033[1;31;0m登录失败！\033[0m')
                return ret
            print('\033[1;31;0m用户名或密码错误，您还有%s机会！\033[0m' % (2 - count))
        count += 1
