from Student import Student


def __buildStudentInformation(studentList: list[str]) -> Student:
    if len(studentList) != 6:
        raise ValueError("The number of student information is incorrect")
    fistName = studentList[0]
    secondName = studentList[1]
    number = studentList[2]
    firstGrade = eval(studentList[3])
    secondGrade = eval(studentList[4])
    thirdGrade = eval(studentList[5])
    student = Student(fistName, secondName, number)
    student.addGradeList([firstGrade, secondGrade, thirdGrade])
    return student


def __addNewGrade(gradeList: list[str], student: Student) -> None:
    if len(gradeList) != 3:
        raise ValueError("The number of grades is incorrect")
    intList = [eval(i) for i in gradeList]
    student.addGradeList(intList)


def loadStudentData() -> list[Student] | None:
    try:
        with open('student.txt') as content:
            line = content.readline()
            studentList: list[Student] = []
            student = None
            while line:
                lineSplit = line.split(" ")
                if (len(lineSplit) == 6):
                    if (student is not None):
                        studentList.append(student)
                    student = __buildStudentInformation(lineSplit)
                elif (len(lineSplit) == 3):
                    if (student is not None):
                        __addNewGrade(lineSplit, student)
                line = content.readline()
            if (student is not None):
                studentList.append(student)

        return studentList
    except (FileNotFoundError, PermissionError, OSError) as error:
        print("File not found or permission error")
        return None
        # TODO(report(error))
