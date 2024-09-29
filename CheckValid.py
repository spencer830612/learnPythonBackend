import re


def isVaildForAddGrade(strList: list[str]) -> bool:
    if len(strList) != 3:
        return False
    rule = re.compile(r'^[0-9]+$')
    for grade in strList:
        if not rule.match(grade):
            return False
    return True


def isVaildForAddNumber(numberString: str) -> bool:
    # 檢查電話號碼是否符合規定
    # TODO(check(numberString))
    return True
