def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charset = set()
        ans = 0
        i = 0
        j = 0
        
        while i < n and j < n:
            if s[j] not in charset:
                charset.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                charset.remove(s[i])
                i += 1
                
        return ans