class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i, num in enumerate(nums):
            # if num is in window already return true
            if num in seen:
                return True
            
            # otherwise append it for future use
            seen.add(num)

            # if length of window is too big, remove frist element
            if len(seen) > k:
                seen.remove(nums[i - k])

        # no dup found
        return False