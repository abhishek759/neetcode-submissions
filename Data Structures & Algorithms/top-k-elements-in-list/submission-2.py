class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            i = str(i)
            if i not in my_dict:
                my_dict[i] = 0
            my_dict[i] += 1

        sorted_dict = dict(sorted(my_dict.items(), key = lambda item : item[1], reverse = True))
        
        return list(sorted_dict.keys())[0:k]

