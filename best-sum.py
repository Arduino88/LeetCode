def howSum(targetSum: int, numbers: list, memo = {}):
    if targetSum == 0:
        print('BASE CASE')
        return []
    
    if targetSum < 0:
        print ('TARGET BELOW ZERO')
        return None

    if targetSum in memo:
        return memo[targetSum]

    for item in numbers:
        
        if item <= targetSum:
            print(item, targetSum, "input:", targetSum - item)
            how_sum = howSum(targetSum - item, numbers)
            if how_sum is not None:
                how_sum.append(item)
                memo[targetSum] = how_sum
                return memo[targetSum]

    memo[targetSum] = None
    return None


print(howSum(678, [5, 3, 4, 7]))