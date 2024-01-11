class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        #Brute force
        for i in range(k):
            for j in range(len(nums)):
                nums[j], nums[-1] = nums[-1], nums[j]
        return nums
        
        #Time Complexity = O(n*k)
        #Space Complexity = O(1)
#-----------------------------------------------------------------------------------
        l = len(nums)
        nums_new = [0]*l
        for i in range(l):
            nums_new[(i+k)%l] = nums[i]
        nums[:] = nums_new

#Time Complexity: O(n)
#Space Complexity: O(n)

