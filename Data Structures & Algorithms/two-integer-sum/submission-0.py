class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for n in range (len(nums)): 
            for i in range (len(nums)):
                if n == i: 
                    pass
                else:
                    sum = nums[n]+nums[i]
                    if sum == target:
                        return [n,i]

        