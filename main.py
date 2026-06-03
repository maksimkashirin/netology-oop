class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

def average_students_grade(students, course):
    all_grades = []

    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]

    if len(all_grades) == 0:
        return 0

    return sum(all_grades) / len(all_grades)


def average_lecturers_grade(lecturers, course):
    all_grades = []

    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]

    if len(all_grades) == 0:
        return 0

    return sum(all_grades) / len(all_grades)


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_2 = Student('Ольга', 'Алёхина', 'Ж')

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Сергей', 'Сергеев')

reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Some', 'Buddy')


student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Git']


lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Java']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)


student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Git', 9)

student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Java', 7)


print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()

print('Сравнение студентов:')
print(student_1 > student_2)

print('Сравнение лекторов:')
print(lecturer_1 > lecturer_2)

print('Средняя оценка студентов по Python:')
print(average_students_grade([student_1, student_2], 'Python'))

print('Средняя оценка лекторов по Python:')
print(average_lecturers_grade([lecturer_1, lecturer_2], 'Python'))