class Solution:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        memo = {}

        for width in range(2, len(nums)):
            for left in range(len(nums) - width):
                right = left + width
                for pointer in range(left + 1, right):
                    coins = nums[left] * nums[pointer] * nums[right]
                    coins += memo.get((left, pointer), 0) + memo.get((pointer, right), 0)
                    memo[(left, right)] = max(coins, memo.get((left, right), 0))

        print(memo)
        return memo.get((0, len(nums) - 1), 0)
    
    
newSol = Solution()
print(newSol.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,5,2,4,7,3,1,3,6,7,8,4,3,2,8,5,5,3,3,2,1,6,5,3,4,7,3,5,8,9,4,2,4,6,3,9,9,9,9,9,9,9,9,6,7,8,5,5,5,4,2]))