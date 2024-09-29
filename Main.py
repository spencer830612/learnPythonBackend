from LoadFile import loadStudentData, printStudentData
from ScreenSelect import ScreenSelect


def informationBeforeInput(screenSelect: ScreenSelect) -> None:
    index = 1
    print("\n")
    for select in screenSelect.options:
        print(str(index) + ". " + select.description)
        index += 1


def getChoosenFromInput() -> int:
    isAsked = True
    while isAsked:
        try:
            choose = int(input("Please choose one and enter its number:\n"))
            if (choose > len(screenSelect.options)):
                print("Please enter a number in the list")
            else:
                isAsked = False
        except ValueError:
            print("Please enter a number")
    return choose


studentList = loadStudentData()
if studentList is None:
    # TODO("Other error handling")
    exit(1)
printStudentData(studentList)
screenSelect = ScreenSelect(studentList)
informationBeforeInput(screenSelect)
choose: int = getChoosenFromInput()
screenSelect.options[choose - 1].method()
