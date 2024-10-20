from prettytable import PrettyTable
from Student_dataClass import Student
FILE_PATH = './student02.txt'

OPTION_PROMPT = "Please choose one and enter its number: "


def print_option():
    print("1. Print students' grade")
    print("2. Print subject scores")
    print("3. Rank students")
    print("4. Search for name")
    print("5. Exit")


def get_students_list_table(student_list: list[Student]) -> PrettyTable:
    table = PrettyTable()
    __set_table(table)
    for student in student_list:
        __add_student_information(table, student)
    return table


def __set_table(table: PrettyTable) -> None:
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


def __add_student_information(table: PrettyTable, student: Student) -> None:
    '''Add each student's information to the table'''
    row = [student.first_name, student.second_name, student.phone_number]
    for grade in student.grade_list:
        sum = grade[0] + grade[1] + grade[2]
        average = sum / 3.0
        row.extend([str(grade[0]), str(grade[1]), str(grade[2]), f"{sum:.2f}", f"{average:.2f}"])
        table.add_row(row)
        row = ["", "", ""]


def get_subject_scores_table(student_list: list[Student]) -> PrettyTable:
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
    average_first_subject = sum_first_subject / times
    average_second_subject = sum_second_subject / times
    average_third_subject = sum_third_subject / times
    table = PrettyTable()
    table.field_names = ["Subject Name", "Total", "Average"]
    table.align["Total"] = "r"
    table.align["Average"] = "r"
    table.add_row(["English", f"{sum_first_subject:.2f}", f"{average_first_subject:.2f}"])
    table.add_row(["Chinese", f"{sum_second_subject:.2f}", f"{average_second_subject:.2f}"])
    table.add_row(["Math", f"{sum_third_subject:.2f}", f"{average_third_subject:.2f}"])
    return table


def get_ranked_students_table(student_list: list[Student]) -> PrettyTable:
    '''Use the rule of sorting to sort the data of students'''
    sorted_students_list = sorted(student_list, key=__mutiple_sort, reverse=True)
    return get_students_list_table(sorted_students_list)


def __mutiple_sort(student: Student):
    '''The rule to sort the data of students'''
    last_grade = student.grade_list[-1]
    sum_grade = last_grade[0] + last_grade[1] + last_grade[2]
    return (sum_grade, last_grade[0], last_grade[1], last_grade[2])


def get_student_table_by_search(student_list: list[Student]) -> PrettyTable | None:
    '''Search the full name to find the qualified students.
    If we don't find any student, return None'''

    name = input("Please enter the name:")
    table = PrettyTable()
    __set_table(table)
    is_searchable = False
    for student in student_list:
        full_name = f"{student.first_name} {student.second_name}"
        if (name in full_name and name != " " and name != ""):
            __add_student_information(table, student)
            is_searchable = True
    if is_searchable:
        return table
    else:
        return None


def transfer_to_students_list(student_raw_list: list[str]) -> list[Student]:
    '''Transfer the raw data to a list of Students elements'''
    students_list: list[Student] = []
    student = None
    for student_raw in student_raw_list:
        student_information = student_raw.split(' ')
        if len(student_information) == 6:
            ''' Data Format: Spencer Dai 101021203 100 100 100'''
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
            ''' Data Format: 100 100 100'''
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

        result = None
        if option_number == 1:
            result = get_students_list_table(students_list)
        elif option_number == 2:
            result = get_subject_scores_table(students_list)
        elif option_number == 3:
            result = get_ranked_students_table(students_list)
        elif option_number == 4:
            # If we don't find any student, return None
            result = get_student_table_by_search(students_list)

        if result is not None:
            print(result)
        elif option_number == 4:
            print("Find nothing.")
        elif option_number == 5:
            print("Bye bye")
        else:
            print("Invalid option")
