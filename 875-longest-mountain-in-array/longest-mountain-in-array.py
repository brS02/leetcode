class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        # Stores the maximum mountain length found
        ans = 0

        # Iterate through possible mountain peaks
        # A peak cannot be the first or last element
        for i in range(1, len(arr) - 1):

            # Check if current element is a valid peak
            if arr[i - 1] < arr[i] > arr[i + 1]:

                # Start expanding from the peak
                l = i
                r = i

                # Move left while the sequence is strictly increasing
                # (walking down the mountain toward its left boundary)
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1

                # Move right while the sequence is strictly decreasing
                # (walking down the mountain toward its right boundary)
                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1

                # Update the longest mountain length
                ans = max(ans, r - l + 1)

        return ans