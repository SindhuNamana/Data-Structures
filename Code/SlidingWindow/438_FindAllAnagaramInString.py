class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr_ind = []
        count_p = Counter(p)
        len_p = len(p)
        count_s = Counter(s[:len_p-1])
        for j in range(len_p-1, len(s)):
            i = (j-len_p+1) #window_length = j-i+1
            count_s[s[j]]+=1
            if count_p == count_s:
                arr_ind.append(j-len_p+1)
            count_s[s[j-len_p+1]]-=1
        return arr_ind
        #Time-Complexity = O(n)
        #Space-Complexity = O(1)    

        #i=j=0
        #arr_ind = []
        #p_sort = sorted(p)
        # p_count = Counter(p)
        # while j<len(s):
        #     if (j-i+1)<len(p):
        #         j+=1
        #     elif (j-i+1)==len(p):
        #         s_count = Counter(s[i:j+1])
        #         if s_count == p_count:
        #         #if sorted(s[i:j+1])==p_sort:
        #             arr_ind.append(i)
        #         j+=1
        #         i+=1
        # return arr_ind
