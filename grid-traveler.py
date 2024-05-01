def gridTraveler(m, n, memo = {}):    
    if (m, n) in memo:
        return memo[(m, n)]
    if (m, n) == (1, 1):
        return 1
    if n * m < 1:
        return 0
    
    memo[(m, n)] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    
    print(memo)
    return memo[(m, n)]
    
    
print(gridTraveler(3,3))