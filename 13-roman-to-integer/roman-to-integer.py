class Solution:
    def romanToInt(self, s: str) -> int:
        num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
      
        res = 0
        i = 0
        while i < len(s):
            cur = num[s[i]]

            if i+1 < len(s) and cur < num[s[i+1]]:
                res += num[s[i+1]] - cur
                i += 2

            else:
                res += cur
                i += 1
            
        return res