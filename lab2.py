from lab1 import pruverka

class Student(pruverka):
    def __init__(self, first_name=None, last_name=None, birth_year=None, 
                 average_grade=None, specialty=None, group=None):
        super().__init__(first_name, last_name, birth_year)
        self.average_grade = average_grade
        self.specialty = specialty
        self.group = group

    def _calculate_scholarship(self):
        """Захищений метод для розрахунку стипендії"""
        if self.average_grade is None:
            return 0
        if self.average_grade >= 4.5:
            return 2000
        elif self.average_grade >= 4.0:
            return 1500
        return 0

    def __check_attendance(self):
        """Приватний метод для перевірки відвідуваності"""
        if self.group is None:
            return "Невідома група"
        return f"Студент групи {self.group}"

    def get_student_info(self):
        """Публічний метод для отримання інформації про студента"""
        scholarship = self._calculate_scholarship()
        attendance = self.__check_attendance()
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Курс": self.calculate_course(),
            "Середній бал": self.average_grade,
            "Спеціальність": self.specialty,
            "Група": self.group,
            "Стипендія": scholarship,
            "Статус відвідування": attendance
        } 