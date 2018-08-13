import logging
from core.login import login
from core import dispatch
from conf import my_log_settings


def main():  # 程序的梗概逻辑

    while True:
        print('欢迎您使用校园管理系统')
        ret = login()
        my_log_settings.load_my_logging_cfg(ret)
        if ret['state'] == False:
            flag = input("是否继续(结束：E)：").strip()
            if flag.upper() == 'E':
                print('\033[1;31;0m系统关闭,欢迎使用！\033[0m')
                return False
        if ret['state']:
            if hasattr(dispatch.Management(),ret['role']):
                func = getattr(dispatch.Management(),ret['role'])
                func(ret)
    return True

