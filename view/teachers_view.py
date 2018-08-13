import os
import sys

# 获取项目所在文件目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 将项目添加到sys.path中
sys.path.append(BASE_DIR)

from module import management
from db import operate_data


def teachers_init(ret):
    """初始化"""
    while True:
        str = """                    欢迎光临-教师管理系统
查询课程:1 | 查询班级:2 | 查询学员:3 | 管理学员成绩:4 | 退出:0"""
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
            str = "课程编号:{} 课程名称:{} 学校名称:{} 课程备注:{}".\
                format(course['id'], course['name'], course['school_name'],course['other'])
            print(str)
    print('--------------------------------------------------')


def func2(ret):
    grade_dicts = operate_data.r_grade()
    grade_list = [grade for grade in grade_dicts.values() if
                  grade['school_name'] == ret['school_name'] and grade['course_name'] == ret['course_name']]

    print('---------------------执行结果---------------------')
    if len(grade_list):
        for grade in grade_list:
            str = "班级编号:{} 班级名称:{} 学校名称:{} 课程名称:{} 班级备注{}".\
                format(grade['id'], grade['name'], grade['school_name'],grade['course_name'], grade['other'])
            print(str)
    else:
        print('\033[1;31;0m还未给您分配课程，请联系管理员！\033[0m')
    print('--------------------------------------------------')


def func3(ret):
    student_dicts = operate_data.r_student()
    student_list = [student for student in student_dicts.values() if
                  student['school_name'] == ret['school_name'] and student['teacher_name'] == ret['name']]

    print('---------------------执行结果---------------------')
    if len(student_list):
        for student in student_list:
            str = "学生编号:{} 学生姓名:{} 学生年龄:{} 学生性别:{} 学生级别:{} 学校名称:{} 课程名称:{} 学生成绩:{} 学生备注:{}" \
                    .format(student['id'], student['name'], student['age'], student['sex'], student['role'],
                            student['school_name'], student['course_name'], student['score'], student['other'])
            print(str)
    else:
        print('\033[1;31;0m还未给您分配学生，请联系管理员！\033[0m')
    print('--------------------------------------------------')


def func4(ret):
    student_dicts = operate_data.r_student()

    student_list = [student for student in student_dicts.values() if
                    student['school_name'] == ret['school_name'] and student['teacher_name'] == ret['name']]

    if len(student_list):
        while True:
            for student in student_list:
                str = "学生编号:{} 学生姓名:{} 学校名称:{} 课程名称:{} 学生成绩:{} 学生备注:{}" \
                    .format(student['id'], student['name'], student['school_name'], student['course_name'],
                        student['score'], student['other'])
                print(str)

            student_name = input("请输入学生的姓名(退出Q)：").strip()

            if student_name.upper() == 'Q':
                break

            if student_name in student_dicts.keys():
                student = student_dicts[student_name]
                str = "学生编号:{} 学生姓名:{} 学校名称:{} 课程名称:{} 学生成绩:{} 学生备注:{}" \
                    .format(student['id'], student['name'], student['school_name'], student['course_name'],
                            student['score'],student['other'])
                score = input("请输入学生成绩(不修改:N)：").strip()
                print("修改前：", str)

                if score.upper() == 'N':
                    continue
                elif score.isdigit():
                    student_dicts[student_name]['score'] = score

                str = "学生编号:{} 学生姓名:{} 学校名称:{} 课程名称:{} 学生成绩:{} 学生备注:{}" \
                    .format(student['id'], student['name'], student['school_name'], student['course_name'],
                            student['score'],student['other'])
                print("修改后：", str)

                management.update_student(student_dicts)
                print('---------------------执行结果---------------------')
                print('\033[1;31;0m %s 学生修改成功！\033[0m' % student_name)
                print('--------------------------------------------------')
            else:
                print('\033[1;31;0m请输入正确的学生姓名！\033[0m')
    else:
        print('---------------------执行结果---------------------')
        print('\033[1;31;0m当前还未给您分配学生，请联系管理员！\033[0m')
        print('--------------------------------------------------')

    return True
