from Student import Student


class ScreenSelect():
    def __init__(self, studentList: list[Student]):
        self.screenSelect = [
            SelectMethod("Print student's grade", self.printStudentGrade),
            SelectMethod("Print subject score", self.printSubjectScore),
            SelectMethod("Rank Student", self.rankStudent),
            SelectMethod("Search for name", self.searchForName)
        ]
        self.studentList = studentList

    def printStudentGrade(self):
        pass

    def printSubjectScore(self):
        pass

    def rankStudent(self):
        pass

    def searchForName(self):
        pass


class SelectMethod():
    def __init__(self, description: str, selectMethod):
        self.description = description
        self.selectMethod = selectMethod
