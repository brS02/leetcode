class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        currentMax = 0
        for num in nums:
            if num == 1:
                currentMax += 1
                res = max(currentMax, res)
            else:
                currentMax = 0

        return res