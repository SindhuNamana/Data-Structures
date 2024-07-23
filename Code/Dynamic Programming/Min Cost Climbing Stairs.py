#Bottom-up approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])
        return min_cost[-1]

        #Time Complexity = O(N)
        #Space Complexity = O(N)
