def dp(s, wordDict):
    if s == '':
        print('s == empty string, returning None')
        return None

    #print('wordDict', wordDict)
    possibilities = []
    remaining = wordDict.copy()
    removeList = []
    longest = len(max(wordDict, key = len))
    
    for k in range(longest):
        for i in range(len(remaining)):
            print(s, k, i, remaining, possibilities)
            if k < len(remaining[i]) and k < len(s):
                if remaining[i][k] < s[k]:
                    removeList.append(remaining[i])
                    continue

                if remaining[i][k] == s[k]:
                    if k == len(remaining[i]) - 1:
                        possibilities.append(remaining[i])
        
        #remove impossible words:
        for word in removeList:
            #print(word)
            remaining.remove(word)

        removeList.clear()

    print(f'POSSIBILITIES: {possibilities}')

    if len(possibilities) == 1 and len(s) == len(possibilities[0]):
        print(f'len(possibilities) == 1, returning possibilities: {possibilities}')
        return possibilities
    
    if possibilities == []:
        print('possibilities == [], returning None')
        return None

    returnList = []

    #print('returning...')
    for possibility in possibilities:
        print(f'possibility: {possibility} + {s[len(possibility):]}')
        temp = dp(s[len(possibility):], wordDict)
        print(f'temp: {temp}')        
        
        if temp:
            for i, option in enumerate(temp):
                print(f'words: {possibility}, {option}')
                print(f'types: {type(possibility)}, {type(option)}')

                temp[i] = possibility + ' ' + option
                print(f'temp[i]: {temp[i]}')
                returnList.append(temp[i])

    if returnList == []:
        print('returnList == [], returning None')
        return None

    print(f'FUNCTION CALL; INPUT: {s}, RETURN: {returnList}')
    return returnList




class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict.sort()
        return dp(s, wordDict)
    

newSol = Solution()

#print(newSol.wordBreak('leetcode', ['leet', 'code']))
#print(newSol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
#print(newSol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
print(newSol.wordBreak("aaaaaaa", ["aaaa","aaa"]))
