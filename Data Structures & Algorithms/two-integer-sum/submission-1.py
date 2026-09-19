class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i , num in enumerate(nums):

            c = target - num

            if c in num_to_index:
                return [num_to_index[c], i]

            num_to_index[num] = i


        