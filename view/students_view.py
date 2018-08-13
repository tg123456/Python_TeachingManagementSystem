import os
import sys

# 获取项目所在文件目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 将项目添加到sys.path中
sys.path.append(BASE_DIR)

from db import operate_data


# 初始化
def students_init(ret):
    while True:
        str = """      欢迎光临-学生管理系统
查询课程:1 | 查询班级:2 | 查询老师:3 | 退出:0"""
        print(str)
        opreate_code = 'func' + input("请输入对应的操作编号：").strip()
        if opreate_code == 'func0':
            print('\033[1;31;0m欢迎使用！\033[0m')
            return

        if hasattr(sys.modules[__name__], opreate_code):
            func = getattr(sys.modules[__name__], opreate_code)
            func(ret)
        else:
            print('\033[1;31;0m请输入对应的操作编码！\033[0m')
    return True


def func1(ret):
    course_dicts = operate_data.r_course()
    course_list = [course for course in course_dicts.values() if
                   course['school_name'] == ret['school_name'] and course['name'] == ret['course_name']]
    print('---------------------执行结果---------------------')
    if len(course_list):
        for course in course_list:
            str = "课程编号:{} 课程名称:{} 课程成绩:{} 学校名称:{} 课程备注:{}".\
                format(course['id'], course['name'], ret['score'],course['school_name'],course['other'])
            print(str)
    else:
        print('\033[1;31;0m还未给您分配课程,请练习管理员！\033[0m')
    print('--------------------------------------------------')


def func2(ret):
    grade_dicts = operate_data.r_grade()
    grade_list = [grade for grade in grade_dicts.values() if
                  grade['school_name'] == ret['school_name'] and grade['name'] == ret['grade_name']]
    print('---------------------执行结果---------------------')
    if len(grade_list):
        for grade in grade_list:
            str = "班级编号:{} 班级名称:{} 学校名称:{} 课程名称:{} 班级备注{}".\
                format(grade['id'], grade['name'], grade['school_name'],grade['course_name'], grade['other'])
            print(str)
    else:
        print('\033[1;31;0m还未给您分配班级,请练习管理员！\033[0m')
    print('--------------------------------------------------')

def func3(ret):
    teacher_dicts = operate_data.r_teacher()
    teacher_list = [teacher for teacher in teacher_dicts.values() if
                    teacher['school_name'] == ret['school_name'] and teacher['name'] == ret['teacher_name']]
    print('---------------------执行结果---------------------')
    if len(teacher_list):
        for teacher in teacher_list:
            str = "老师编号:{} 老师姓名:{} 学校名称:{} 课程名称:{} 老师备注{}".\
                format(teacher['id'], teacher['name'], teacher['school_name'],teacher['course_name'], teacher['other'])
            print(str)
    else:
        print('\033[1;31;0m还未给您分配老师,请练习管理员！\033[0m')
    print('--------------------------------------------------')
