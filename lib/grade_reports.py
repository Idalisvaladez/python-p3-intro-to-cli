#!/usr/bin/env python3

def create_grade_reports(student_grades):
    with open('reports/grade_report.txt', 'w') as grades:
        for grade in student_grades:
            grades.write(grade + '\n')


if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        grade = input("Student name, grade: ")
    create_grade_reports(student_grades)
