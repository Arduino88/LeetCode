class Solution:
    def myAtoi(self, s: str) -> int:
        pointer = 0
        
        while (s[pointer] == " ") and len(s)!= 1:
            pointer += 1
            
        if s == "":
            return 0
        elif (not s[pointer].isdigit()) and not ((s[pointer] == "-" or s[pointer] == "+") and len(s) > pointer + 1):
            return 0
        
        sign = 1
        if s[pointer] == "-":
            sign = -1
            pointer += 1
        elif s[pointer] == "+":
            pointer += 1
            
        num = 0
        
        for i in range(pointer,len(s)):
            if not s[i].isdigit():
                break
            else:
                num *= 10
                num += int(s[i])
                
        return sign * min(max(-2**31,num),2**31)
    
    
newSol = Solution()
print(newSol.myAtoi("42"))