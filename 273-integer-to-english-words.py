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
    0: "Thousand",
    1: "Million",
    2: "Billion",
    3: "Trillion",
    4: "Quadrillion",
    5: "Quintillion",
    6: "Sextillion"
    }

def makeSections(number: int) -> list:
    tempList = []
    tempString = str(number)
    while len(tempString) > 0:
        tempList.append(tempString[-3:])
        tempString = tempString[:-3]
    return tempList

def finalThreeDigits(sectionString: str) -> str:
    
    tempString = ''

    num1 = int(sectionString[-3])
    
    if not num1 == 0:
        tempString = tempString + onesDict[num1] + ' Hundred '

    num2 = int(sectionString[-2])

    if not num2 == 0:
        if not num2 == 1:
            tempString = tempString + tensDict[num2] + ' '
        else:
            tempString = tempString + teensDict[int(str(num2) + str(num3))] + ' '
            return tempString
            
    num3 = int(sectionString[-1])
    if not num3 == 0:
        tempString = tempString + onesDict[num3] + ' '

    return(tempString)



def hundredsSectionToWords(sectionString: str, degree: int) -> str:
    
    tempString = ''
    if len(sectionString) == 3:
        num1 = int(sectionString[-3])
        
        if not num1 == 0:
            tempString = tempString + onesDict[num1] + ' Hundred '
    
    if len(sectionString) >= 2:

        num2 = int(sectionString[-2])

        if not num2 == 0:
            if not num2 == 1:
                tempString = tempString + tensDict[num2] + ' '
            else:
                tempString = tempString + teensDict[int(str(num2) + str(num3))] + ' ' + degreeDict[degree] + ' '
                return tempString
            
    num3 = int(sectionString[-1])
    if not num3 == 0:
        tempString = tempString + onesDict[num3] + ' '

    tempString = tempString + degreeDict[degree] + ' '
    return(tempString)
    


    
inputInt = 1234567
inputString = str(inputInt)

firstDigits = inputString[-3:]
print(firstDigits)

inputString = inputString[:-3]
print(inputString)

if len(inputString) > 0:
    sectionList = makeSections(inputString)

    degree = len(sectionList)
    print(degree)

    print(sectionList)


    for i in reversed(range(degree)):
        #if len(sectionList[i]) == 3:
        print(hundredsSectionToWords(sectionList[i], i))
        
    print(finalThreeDigits(firstDigits))

elif not inputString == '0':
    print(finalThreeDigits(firstDigits))

else:
    print(onesDict[0])





