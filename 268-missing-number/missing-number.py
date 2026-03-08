class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums) # sumsshould equal, otherwise returns missing number (difference)
