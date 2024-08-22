class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == len(set(nums)):
            return False
        else:
            return True 

#TimeComplexity = O(N)
#SpaceComplexity = O(N)
