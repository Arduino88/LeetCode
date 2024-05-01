def canSum(targetSum, numbers, memo = {}):    
    if targetSum == 0:
        return True
    
    if targetSum < 0:
        return False

    if targetSum in memo:
        return memo[targetSum]

    for item in numbers:
        if item > targetSum:
            continue
        if canSum(targetSum - item, numbers, memo):
            memo[targetSum - item] = True
            print(memo)
            return True
    
    memo[targetSum] = False  
    print(memo)      
    return False



print(canSum(300, [7, 14]))