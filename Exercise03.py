from Student import Student


FILE_PATH = './student01.txt'

OPTION_PROMPT = "Please choose one and enter its number:"


def print_option():
    print("1. Print students' grade")
    print("2. Print subject scores")
    print("3. Rank students")
    print("4. Search for name")
    print("5. Exit")


def show_all_students_grade(student_list: list[Student]) -> None:
    for student in student_list:
        show_student_grade(student)


def show_student_grade(student: Student) -> None:
    sum = student.grade1 + student.grade2 + student.grade3
    average_string = "{:.2f}".format(sum / 3.0)
    sum_string = "{:.2f}".format(sum)
    print(f"{student.name} {student.grade1} {student.grade2} {student.grade3},"
          f"sum = {sum_string}, average = {average_string}")


def print_subject_scores(student_list: list[Student]) -> None:
    count = len(student_list)
    sum_first_subject = 0.0
    sum_second_subject = 0.0
    sum_third_subject = 0.0
    for student in student_list:
        sum_first_subject += student.grade1
        sum_second_subject += student.grade2
        sum_third_subject += student.grade3
    average_first_subject = "{:.2f}".format(sum_first_subject / count)
    average_second_subject = "{:.2f}".format(sum_second_subject / count)
    average_third_subject = "{:.2f}".format(sum_third_subject / count)
    sum_first_subject_string = "{:.2f}".format(sum_first_subject)
    sum_second_subject_string = "{:.2f}".format(sum_second_subject)
    sum_third_subject_string = "{:.2f}".format(sum_third_subject)
    print(f"First subject: total = {sum_first_subject_string}, average = {average_first_subject}")
    print(f"Second subject: total = {sum_second_subject_string}, average = {average_second_subject}")
    print(f"Third subject: total = {sum_third_subject_string}, average = {average_third_subject}")


def rank_students(student_list: list[Student]) -> None:
    sorted_students = sorted(student_list, key=mutiple_sort, reverse=True)
    show_all_students_grade(sorted_students)


def mutiple_sort(student: Student):
    sum_grade = student.grade1 + student.grade2 + student.grade3
    return (sum_grade, student.grade1, student.grade2, student.grade3)


def search_for_name(student_list: list[Student]) -> None:
    name = input("Please enter the name:")
    for student in student_list:
        if (name in student.name):
            show_student_grade(student)
            return None
    print("Can not find")


def transfer_to_students_list(student_raw_list: list[str]) -> list[Student]:
    students_list = []
    for student_raw in student_raw_list:
        student_information = student_raw.split(' ')
        name = student_information[0]
        grade1 = float(student_information[1])
        grade2 = float(student_information[2])
        grade3 = float(student_information[3])
        student = Student(name, grade1, grade2, grade3)
        students_list.append(student)
    return students_list


if __name__ == '__main__':
    students_raw_list = []
    try:
        with open(FILE_PATH, 'r') as f:
            students_raw_list = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {FILE_PATH} was not found.")

    student_list = transfer_to_students_list(students_raw_list)
    option_number = 0
    while option_number != 5:
        print("\n")
        print_option()
        option_number = int(input(OPTION_PROMPT))
        match option_number:
            case 1:
                show_all_students_grade(student_list)
            case 2:
                print_subject_scores(student_list)
            case 3:
                rank_students(student_list)
            case 4:
                search_for_name(student_list)
            case 5:
                print("Bye bye")
            case _:
                print("Invalid option")
