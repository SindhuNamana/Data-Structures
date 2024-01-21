class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>=goal-i:
                goal = i

        if goal==0:
            return True
        else:
            return False

        #Time Complexity = O(n)
        #Space Complexity = O(1)
