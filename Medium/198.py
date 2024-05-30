from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
    #     Max = 0
    #     if len(nums) <= 2:
    #         return max(nums)
        
    #     for i in range(len(nums)):
    #         if Max < nums[i] + Solution.GetMaxAmount(i+2, nums):
    #             Max = nums[i] + Solution.GetMaxAmount(i+2, nums)
    #     return Max
    
    # def GetMaxAmount(start, nums: List[int]) -> int:
    #     if start + 1 > len(nums):
    #         return 0
    #     if start + 1 == len(nums):
    #         return nums[start]
    #     return nums[start] + Solution.GetMaxAmount(start+2, nums)
        rob = 0
        not_rob = 0
        
        for num in nums:
            cur_rob = not_rob + num
            not_rob, rob = max(not_rob, rob), cur_rob

        return max(rob, not_rob)


if __name__ == "__main__":
    output = Solution.rob("", [2,7,9,3,1])
    print(output)