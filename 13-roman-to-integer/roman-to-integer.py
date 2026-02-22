class Solution:
    def romanToInt(self, s: str) -> int:
        num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
      
        res = 0
        previous = 0

        for char in reversed(s):
            current = num[char]

            if current < previous:
                res -= current
                
            else:
                res += current

            previous = current
            
        return res