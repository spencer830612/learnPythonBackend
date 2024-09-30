FILE_PATH = './student01.txt'

OPTION_PROMPT = "Please choose one and enter its number:"


def print_option():
    print("1. Print students' grade")
    print("2. Print subject scores")
    print("3. Rank students")
    print("4. Search for name")
    print("5. Exit")


def show_all_students_grade(student_raw_list: list[str]) -> None:
    for student in student_raw_list:
        show_student_grade(student)


def show_student_grade(student: str) -> None:
    student_information = student.split(' ')
    name = student_information[0]
    first_grade = int(student_information[1])
    second_grade = int(student_information[2])
    third_grade = int(student_information[3])
    sum = first_grade + second_grade + third_grade
    average = "{:.2f}".format(sum / 3.0)
    print(f"{name} {first_grade} {second_grade} {third_grade}, "
            f"sum = {sum}, average = {average}")


def print_subject_scores(student_list: list[str]) -> None:
    count = len(student_list)
    sum_first_subject = 0.0
    sum_second_subject = 0.0
    sum_third_subject = 0.0
    for student in student_list:
        student_information = student.split(' ')
        sum_first_subject += int(student_information[1])
        sum_second_subject += int(student_information[2])
        sum_third_subject += int(student_information[3])
    average_first_subject = "{:.2f}".format(sum_first_subject / count)
    average_second_subject = "{:.2f}".format(sum_second_subject / count)
    average_third_subject = "{:.2f}".format(sum_third_subject / count)
    print(f"First subject: total = {sum_first_subject}, average = {average_first_subject}")
    print(f"Second subject: total = {sum_second_subject}, average = {average_second_subject}")
    print(f"Third subject: total = {sum_third_subject}, average = {average_third_subject}")


def rank_students(student_list: list[str]) -> None:
    show_all_students_grade(sorted(student_list, key=mutiple_sort, reverse=True))


def mutiple_sort(student: str):
    student_information = student.split(' ')
    first_grade = int(student_information[1])
    second_grade = int(student_information[2])
    third_grade = int(student_information[3])
    sum_grade = first_grade + second_grade + third_grade
    return (sum_grade, first_grade, second_grade, third_grade)


def search_for_name(student_list: list[str]) -> None:
    name = input("Please enter the name:")
    for student in student_list:
        student_information = student.split(' ')
        if (name in student_information[0]):
            show_student_grade(student)
            return None
    print("Can not find")


if __name__ == '__main__':
    try:
        with open(FILE_PATH, 'r') as f:
            students_raw_list = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {FILE_PATH} was not found.")
        students_raw_list = []

    option_number = 0
    while option_number != 5:
        print("\n")
        print_option()
        option_number = int(input(OPTION_PROMPT))
        match option_number:
            case 1:
                show_all_students_grade(students_raw_list)
            case 2:
                print_subject_scores(students_raw_list)
            case 3:
                rank_students(students_raw_list)
            case 4:
                search_for_name(students_raw_list)
            case 5:
                print("Bye bye")
            case _:
                print("Invalid option")
