class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            product = 1
            the_list = nums.copy()
            the_list.remove(nums[i])
            for j in the_list:
                product *= j
            new_list.append(product)

        return new_list

        