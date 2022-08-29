import random

def input_names(nums):

    students_data = []

    for i in range(nums):
        first_name = input("Please enter student's first name: ")
        last_name = input("Please enter student's last name: ")
        student_id = random.randint(111111, 999999)
        email_student = email_calculation(first_name, last_name, str(student_id))

        student_data = {
            "first_name" : first_name,
            "last_name" : last_name,
            "id_student" : student_id,
            "email_student" : email_student
        }

        students_data.append(student_data)

    return students_data

def email_calculation(first_name, last_name, student_id):
    return first_name[0] + last_name + student_id[-3:len(student_id)] + "@example.org"


print(input_names(int(input("Please enter number of students' entries: "))))