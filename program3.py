# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Luca Maddaleni
# Section:      273
# Assignment:   Lab 7 Program 3
# Date:         10/06/2020

master_list = []
final_gpa = 0
final_hours = 0
class_count = int(input("How many classes are you taking this semester? "))

for i in range(class_count):
    class_name = input("Enter the class name: ")
    credit_hours = int(input("How many credit hours is the course?: "))
    final_grade = (input("What is your final grade in the course?: "))
    if final_grade.lower() == "a":
        final_grade = 4
    elif final_grade.lower() == "b":
        final_grade = 3
    elif final_grade.lower() == "c":
        final_grade = 2
    elif final_grade.lower() == "d":
        final_grade = 1
    else:
        final_grade = 0
    class_list = []
    class_list.extend((class_name, credit_hours, final_grade))
    master_list.append(class_list)

for i in range(len(master_list)):
    final_gpa += master_list[i][1] * master_list[i][2]
    final_hours += master_list[i][1]

print("Your final GPA is {}.".format(final_gpa/final_hours))