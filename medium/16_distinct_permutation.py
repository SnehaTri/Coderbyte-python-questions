from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm_list = permutations(nums, len(nums))
        perm_list = list(set(perm_list))
        return perm_list
