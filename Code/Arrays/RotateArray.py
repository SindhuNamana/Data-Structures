class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        l = len(nums)
        nums_new = [0]*l
        for i in range(l):
            nums_new[(i+k)%l] = nums[i]
        nums[:] = nums_new

#Time Complexity: O(n)
#Space Complexity: O(n)

