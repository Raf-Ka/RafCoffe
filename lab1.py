class Raf:
    def __init__(self, name=None, surname=None, birth_year=None, manual_course=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.manual_course = manual_course

    def college_year_calc(self, current_year=2024):
        if self.birth_year is None:
            return "невідомо"

        age = current_year - self.birth_year

        if self.manual_course is not None and 1 <= self.manual_course <= 4:
            return self.manual_course

        if age == 16:
            return 1
        elif age == 17:
            return 2
        elif age == 18:
            return 3
        elif age == 19:
            return 4
        else:
            return "невідомо"

    @staticmethod
    def get_names_list(students):
        return [f"{student.name or 'Імʼя невідоме'} {student.surname or 'Прізвище невідоме'}" for student in students]


student1 = Raf("Діма", "Поліщук", 2008)
student2 = Raf("Дімон", None, 2000)
student3 = Raf("Дмітрій", "Поляков", 2007, 2)

students = [student1, student2, student3]

names_list = Raf.get_names_list(students)
print("Список імен:", names_list)

for s in students:
    print(f"Студент {s.name or 'Невідомо'} {s.surname or ''} знаходиться на {s.college_year_calc()} курсі.")
