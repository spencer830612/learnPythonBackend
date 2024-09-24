class Student():
    def __init__(self, firstName: str, secondName: str, number: str):
        self.firstName = firstName
        self.secondName = secondName
        self.number = number
        self.gradeSequenceList: list[object] = []

    def addGradeList(self, gradeList: list[int]):
        if len(gradeList) != 3:
            raise ValueError("The number of grades is incorrect")
        self.gradeSequenceList.append(gradeList)
