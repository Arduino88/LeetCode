def is_32_bit_signed_integer(n):
    return -2**31 <= n <= 2**31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        prefix = ''
        if x < 0:
            x = abs(x)
            prefix = '-'
        string = str(x)[::-1]
        if is_32_bit_signed_integer(int(string)):
            return (int(prefix + string))
        else:
            return 0
        

newSol = Solution()
print(newSol.reverse(-321))