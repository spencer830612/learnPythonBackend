from Student_new import Student


FILE_PATH = './student02.txt'

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
    message = f"{student.first_name} {student.second_name} "
    for grade in student.grade_list:
        sum = grade[0] + grade[1] + grade[2]
        average = "{:.2f}".format(sum / 3.0)
        sum_string = "{:.2f}".format(sum)
        message += (f"{grade[0]} {grade[1]} {grade[2]}, "
                    f"sum = {sum_string}, average = {average}\n")
    print(message)


def print_subject_scores(student_list: list[Student]) -> None:
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
    print(f"First subject: total = {sum_first_subject_string}, average = {average_first_subject}")
    print(f"Second subject: total = {sum_second_subject_string}, average = {average_second_subject}")
    print(f"Third subject: total = {sum_third_subject_string}, average = {average_third_subject}")


def rank_students(student_list: list[Student]) -> None:
    sorted_students = sorted(student_list, key=mutiple_sort, reverse=True)
    show_all_students_grade(sorted_students)


def mutiple_sort(student: Student):
    last_grade = student.grade_list[-1]
    sum_grade = last_grade[0] + last_grade[1] + last_grade[2]
    return (sum_grade, last_grade[0], last_grade[1], last_grade[2])


def search_for_name(student_list: list[Student]) -> None:
    name = input("Please enter the name:")
    is_searchable = False
    for student in student_list:
        full_name = f"{student.first_name} {student.second_name}"
        if (name in full_name):
            show_student_grade(student)
            is_searchable = True
    if not is_searchable:
        print("Nothing")


def transfer_to_students_list(student_raw_list: list[str]) -> list[Student]:
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
