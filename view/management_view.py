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


# 初始化
def course_init(ret):
    while True:
        str = """                    欢迎光临-管理员系统
创建学校:1 | 创建课程:2 | 创建班级:3 | 创建老师:4 | 创建学生:5
查询学校:6 | 查询课程:7 | 查询班级:8 | 查询老师:9 | 查询学生:10 | 退出:0"""
        print(str)

        opreate_code = 'func' + input("请输入对应的操作编号：").strip()
        if opreate_code == 'func0':
            print('\033[1;31;0m欢迎使用！\033[0m')
            break

        if hasattr(sys.modules[__name__], opreate_code):
            func = getattr(sys.modules[__name__], opreate_code)
            func()
        else:
            print('\033[1;31;0m请输入对应的操作编码！\033[0m')

    return True


# 创建学校
def func1():

    while True:
        school_dicts = operate_data.r_school()

        if len(school_dicts):
            id = tools.auto_increment(school_dicts.values())
        else:
            id = '1'

        name = input("请输入学校名称(退出:Q)：").strip()
        if tools.quit(name): break

        address = input("请输入学校地址(退出:Q)：").strip()
        if tools.quit(address): break

        if school_dicts.get(name, None):
            name = name + time.strftime("%Y%m%d%H%M%S")
            print("该学校名称已经存在，学校名称更新为：%s" % (name))

        other = input("请输入学校备注(退出:Q)：").strip()
        if tools.quit(other): break

        print('---------------------执行结果---------------------')
        management.create_school(id, name, address, other)
        print("%s 学校创建成功！" % name)
        print('--------------------------------------------------')

        flag = input('是否继续创建学校？(Y/N):').strip()

        if flag.upper() == 'Y':
            continue
        else:
            break
    return True


# 创建课程
def func2():
    school_dicts = operate_data.r_school()

    if len(school_dicts) <= 0:
        print("\033[1;31;0m还未创建学校，请先创建学校，谢谢！\033[0m")
        return

    while True:
        flag = False
        course_dicts = operate_data.r_course()

        if len(course_dicts):
            id = tools.auto_increment(course_dicts.values())
        else:
            id = '1'

        name = input("请输入课程名称(退出:Q)：").strip()
        if tools.quit(name): break

        if course_dicts.get(name, None):
            name = name + time.strftime("%Y%m%d%H%M%S")
            print("该课程名称已经存在，课程名称更新为：%s" % (name))

        for school in school_dicts.values():
            print("学校编号:{} 学校名称:{} 学校地址:{}".format(school['id'], school['name'], school['address']))

        while True:
            school_name = input("请输入学校名称(退出:Q)：").strip()
            if tools.quit(school_name):
                flag = True
                break
            if tools.check_info(school_name, school_dicts.keys(), 'name'):
                print('\033[1;31;0m请输入正确的学校名称！\033[0m')
            else:
                break

        if flag: break

        cycle = input("请输入课程周期(退出:Q)：").strip()
        if tools.quit(cycle): break

        price = input("请输入课程价格(退出:Q)：").strip()
        if tools.quit(price): break

        other = input("请输入课程备注(退出:Q)：").strip()
        if tools.quit(other): break

        print('---------------------执行结果---------------------')
        management.create_course(id, name, school_name, cycle, price, other)
        print("%s 课程创建成功！" % name)
        print('--------------------------------------------------')

        flag = input('是否继续创建课程？(Y/N):').strip()

        if flag.upper() == 'Y':
            continue
        else:
            break
    return True


# 创建班级
def func3():
    school_dicts = operate_data.r_school()
    course_dicts = operate_data.r_course()

    if len(school_dicts) <= 0:
        print("\033[1;31;0m还未创建学校，请先创建学校，谢谢！\033[0m")
        return
    if len(course_dicts) <= 0:
        print("\033[1;31;0m还未创建课程，请先创建课程，谢谢！\033[0m")
        return

    while True:
        flag = False
        grade_dicts = operate_data.r_grade()

        if len(grade_dicts):
            id = tools.auto_increment(grade_dicts.values())
        else:
            id = '1'

        name = input("请输入班级名称(退出:Q)：").strip()
        if tools.quit(name): break

        if grade_dicts.get(name, None):
            name = name + time.strftime("%Y%m%d%H%M%S")
            print("该班级名称已经存在，班级名称更新为：%s" % (name))

        for school in school_dicts.values():
            print("学校编号:{} 学校名称:{} 学校地址:{}".format(school['id'], school['name'], school['address']))

        while True:
            school_name = input("请输入学校名称(退出:Q)：").strip()
            if tools.quit(school_name):
                flag = True
                break
            if tools.check_info(school_name, school_dicts.keys(), 'name'):
                print('\033[1;31;0m请输入正确的学校名称！\033[0m')
            else:
                break

        if flag: break
        flag = False

        course_list = [k for k, course in course_dicts.items() if course['school_name'] == school_name]
        if len(course_list):
            for course in course_list:
                print("课程名称:{}".format(course))
        else:
            print('\033[1;31;0m该学校没有创建相应的课程，请先创建课程！\033[0m')

        while True:
            course_name = input("请输入课程名称(退出:Q)：").strip()
            if tools.quit(course_name):
                flag = True
                break
            if tools.check_info(course_name, course_list, 'name'):
                print('\033[1;31;0m请输入正确的课程名称！\033[0m')
            else:
                break

        if flag: break

        other = input("请输入班级备注(退出:Q)：").strip()
        if tools.quit(other): break

        print('---------------------执行结果---------------------')
        management.create_grade(id, name, school_name, course_name, other)
        print("%s 班级创建成功！" % name)
        print('--------------------------------------------------')

        flag = input('是否继续创建班级？(Y/N):').strip()

        if flag.upper() == 'Y':
            continue
        else:
            break
    return True


# func3()
# 创建老师
def func4():
    school_dicts = operate_data.r_school()
    course_dicts = operate_data.r_course()

    if len(school_dicts) <= 0:
        print("\033[1;31;0m还未创建学校，请先创建学校，谢谢！\033[0m")
        return
    if len(course_dicts) <= 0:
        print("\033[1;31;0m还未创建课程，请先创建课程，谢谢！\033[0m")
        return

    while True:
        flag = False
        teacher_dicts = operate_data.r_teacher()

        if len(teacher_dicts):
            id = tools.auto_increment(teacher_dicts.values())
        else:
            id = '1'

        name = input("请输入老师姓名(退出:Q)：").strip()
        if tools.quit(name): break

        if teacher_dicts.get(name, None):
            name = name + time.strftime("%Y%m%d%H%M%S")
            print("该老师已经存在，老师姓名更新为：%s" % (name))

        age = input("请输入老师年龄(退出:Q)：").strip()
        if tools.quit(age): break

        sex = input("请输入老师性别(退出:Q)：").strip()
        if tools.quit(sex): break

        for school in school_dicts.values():
            print("学校编号:{} 学校名称:{} 学校地址:{}".format(school['id'], school['name'], school['address']))

        while True:
            school_name = input("请输入学校名称(退出:Q)：").strip()
            if tools.quit(school_name):
                flag = True
                break
            if tools.check_info(school_name, school_dicts.keys(), 'name'):
                print('\033[1;31;0m请输入正确的学校名称！\033[0m')
            else:
                break

        if flag: break
        flag = False

        course_list = [k for k, course in course_dicts.items() if course['school_name'] == school_name]
        if len(course_list):
            for course in course_list:
                print("课程名称:{}".format(course))
        else:
            print('\033[1;31;0m该学校没有创建相应的课程，请先创建课程！\033[0m')

        while True:
            course_name = input("请输入课程名称(退出:Q)：").strip()
            if tools.quit(course_name):
                flag = True
                break
            if tools.check_info(course_name, course_list, 'name'):
                print('\033[1;31;0m请输入正确的课程名称！\033[0m')
            else:
                break

        if flag: break

        other = input("请输入老师备注(退出:Q)：").strip()
        if tools.quit(other): break

        password = input("请输入老师密码(退出:Q)：").strip()
        if tools.quit(password): break

        password = tools.md5(name, password)

        print('---------------------执行结果---------------------')
        management.create_teacher(id, name, age, school_name, course_name, other, password, sex)
        print("%s 老师创建成功！" % name)
        print('--------------------------------------------------')

        flag = input('是否继续创建老师？(Y/N):').strip()

        if flag.upper() == 'Y':
            continue
        else:
            break
    return True


# 创建学生
def func5():
    grade_dicts = operate_data.r_grade()
    school_dicts = operate_data.r_school()
    course_dicts = operate_data.r_course()
    teacher_dicts = operate_data.r_teacher()

    if len(school_dicts) <= 0:
        print("\033[1;31;0m还未创建学校，请先创建学校，谢谢！\033[0m")
        return
    if len(course_dicts) <= 0:
        print("\033[1;31;0m还未创建课程，请先创建课程，谢谢！\033[0m")
        return
    if len(teacher_dicts) <= 0:
        print("\033[1;31;0m还未创建老师，请先创建老师，谢谢！\033[0m")
        return

    while True:
        flag = False

        student_dicts = operate_data.r_student()

        if len(student_dicts):
            id = tools.auto_increment(student_dicts.values())
        else:
            id = '1'

        name = input("请输入学生姓名(退出:Q)：").strip()
        if tools.quit(name): break

        if student_dicts.get(name, None):
            name = name + time.strftime("%Y%m%d%H%M%S")
            print("该学生已经存在，学生姓名更新为：%s" % (name))

        age = input("请输入学生年龄(退出:Q)：").strip()
        if tools.quit(age): break

        sex = input("请输入学生性别(退出:Q)：").strip()
        if tools.quit(sex): break

        for school in school_dicts.values():
            print("学校编号:{} 学校名称:{} 学校地址:{}".format(school['id'], school['name'], school['address']))

        while True:
            school_name = input("请输入学校名称(退出:Q)：").strip()
            if tools.quit(school_name):
                flag = True
                break
            if tools.check_info(school_name, school_dicts.keys(), 'name'):
                print('\033[1;31;0m请输入正确的学校名称！\033[0m')
            else:
                break

        if flag: break
        flag = False

        course_list = [k for k, course in course_dicts.items() if course['school_name'] == school_name]
        if len(course_list):
            for course in course_list:
                print("课程名称:{}".format(course))
        else:
            print('\033[1;31;0m该学校没有创建相应的课程，请先创建课程！\033[0m')

        while True:
            course_name = input("请输入课程名称(退出:Q)：").strip()
            if tools.quit(course_name):
                flag = True
                break
            if tools.check_info(course_name, course_list, 'name'):
                print('\033[1;31;0m请输入正确的课程名称！\033[0m')
            else:
                break

        if flag: break
        flag = False

        grade_list = [k for k, grade in grade_dicts.items() if
                      grade['school_name'] == school_name and grade['course_name'] == course_name]
        if len(grade_list):
            for grade in grade_list:
                print("班级名称:{}".format(grade))
        else:
            print('\033[1;31;0m该课程没有创建相应的班级，请先创建班级！\033[0m')
            break

        while True:
            grade_name = input("请输入班级名称(退出:Q)：").strip()
            if tools.quit(grade_name):
                flag = True
                break
            if tools.check_info(grade_name, grade_list, 'name'):
                print('\033[1;31;0m请输入正确的班级名称！\033[0m')
            else:
                break

        if flag: break
        flag = False

        teacher_list = [k for k, teacher in teacher_dicts.items() if
                        teacher['school_name'] == school_name and teacher['course_name'] == course_name]
        if len(teacher_list):
            for teacher in teacher_list:
                print("老师名称:{}".format(teacher))
        else:
            print('\033[1;31;0m该课程没有创建相应的老师，请先创建老师！\033[0m')
            break

        while True:
            teacher_name = input("请输入老师姓名：").strip()
            if tools.quit(teacher_name):
                flag = True
                break
            if tools.check_info(teacher_name, teacher_list, 'name'):
                print('\033[1;31;0m请输入正确的老师姓名！\033[0m')
            else:
                break

        if flag: break

        score = input("请输入学生成绩(默认为0,退出:Q)：").strip()
        if tools.quit(score): break
        other = input("请输入学生备注(退出:Q)：").strip()
        if tools.quit(other): break
        password = input("请输入学生密码(退出:Q)：")
        if tools.quit(password): break
        password = tools.md5(name, password)

        print('---------------------执行结果---------------------')
        management.create_student(id, name, age, school_name, course_name, teacher_name, grade_name, other, password,
                                score, sex)
        print("%s 学生创建成功！" % name)
        print('--------------------------------------------------')

        flag = input('是否继续创建学生？(Y/N):').strip()
        if flag.upper() == 'Y':
            continue
        else:
            break
    return True


def func6():
    school_dicts = operate_data.r_school()
    print('---------------------执行结果---------------------')
    if len(school_dicts):
        for school in school_dicts.values():
            str = "学校编号:{} 学校名称:{} 学校地址:{} 学校备注:{}".format(school['id'], school['name'], school['address'],
                                                           school['other'])
            print(str)
    print('--------------------------------------------------')


def func7():
    course_dicts = operate_data.r_course()
    print('---------------------执行结果---------------------')
    if len(course_dicts):
        for course in course_dicts.values():
            str = "课程编号:{} 课程名称:{} 学校名称:{} 课程备注:{}".format(course['id'], course['name'], course['school_name'],
                                                           course['other'])
            print(str)
    print('--------------------------------------------------')


def func8():
    grade_dicts = operate_data.r_grade()
    print('---------------------执行结果---------------------')
    if len(grade_dicts):
        for grade in grade_dicts.values():
            str = "班级编号:{} 班级名称:{} 学校名称:{} 课程名称:{} 班级备注{}".format(grade['id'], grade['name'], grade['school_name'],
                                                                  grade['course_name'], grade['other'])
            print(str)
    print('--------------------------------------------------')


def func9():
    teacher_dicts = operate_data.r_teacher()
    print('---------------------执行结果---------------------')
    if len(teacher_dicts):
        for teacher in teacher_dicts.values():
            str = "老师编号:{} 老师姓名:{} 老师年龄:{} 老师性别:{} 老师级别:{} 学校名称:{} 课程名称:{} 老师备注:{}" \
                .format(teacher['id'], teacher['name'], teacher['age'], teacher['sex'], teacher['role'],
                        teacher['school_name'], teacher['course_name'], teacher['other'])
            print(str)
    print('--------------------------------------------------')


def func10():
    student_dicts = operate_data.r_student()
    print('---------------------执行结果---------------------')
    if len(student_dicts):
        for student in student_dicts.values():
            str = "学生编号:{} 学生姓名:{} 学生年龄:{} 学生性别:{} 学生成绩:{} 学生级别:{} 学校名称:{} 课程名称:{} 班级名称:{} 老师名称:{} 学生备注:{}" \
                .format(student['id'], student['name'], student['age'], student['sex'], student['score'],
                        student['role'], student['school_name'], student['course_name'], student['grade_name'],
                        student['teacher_name'], student['other'])
            print(str)
    print('--------------------------------------------------')


