class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        
        l = 0
        ss = set()
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[r])            
            ans = max(ans, r - l + 1)
        
        return ans