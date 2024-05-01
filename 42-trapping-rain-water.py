class Solution:
    def trap(self, height: list[int]) -> int:
        
        right = list()
        left = list()
        
        # populate left array

        for i in range(len(height)):
            if i == 0:
                left.append(height[i])
                continue

            if left[i - 1] < height[i]:
                left.append(height[i])
            else:
                left.append(left[i - 1])

        # populate right array
        
        for i in range(len(height)):
            if i == 0:
                right.insert(0, height[-(i+1)])
                continue
            
            if right[0] < height[-(i+1)]:
                right.insert(0, height[-(i+1)])
            else:
                right.insert(0, right[0])


        waterArea = sum(list(map(lambda x, y, z: min(x, y) - z, right, left, height)))
        
        return(waterArea)
    
sol1 = Solution()

print(sol1.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))