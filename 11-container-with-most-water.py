def storedWater(pos1, pos2, array, memo):
    print(f'position1: {pos1}, position2: {pos2}')
    if pos1 == pos2:
        return 0, memo
    
    if (pos1, pos2) in memo:
        return memo[(pos1, pos2)], memo

    if (pos2, pos1) in memo:
        return memo[(pos2, pos1)], memo
    
    h = min(array[pos1], array[pos2])
    print(f"h: {h}")
    area = abs(pos1 - pos2) * h
    memo[(pos1, pos2)] = area
    return area, memo


class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        memo = {}
        for i in range(len(height)):
            for j in range(len(height)):
                water, memo = storedWater(i, j, height, memo)
                #print(height[i], height[j])
                print(f'pos1: {i}, pos2: {j}')
                print('water:', water)
                if water > maxWater:
                    maxWater = water

        return maxWater
    
    
newSol = Solution()
#print(newSol.maxArea([1,8,6,2,5,4,8,3,7]))
#print(newSol.maxArea([1,1]))
print(newSol.maxArea([4,3,2,1,4]))