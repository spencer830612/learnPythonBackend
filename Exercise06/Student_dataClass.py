from dataclasses import dataclass, field


@dataclass
class Student:
    first_name: str
    second_name: str
    phone_number: str
    grade_list: list[list[float]] = field(init=False)

    def __post_init__(self):
        self.grade_list = []

    def add_grade(self, grade: list[float]) -> None:
        self.grade_list.append(grade)
