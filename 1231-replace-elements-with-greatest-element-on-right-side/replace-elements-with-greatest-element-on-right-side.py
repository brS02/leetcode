class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i] # store num first
            arr[i] = maxNum # set last max to current place
            maxNum = max(temp, maxNum) # set new max num

        return arr