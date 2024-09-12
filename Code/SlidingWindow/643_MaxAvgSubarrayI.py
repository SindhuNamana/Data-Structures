class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # left = right = 0
        # max_sum = float('-inf')
        # sum_val = 0
 
        # while right<len(nums):
        #     if right<k-1:
        #         sum_val+=nums[right]
        #     else:
        #         sum_val+=nums[right]
        #         max_sum = max(sum_val, max_sum)
        #         sum_val-=nums[left]
        #         left+=1
        #     right+=1
        # return max_sum/k

        left = 0
        #window_length = right-left+1
        max_sum = float('-inf')
        sum_val = sum(nums[:k-1])

        for right in range(k-1,len(nums)):
            sum_val+=nums[right]
            max_sum = max(sum_val, max_sum)
            sum_val-=nums[left]
            left+=1
        return max_sum/k

        #Time-Complexity = O(n)
        #Space-Complexity = O(1)
