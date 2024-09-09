class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s1 = Counter(s)
        t1 = Counter(t)

        if len(s1)!=len(t1):
            return False
        for key in s1:
            if key not in t1 or t1[key]!=s1[key]:
                return False
        return True

        #Time-Complexity = O(n)
        #Space-Complexity= O(n)
