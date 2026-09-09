class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set() # window

        # go through list
        for i, num in enumerate(nums):

            # if 2 numbers in window, return true
            if num in seen:
                return True
            
            # add number to window if not in it
            seen.add(num)

            # if window is too big, remove firist number
            if len(seen) > k:
                seen.remove(nums[i - k])

        # no pairs in window
        return False