from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if counter == 0:
                majority = nums[i]
            if majority == nums[i]:
                counter += 1
            else:
                counter -= 1

        return majority
    
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]

    
def main():
    try:
        output = Solution.majorityElement("",[2,2,1,1,1,2,2])
        print(output)
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    main()