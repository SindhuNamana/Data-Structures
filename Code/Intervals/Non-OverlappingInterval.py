class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        k = -inf
        ans = 0

        #If the intervals are non-overlapping update k to y
        #If the intervals are overlapping increase count and since we are removing the tuple, we compare with earlier y and doesn't update k
        for x,y in intervals:
            if x>=k:
                k = y
            else:
                ans+=1
        return ans

    #TimeComplexity = O(NlogN)
    #SpaceComplexity = O(N)
    #In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space complexity of O(n)

            
        
