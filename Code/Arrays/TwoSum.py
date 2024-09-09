class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Brute-force
        #Time-Complexity = O(n^2)
        #Space-Complexity = O(n)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        #Time-Complexity = O(n)
        #Space-Complexity= O(n)
        hasmap = {}
        for i in range(len(nums)):
            hasmap[nums[i]] = i
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hasmap and i!=hasmap[diff]:
                return [i, hasmap[diff]]
