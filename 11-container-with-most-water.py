def storedWater(pos1, pos2, array, memo = {}):
    if pos1 == pos2:
        return 0
    
    if (pos1, pos2) in memo:
        return memo[(pos1, pos2)]

    if (pos2, pos1) in memo:
        return memo[(pos2, pos1)]
    
    h = min(array[pos1], array[pos2])
    area = abs(pos1 - pos2) * h
    memo[(pos1, pos2)] = area
    return area


class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        for i in height:
            for j in height:
                water = storedWater(i, j, height)
                if water > maxWater:
                    maxWater = water

        return maxWater
    
    
newSol = Solution()
print(newSol.maxArea([1,8,6,2,5,4,8,3,7]))