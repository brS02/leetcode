class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in nums and nums.index(ans) != i:
                j = nums.index(ans)
                return [i, j] 