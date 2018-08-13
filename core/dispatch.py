from view import teachers_view,management_view,students_view


class Management:
    def manager(self,ret):
        management_view.course_init(ret)
        return True

    def teacher(self,ret):
        teachers_view.teachers_init(ret)
        return True

    def student(self,ret):
        students_view.students_init(ret)
        return True


