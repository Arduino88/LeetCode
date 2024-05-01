def bestSum(targetSum: int, numbers: list, memo = {}):
    if targetSum == 0:
        return []
    
    if targetSum in memo:
        return memo[targetSum]
    
    
    smallestCombination = None
    
    for num in numbers:
        if num > targetSum:
            continue
        
        returnedList = bestSum(targetSum - num, numbers, memo)
        
        if returnedList == None:
            continue
        
        combination = [num] + returnedList
        
        if smallestCombination is None:
            smallestCombination = combination
            continue
            
        if len(smallestCombination) > len(combination):
            smallestCombination = combination
            
    memo[targetSum] = smallestCombination
    #print(f"Target: {targetSum}, smallest combination: {smallestCombination}")
    return smallestCombination


print(bestSum(100, [2, 5, 10, 25]))