class Solution:
    def climbStairs(self, n: int) -> int:
        #no of ways to n = ways to reach (n-1) + ways to reach (n-2)
        def ways(i):
            if i in memo:
                return memo[i]
            
            memo[i] = ways(i-1)+ways(i-2)
            return memo[i]

        memo = {1:1, 2:2}
        return ways(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        #no of ways to n = ways to reach (n-1) + ways to reach (n-2)

        ways = [0]*(n+1)
        for i in range(n+1):
            if i==1:
                ways[1]=1
            elif i==2:
                ways[2]=2
            else:
                ways[i] = ways[i-1]+ways[i-2]
        return ways[n]
