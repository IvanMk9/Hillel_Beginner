from student import Student
from group import Group, GroupOverflowError


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
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
