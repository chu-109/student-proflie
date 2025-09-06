import os
def create_profile():
    print(f'\n---Create a new student dlie---')
    student_name = input('student name:')
    student_age = int(input('student age:'))
    student_grade = input('grade:')
    favorite_subject = input('My favorite subject:')
    
    if student_age < 13:
        group = 'primary group'
    elif student_age <19:
        group = 'secondaey school group'
    else:
        group = 'university geoup'

    return f'student:{student_name},age:{student_age},group:{group},grade:{student_grade}, favorite subject:{favorite_subject}'

print('===student Learning Record System===')
count = int(input('Who many student records to crseate?'))

students = []
for i in range(count):
    profile = create_profile()
    students.append(profile)


for profile in students: 
    print(profile)
with open('student_records.txt', 'w', encoding='utf-8') as file:
    file.write('=== Student Records ===\n')
    file.write('Created on: 2024-06-30\n\n')
    for profile in students:
        file.write(profile + '\n')


file_path = os.path.abspath('student_records.txt')

print('\n all proflie seve to student_records.txt')
