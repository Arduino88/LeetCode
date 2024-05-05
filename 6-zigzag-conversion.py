class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = {}
        pointer = 0
        direction = 1
        finalString = ""
        
        for n in range(numRows):
            result[n] = ""
            
        for i in s:
            print(result, pointer)
            result[pointer] += i
            if numRows is not 1:
                pointer += direction
                if pointer == numRows - 1 or pointer == 0:
                    direction *= -1
            
        for key in result:
            finalString += result[key]
            
            
        
        return finalString
        
newSol = Solution()
print(newSol.convert("PAYPALISHIRING", 3))