class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = len(nums)
        len_sub = l
        i = j = 0
        sum_ = nums[i]
        while i<=j and j<l:
            if sum_>=target:
                len_sub = min(j-i+1, len_sub)
                sum_-=nums[i]
                i+=1
            else:
                j+=1
                if j<len(nums):
                    sum_+=nums[j]

        if sum(nums)<target:
            return 0
        else:
            return len_sub

      #Time Complexity = O(n)
      #Space Complexity = O(1)
