def allConstruct(target, wordBank):
    if target == '': return [[]]
    
    result = []
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            print(suffixWays)
            targetWays = list(map(lambda tempList:tempList.insert(0, word), suffixWays))
                
            print (targetWays)
            result.append(targetWays)
                
                
                
            
            
            print(result)
            pass
        
        
    return result
    pass


print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))