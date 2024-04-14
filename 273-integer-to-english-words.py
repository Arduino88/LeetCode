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
    10: "Ten",
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
    num1 = num2 = num3 = 0

    tempString = ''
    if len(sectionString) == 3:
        num1 = int(sectionString[-3])
        
        if not num1 == 0:
            tempString = tempString + ' ' + onesDict[num1] + ' Hundred'
    
    if len(sectionString) >= 2:

        num2 = int(sectionString[-2])

        if not num2 == 0:
            if not num2 == 1:
                tempString = tempString + ' ' + tensDict[num2]
            else:
                tempString = tempString + ' ' + teensDict[int(str(num2) + sectionString[-1])]
                return tempString
            
    num3 = int(sectionString[-1])
    if not num3 == 0:
        tempString = tempString + ' ' + onesDict[num3]
    return(tempString)

def hundredsSectionToWords(sectionString: str, degree: int) -> str:
    num1 = num2 = num3 = 0

    tempString = ''
    if len(sectionString) == 3:
        num1 = int(sectionString[-3])
        
        if not num1 == 0:
            tempString = tempString + ' ' + onesDict[num1] + ' Hundred'
    
    if len(sectionString) >= 2:

        num2 = int(sectionString[-2])

        if not num2 == 0:
            if not num2 == 1:
                tempString = tempString + ' ' + tensDict[num2] 
            else:
                tempString = tempString + ' ' + teensDict[int(str(num2) + sectionString[-1])] + ' ' + degreeDict[degree] 
                return tempString
            
    num3 = int(sectionString[-1])
    if not num3 == 0:
        tempString = tempString + ' ' + onesDict[num3]
    if not (num1 == 0 and num2 == 0 and num3 == 0):
        tempString = tempString + ' ' + degreeDict[degree]
    return(tempString)
    
class Solution:
    def numberToWords(self, num: int) -> str:
        finalString = ""
        inputInt = num
        inputString = str(inputInt)
        firstDigits = inputString[-3:]
        inputString = inputString[:-3]

        if len(inputString) > 0:
            sectionList = makeSections(inputString)
            degree = len(sectionList)
            for i in reversed(range(degree)):
                #if len(sectionList[i]) == 3:
                finalString = finalString + hundredsSectionToWords(sectionList[i], i)

            finalString = finalString + finalThreeDigits(firstDigits)

        elif not inputInt == 0:
            finalString = finalString + finalThreeDigits(firstDigits)

        else:
            finalString = finalString + ' ' + onesDict[0]

        finalString = finalString[1:]
        return(finalString)

num = input()
new = Solution()
print(new.numberToWords(int(num)))