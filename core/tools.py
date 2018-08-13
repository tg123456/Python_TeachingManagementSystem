import hashlib


def md5(usr,passwd):
    """md5摘要算法"""
    md5_obj = hashlib.md5(usr.encode('utf-8'))
    md5_obj.update(passwd.encode('utf-8'))
    return md5_obj.hexdigest()


def quit(info):
    """统一退出功能"""
    if info.upper() == 'Q':
        print('\033[1;31;0m欢迎使用！\033[0m')
        return True
    else:
        return False


def check_info(info,list_view,key=None):
    """校验信息"""
    for item in list_view:
        if type(item) == 'dict':
            item = dict(item)
            if info == item['name']:
                return False
        else:
            if info == item:
                return False
    return True


def auto_increment(dic_list_view):
    dic_list = sorted(dic_list_view,key=lambda x:x['id'])
    # print("id = ", str(int(dic_list[-1]['id'])+1))
    return str(int(dic_list[-1]['id'])+1)


