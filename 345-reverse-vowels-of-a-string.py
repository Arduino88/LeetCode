def isVowel(char: str) -> bool:
    vowelList = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    if char in vowelList:
        return True
    else: 
        return False


class Solution:
    def reverseVowels(self, s: str) -> str:
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if not isVowel(s[p1]):
                p1 += 1

            if not isVowel(s[p2]):
                p2 -= 1

            if isVowel(s[p1]) and isVowel(s[p2]) and p1 < p2:
                s = s[:p1] + s[p2] + s[p1 + 1: p2] + s[p1] + s[p2 + 1:]
                p1 += 1
                p2 -= 1
        return s
            
            
sol1 = Solution()
print(sol1.reverseVowels("a."))