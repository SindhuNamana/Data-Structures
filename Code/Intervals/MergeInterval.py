class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

      #Sort array
        intervals.sort(key = lambda x: x[0])
        
        new = []
        for interval in intervals:
            #empty or non-over lapping
            if not new or new[-1][1]<interval[0]:
                new.append(interval)
            else:
                new[-1][1] = max(new[-1][1], interval[1])
        
        return new

        #TimeComplexity = 
        #SpaceComplexity
        #Lambda Function
