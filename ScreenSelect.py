from Student import Student


class ScreenSelect():
    def __init__(self, studentList: list[Student]):
        self.options = [
            SelectMethod("Print student's grade", self.printStudentGrade),
            SelectMethod("Print subject score", self.printSubjectScore),
            SelectMethod("Rank Student", self.rankStudent),
            SelectMethod("Search for name", self.searchForName),
            SelectMethod("Exit", self.exit)
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

    def exit(self):
        pass


class SelectMethod():
    def __init__(self, description: str, selectMethod):
        self.description = description
        self.method = selectMethod
