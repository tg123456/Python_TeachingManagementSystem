import os
import sys

# 获取项目所在文件目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 将项目添加到sys.path中
sys.path.append(BASE_DIR)

from core import modes, tools
from db import operate_data


def create_school(id, name, address, other):
    """
    创建学校
    :param id:
    :param name:
    :param address:
    :param other:
    :return:
    """
    school_dicts = operate_data.r_school()
    school = modes.School(id, name, address, other)
    school_dict = {'id': school.id, 'name': school.name, 'address': school.address, 'other': school.other}
    school_dicts[name] = school_dict
    operate_data.w_school(school_dicts)
    return True


def create_course(id, name, school_name, cycle, price, other):
    """
    创建课程
    :param id:
    :param name:
    :param school_name:
    :param cycle:
    :param price:
    :param other:
    :return:
    """
    course_dicts = operate_data.r_course()
    course = modes.Course(id, name, school_name, cycle, price, other)
    course_dict = {'id': course.id, 'name': course.name, 'school_name': course.school_name, 'cycle': course.cycle,
                   'price': course.price, 'other': course.other}
    course_dicts[name] = course_dict
    operate_data.w_course(course_dicts)
    return True


def create_grade(id, name, school_name, course_name, other):
    """
    创建班级
    :param id:
    :param name:
    :param school_name:
    :param course_name:
    :param other:
    :return:
    """
    grade_dicts = operate_data.r_grade()
    grade = modes.Grade(id, name, school_name, course_name, other)
    grade_dict = {'id': grade.id, 'name': grade.name, 'school_name': grade.school_name,
                  'course_name': grade.course_name, 'other': grade.other}
    grade_dicts[name] = grade_dict
    operate_data.w_grade(grade_dicts)
    return True


def create_teacher(id, name, age, school_name, course_name, other, password, sex):
    """
    创建老师
    :param id:
    :param name:
    :param age:
    :param school_name:
    :param course_name:
    :param other:
    :param password:
    :param sex:
    :return:
    """
    teacher_dicts = operate_data.r_teacher()
    teacher = modes.Teacher(id, name, age, school_name, course_name, other, password, sex)
    teacher_dict = {'id': teacher.id, 'name': teacher.name, 'age': teacher.age, 'sex': teacher.sex,
                    'role': teacher.role, 'school_name': teacher.school_name, 'course_name': teacher.course_name,
                    'other': teacher.other, "password": teacher.password}
    teacher_dicts[name] = teacher_dict
    operate_data.w_teacher(teacher_dicts)
    return True


def create_manager(id, name, age, school_name, other, password, sex):
    """
    创建管理员
    :param id:
    :param name:
    :param age:
    :param school_name:
    :param other:
    :param password:
    :param sex:
    :return:
    """
    manager_dicts = operate_data.r_manager()
    manager = modes.Manager(id, name, age, school_name, other, password, sex)
    manager_dict = {'id': manager.id, 'name': manager.name, 'age': manager.age, 'sex': manager.sex,
                    'role': manager.role, 'school_name': manager.school_name, 'other': manager.other,
                    "password": manager.password}
    manager_dicts[name] = manager_dict
    operate_data.w_manager(manager_dicts)
    return True


def create_student(id, name, age, school_name, course_name, teacher_name, grade_name, other, password, score, sex):
    """
    创建学生
    :param id:
    :param name:
    :param age:
    :param school_name:
    :param course_name:
    :param teacher_name:
    :param grade_name:
    :param other:
    :param password:
    :param score:
    :param sex:
    :return:
    """
    student_dicts = operate_data.r_student()
    student = modes.Student(id, name, age, school_name, course_name, teacher_name, grade_name, other, password, score,
                            sex)
    student_dict = {"id": student.id, "name": student.name, "age": student.age, "sex": student.sex,
                    "school_name": student.school_name, "role": "student",
                    "course_name": student.course_name, "teacher_name": student.teacher_name,
                    "grade_name": student.grade_name, "score": student.score,
                    "other": student.other, "password": student.password}

    student_dicts[name] = student_dict
    operate_data.w_student(student_dicts)
    return True


def update_student(student_dicts):
    """
    批量修改学生信息
    :param student_dicts:
    :return:
    """
    for k, student in student_dicts.items():
        student_dict = {"id": student['id'], "name": student['name'], "age": student['age'], "sex": student['sex'],
                        "school_name": student['school_name'], "role": "student",
                        "course_name": student['course_name'], "teacher_name": student['teacher_name'],
                        "grade_name": student['grade_name'], "score": student['score'],
                        "other": student['other'], "password": student['password']}
        student_dicts[k] = student_dict
    operate_data.w_student(student_dicts)
    return True
