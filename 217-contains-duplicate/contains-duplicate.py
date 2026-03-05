class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()

        for val in nums:
            if val not in dupSet:
                dupSet.add(val)
            else:
                return True

        return False