def isPalindrome(string, memo = {}):
    if string in memo:
        return memo[string]
    
    string2 = list(string)
    string2.reverse()
    string2 = "".join(string2)
    memo[string] = string == string2
    return memo[string]


class Solution:
    def longestPalindrome(self, s: str):
        
        if len(s) <= 1:
            return s
        
        longestSubstring = ''
        for letter in enumerate(s):
            for i in range(len(s)):
                substring = s[letter[0] : letter[0] + i + 1]
                if isPalindrome(substring) and len(substring) > len(longestSubstring):
                    longestSubstring = substring
        return longestSubstring


        
        


newSol = Solution()
print(f"Test1, accepted 'a': {newSol.longestPalindrome('a')}")
print(f"Test1, accepted 'bab': {newSol.longestPalindrome('babad')}")
print(f"Test1, accepted 'bb': {newSol.longestPalindrome('cbbd')}")
print(f"Test1, accepted 'a': {newSol.longestPalindrome('ab')}")
print(f"Test1, accepted 'bb': {newSol.longestPalindrome('bb')}")
print(f"Test1, accepted 'bb': {newSol.longestPalindrome('abb')}")


