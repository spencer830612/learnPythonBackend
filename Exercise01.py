'''
Read the content of student01 and display the name of each student, each grade, the total grade and the average grade.
'''

FILE_PATH = './student01.txt'

if __name__ == '__main__':
    try:
        with open(FILE_PATH, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {FILE_PATH} was not found.")
        lines = []

    for line in lines:
        student_information = line.split(' ')
        name = student_information[0]
        first_grade = float(student_information[1])
        second_grade = float(student_information[2])
        third_grade = float(student_information[3])
        sum = first_grade + second_grade + third_grade
        sum_string = "{:.2f}".format(sum)
        average_string = "{:.2f}".format(sum / 3.0)
        print(f"{name} {first_grade} {second_grade} {third_grade}, "
              f"sum = {sum_string}, average = {average_string}")
