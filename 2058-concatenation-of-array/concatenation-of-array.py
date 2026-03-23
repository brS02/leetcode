class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        stop = len(nums)
        for i in range(stop):
            nums.append(nums[i])
        return nums