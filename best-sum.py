def bestSum(targetSum: int, numbers: list, memo = {}):
    if targetSum == 0:
        print('BASE CASE')
        return []
    
    if targetSum < 0:
        print ('TARGET BELOW ZERO')
        return None

    if targetSum in memo:
        return memo[targetSum]

    shortestCombination = None
    
    for item in numbers:
        remainder = 0
        if item <= targetSum:
            remainder = targetSum - item
            remainderCombination = bestSum(remainder, numbers)
        
            print ('RemainderCombination:', remainderCombination, 'Target:', targetSum)
            remainderCombination.append(item)
            combination = remainderCombination
            print (combination)
            if len(shortestCombination) is 0 or len(combination) < len(shortestCombination):
                shortestCombination = combination
            

    memo[targetSum] = shortestCombination
    return shortestCombination
        



print('FINAL', bestSum(50, [1, 5, 10, 25]))