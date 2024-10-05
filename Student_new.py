class Student():
    def __init__(self, first_name: str, second_name: str, telephone_number: str):
        self.first_name = first_name
        self.second_name = second_name
        self.telephone_number = telephone_number
        self.grade_list: list[list[float]] = []

    def add_grade(self, grade: list[float]) -> None:
        self.grade_list.append(grade)
