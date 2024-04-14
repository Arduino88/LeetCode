onesDict = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",

    }

teensDict = {
    1: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}

tensDict = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
    }

degreeDict = {
    1: "Thousand",
    2: "Million",
    3: "Billion",
    4: "Trillion"
    }

def makeSections(number: int) -> list:
    tempList = []
    tempString = str(number)
    while len(tempString) > 4:
        tempList.append(tempString[:3])
        tempString = tempString[3:]
    return tempList

def hundredsSectionToWords(sectionString: str, degree: int) -> str:
    
    tempString = ''
    num1 = int(sectionString[0])
    num2 = int(sectionString[1])
    num3 = int(sectionString[2])
    
    if not num1 == 0:
        tempString = tempString + onesDict[num1] + ' Hundred '
    
    if not num2 == 0:
        if not num2 == 1:
            tempString = tempString + tensDict[num2] + ' '
        else:
            tempString = tempString + teensDict[int(str(num2) + str(num3))]
            return tempString

    if not num3 == 0:
        tempString = tempString + onesDict[num3] + ' '

    return(tempString)

    
inputInt = 1234567890123456789

sectionList = makeSections(int(inputInt))

degree = len(sectionList)

print(inputInt)

for i in reversed(range(degree)):
    print(hundredsSectionToWords(sectionList[i], degreeDict[i]))





