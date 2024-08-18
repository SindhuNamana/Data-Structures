class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        left = 0
        right = l-1

        while left<=right:
            mid = left+(right-left)//2
            if newInterval[0]<intervals[mid][0]:
                right = mid-1
            else:
                left = mid+1
        
        print(f"newinterval should be inserted at {left}")
        intervals.insert(left,newInterval)

        new = []
        for interval in intervals:
            if len(new)==0 or new[-1][1]<interval[0]:
                new.append(interval)
            else:
                new[-1][1] = max(new[-1][1], interval[1])
        return new

  #TimeComplexity = O(N)
  #SpaceComplexity = O(N)
