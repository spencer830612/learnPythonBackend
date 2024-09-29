from LoadFile import loadStudentData
from ScreenSelect import ScreenSelect


def informationBeforeInput(screenSelect: ScreenSelect) -> None:
    index = 1
    print("\n")
    for select in screenSelect.screenSelect:
        print(str(index) + ". " + select.description)
        index += 1
    print(str(index) + ". Exit")


def getChoosenFromInput() -> int:
    while True:
        try:
            choose = int(input("Please choose one and enter its number:\n"))
            if (choose > len(screenSelect.screenSelect)):
                print("Please enter a number in the list")
                continue
            break
        except ValueError:
            print("Please enter a number")
    return choose


studentList = loadStudentData()
if studentList is None:
    # TODO("Other error handling")
    exit(1)
screenSelect = ScreenSelect(studentList)
informationBeforeInput(screenSelect)
choose: int = getChoosenFromInput()
screenSelect.screenSelect[choose - 1].selectMethod()
