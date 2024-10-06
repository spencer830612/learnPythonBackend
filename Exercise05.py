from prettytable import PrettyTable
from Student_dataClass import Student
FILE_PATH = './student02.txt'

OPTION_PROMPT = "Please choose one and enter its number:"


def print_option():
    print("1. Print students' grade")
    print("2. Print subject scores")
    print("3. Rank students")
    print("4. Search for name")
    print("5. Exit")


def show_all_students_grade(student_list: list[Student]) -> None:
    table = PrettyTable()
    set_table(table)
    for student in student_list:
        add_student_information(table, student)
    print(table)


def set_table(table: PrettyTable) -> None:
    '''Set the table's title and alignment'''
    table.field_names = [
        "First Name", "Last Name", "Phone NUmber",
        "English", "Chinese", "Math", "Total", "Average"
        ]
    table.align["English"] = "r"
    table.align["Chinese"] = "r"
    table.align["Math"] = "r"
    table.align["Total"] = "r"
    table.align["Average"] = "r"


def add_student_information(table: PrettyTable, student: Student) -> None:
    '''Add each student's information to the table'''
    row = [student.first_name, student.second_name, student.phone_number]
    for grade in student.grade_list:
        sum = grade[0] + grade[1] + grade[2]
        average = "{:.2f}".format(sum / 3.0)
        sum_string = "{:.2f}".format(sum)
        row += [str(grade[0]), str(grade[1]), str(grade[2]), sum_string, average]
        table.add_row(row)
        row = ["", "", ""]


def print_subject_scores(student_list: list[Student]) -> None:
    '''Print the total and average of each subject'''
    times = 0
    sum_first_subject = 0.0
    sum_second_subject = 0.0
    sum_third_subject = 0.0
    for student in student_list:
        for grade in student.grade_list:
            sum_first_subject += grade[0]
            sum_second_subject += grade[1]
            sum_third_subject += grade[2]
            times += 1
    average_first_subject = "{:.2f}".format(sum_first_subject / times)
    average_second_subject = "{:.2f}".format(sum_second_subject / times)
    average_third_subject = "{:.2f}".format(sum_third_subject / times)
    sum_first_subject_string = "{:.2f}".format(sum_first_subject)
    sum_second_subject_string = "{:.2f}".format(sum_second_subject)
    sum_third_subject_string = "{:.2f}".format(sum_third_subject)
    table = PrettyTable()
    table.field_names = ["Subject Name", "Total", "Average"]
    table.align["Total"] = "r"
    table.align["Average"] = "r"
    table.add_row(["English", sum_first_subject_string, average_first_subject])
    table.add_row(["Chinese", sum_second_subject_string, average_second_subject])
    table.add_row(["Math", sum_third_subject_string, average_third_subject])
    print(table)


def rank_students(student_list: list[Student]) -> None:
    '''Use the rule of sorting to sort the data of students'''
    sorted_students_list = sorted(student_list, key=mutiple_sort, reverse=True)
    show_all_students_grade(sorted_students_list)


def mutiple_sort(student: Student):
    '''The rule to sort the data of students'''
    last_grade = student.grade_list[-1]
    sum_grade = last_grade[0] + last_grade[1] + last_grade[2]
    return (sum_grade, last_grade[0], last_grade[1], last_grade[2])


def search_for_name(student_list: list[Student]) -> None:
    '''Search the full name to find the qualified students'''
    name = input("Please enter the name:")
    table = PrettyTable()
    set_table(table)
    is_searchable = False
    for student in student_list:
        full_name = f"{student.first_name} {student.second_name}"
        if (name in full_name and name != " " and name != ""):
            add_student_information(table, student)
            is_searchable = True
    if is_searchable:
        print(table)
    else:
        print("Nothing")


def transfer_to_students_list(student_raw_list: list[str]) -> list[Student]:
    '''Transfer the raw data to a list of Students elements'''
    students_list: list[Student] = []
    student = None
    for student_raw in student_raw_list:
        student_information = student_raw.split(' ')
        if len(student_information) == 6:
            if student is not None:
                students_list.append(student)
            first_name = student_information[0]
            second_name = student_information[1]
            phone = student_information[2]
            student = Student(first_name, second_name, phone)
            first_grade = float(student_information[3])
            second_grade = float(student_information[4])
            third_grade = float(student_information[5])
            student.add_grade([first_grade, second_grade, third_grade])
        elif len(student_information) == 3 and student is not None:
            first_grade = float(student_information[0])
            second_grade = float(student_information[1])
            third_grade = float(student_information[2])
            student.add_grade([first_grade, second_grade, third_grade])
    if student is not None:
        students_list.append(student)
    return students_list


def load_from_file(file_path: str) -> list[str]:
    '''Load the data from the file'''
    students_raw_list = []
    try:
        with open(file_path, 'r') as f:
            students_raw_list = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return students_raw_list


if __name__ == '__main__':
    students_raw_list = load_from_file(FILE_PATH)
    students_list = transfer_to_students_list(students_raw_list)
    option_number = 0
    while option_number != 5:
        print("\n")
        print_option()
        try:
            option_number = int(input(OPTION_PROMPT))
        except ValueError:
            print("You should enter a number")
            continue

        match option_number:
            case 1:
                show_all_students_grade(students_list)
            case 2:
                print_subject_scores(students_list)
            case 3:
                rank_students(students_list)
            case 4:
                search_for_name(students_list)
            case 5:
                print("Bye bye")
            case _:
                print("Invalid option")
