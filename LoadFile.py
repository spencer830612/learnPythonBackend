from CheckValid import isVaildForAddGrade, isVaildForAddNumber
from Student import Student


def __buildStudentInformation(studentList: list[str]) -> Student:
    # 根據輸入字串建立 Student 物件
    if len(studentList) != 6:
        raise ValueError("The number of student information is incorrect")
    fistName = studentList[0]
    secondName = studentList[1]
    number = studentList[2]
    if (isVaildForAddNumber(number) is not True):
        # TODO(reportAndHandle(error))
        pass
    student = Student(fistName, secondName, number)
    __addNewGrade(studentList[3:], student)
    return student


def __addNewGrade(gradeList: list[str], student: Student) -> None:
    # 根據輸入字串新增成績
    if (isVaildForAddGrade(gradeList) is not True):
        # TODO(reportAndHandle(error))
        pass
    intList = [eval(i) for i in gradeList]
    student.addGradeList(intList)


def loadStudentData() -> list[Student] | None:
    # 讀取檔案，並轉換成 Studnet 的串獵物件
    # 輸出：讀取成功回傳 Student 物件串列，否則回傳 None        
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
