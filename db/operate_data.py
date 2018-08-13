#序列化操作
import pickle
import os

from conf import settings

def r_school():
    path = settings.SCHOOL_PATH
    school_dicts = {}
    if os.path.getsize(path):
        f = open(path, 'rb')
        school_dicts = pickle.load(f)
        f.close()
    return school_dicts

def w_school(school):
    path = settings.SCHOOL_PATH
    f = open(path, 'wb')
    data = pickle.dump(school,f)
    f.close()
    return data


def r_grade():
    path = settings.GRADE_PATH
    grade_dicts = {}
    if os.path.getsize(path):
        f = open(path, 'rb')
        grade_dicts = pickle.load(f)
        f.close()
    return grade_dicts


def w_grade(grade):
    path = settings.GRADE_PATH
    f = open(path, 'wb')
    data = pickle.dump(grade, f)
    f.close()
    return data


def r_course():
    path = settings.COURSE_PATH
    course_dicts = {}
    if os.path.getsize(path):
        f = open(path, 'rb')
        course_dicts = pickle.load(f)
        f.close()
    return course_dicts


def w_course(course):
    path = settings.COURSE_PATH
    f = open(path, 'wb')
    data = pickle.dump(course, f)
    f.close()
    return data


def r_teacher():
    path = settings.TEACHER_PATH
    teacher_dicts = {}
    if os.path.getsize(path):
        f = open(path, 'rb')
        teacher_dicts = pickle.load(f)
        f.close()
    return teacher_dicts


def w_teacher(teacher):
    path = settings.TEACHER_PATH
    f = open(path, 'wb')
    data = pickle.dump(teacher, f)
    f.close()
    return data


def r_manager():
    path = settings.MANAGER_PATH
    manager_dicts = {}
    if os.path.getsize(path):
        f = open(path, 'rb')
        manager_dicts = pickle.load(f)
        f.close()
    return manager_dicts


def w_manager(manager):
    path = settings.MANAGER_PATH
    f = open(path, 'wb')
    data = pickle.dump(manager, f)
    f.close()
    return data


def r_student():
    path = settings.STUDENT_PATH
    student_dicts = {}
    if os.path.getsize(path):
        f = open(path, 'rb')
        student_dicts = pickle.load(f)
        f.close()
    return student_dicts


def w_student(student):
    path = settings.STUDENT_PATH
    f = open(path, 'wb')
    pickle.dump(student, f)
    f.close()
    return True
