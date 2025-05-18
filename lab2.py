from lab1 import pruverka

class Student(pruverka):
    def __init__(self, first_name=None, last_name=None, birth_year=None, 
                 average_grade=None, specialty=None, group=None):
        super().__init__(first_name, last_name, birth_year)
        self.average_grade = average_grade
        self.specialty = specialty
        self.group = group

    def _calculate_scholarship(self):
        if self.average_grade is None:
            return 0
        if self.average_grade >= 4.5:
            return 2000
        elif self.average_grade >= 4.0:
            return 1500
        return 0

    def __check_attendance(self):
        if self.group is None:
            return "Невідома група"
        return f"Студент групи {self.group}"

    def get_student_info(self):
        scholarship = self._calculate_scholarship()
        attendance = self.__check_attendance()
        course = self.calculate_course()
        course_info = course if course is not None else "Невідомо"
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Курс": course_info,
            "Середній бал": self.average_grade,
            "Спеціальність": self.specialty,
            "Група": self.group,
            "Стипендія": scholarship,
            "Статус відвідування": attendance
        }

    def get_names_list(self, students):
        return [f"{s.first_name} {s.last_name}" for s in students if s.first_name and s.last_name]
