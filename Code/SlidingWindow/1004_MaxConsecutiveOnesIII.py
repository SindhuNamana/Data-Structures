class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left=right=0
        # count_ones = 0
        # count_zeros = 0
        max_val=0

        while right<len(nums):
            if nums[right]==0:
                k=k-1
            
            if k>=0:
                max_val = max(max_val,right-left+1)
            else:
                if nums[left]==0:
                    k+=1
                left+=1
            right+=1

            # if nums[right]==1:
            #     count_ones+=1
            # else:
            #     count_zeros+=1
            
            # if count_zeros<=k:
            #     max_val = max(max_val,right-left+1)
            #     right+=1
            # else:
            #     class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left=right=0
        # count_ones = 0
        # count_zeros = 0
        max_val=0

        while right<len(nums):
            if nums[right]==0:
                k=k-1
            
            if k>=0:
                max_val = max(max_val,right-left+1)
                right+=1
            else:
                if nums[left]==0:
                    k+=1
                left+=1
                right+=1
    return max_val

    #Time-Complexity = O(n)
    #Space-Complexity = O(1)

            # if nums[right]==1:
            #     count_ones+=1
            # else:
            #     count_zeros+=1
            
            # if count_zeros<=k:
            #     max_val = max(max_val,right-left+1)
            #     right+=1
            # else:
            #     max_val = max(max_val,right-left)
            #     if nums[left]==1:
            #         count_ones-=1
            #     else:
            #         count_zeros-=1
            #     left+=1
            #     right+=1
        # return max_val


        
