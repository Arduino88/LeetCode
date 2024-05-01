def canConstruct(word, pieces, memo = {}):
    if word == "":
        return True
    
    if word in memo:
        return memo[word]
    
    can_construct = False
    
    for piece in pieces:
        for letter in enumerate(piece):
            if not word[letter[0]] == letter[1]:
                break
        else:
            print(piece, word[len(piece):])
            if canConstruct(word[len(piece):], pieces, memo):
                memo[word] = True
                can_construct = True
            
        memo[word] = can_construct
        print(memo)
            
    return can_construct
    pass



print('abcdef:', canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print('skateboard', canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print('enterapotentpot', canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
]))