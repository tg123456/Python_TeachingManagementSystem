class School:
    def __init__(self, id, name, address, other):
        self.id = id
        self.name = name
        self.address = address
        self.other = other


class Course:
    def __init__(self, id, name, school_name,cycle, price,other):
        self.id = id
        self.name = name
        self.school_name = school_name
        self.cycle = cycle
        self.price = price
        self.other = other


class Grade:
    def __init__(self, id, name, school_name, course_name, other):
        self.id = id
        self.name = name
        self.school_name = school_name
        self.course_name = course_name
        self.other = other


class Person:
    def __init__(self, id, name, age, school_name, other, password, sex='男', role='manager'):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.school_name = school_name
        self.role = role
        self.other = other
        self.password = password


class Manager(Person):
    def __init__(self, id, name, age, school_name, other, password, sex='男', role='manager'):
        super().__init__(id, name, age, school_name, other, password, sex, role)



class Teacher(Person):
    def __init__(self, id, name, age, school_name, course_name, other, password, sex='男', role='teacher'):
        super().__init__(id, name, age, school_name, other, password, sex, role)
        self.course_name = course_name


class Student(Person):
    def __init__(self, id, name, age, school_name, course_name, teacher_name, grade_name, other, password, score=0,
                 sex='男', role='student'):
        super().__init__(id, name, age, school_name, other, password, sex, role)
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.grade_name = grade_name
        self.score = score
