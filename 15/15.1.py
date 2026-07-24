class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (
            f'{self.first_name} {self.last_name}, '
            f'{self.age} years old, gender: {self.gender}'
        )


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (
            f'Student {self.first_name} {self.last_name}, '
            f'{self.age} years old, gender: {self.gender}, '
            f'record book: {self.record_book}'
        )


class GroupOverflowError(Exception):
    pass


class Group:
    max_students = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupOverflowError(
                f'Unable to add the student. '
                f'The group has already'
                f' reached the maximum number of students. '
                f'({self.max_students}).'
            )
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, (
    'Метод пошуку повинен повертати екземпляр'
)

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')


test_group = Group('TEST-1')

for i in range(10):
    new_student = Student(
        'Male', 20, f'Name{i}', f'Surname{i}', f'RB{i}'
    )
    test_group.add_student(new_student)

print(f'Number of students in the test group: {len(test_group.group)}')

try:
    eleventh_student = Student(
        'Female', 21, 'Anna', 'Green', 'RB100'
    )
    test_group.add_student(eleventh_student)
except GroupOverflowError as error:
    print(f'Error adding student: {error}')
