class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ansHash = {}

        for i, num in enumerate(nums):
            j = target - num
            if j in ansHash:
                return [i, ansHash[j]]
            ansHash[num] = i