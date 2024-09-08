class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        left = right = 0
        str_dict = Counter()
        #Usage of Counter vs empty dictionary {} vs defaultdict(int)
        max_len = 0

        while right<str_len:
            r = s[right]
            str_dict[r]+=1

            while str_dict[r]>1:
                l = s[left]
                str_dict[s[left]]-=1
                left+=1

            max_len = max(max_len, right-left+1)
            right+=1
        return max_len

        #Time Complexity: O(n)
        #Space Complexity: O(n)
