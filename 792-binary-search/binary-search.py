class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = round((len(nums))//2)
        if nums[mid] == target:
            return mid

        l = self.search(nums[:mid], target)
        if l != -1:
            return l
        
        r = self.search(nums[mid+1:], target)
        if r != -1:
            return mid + 1 + r
        return -1