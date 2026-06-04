class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if numbers:
            x = 0 # lower bound
            y = len(numbers)-1 #upper bound

            while x < y:
                total = numbers[x] + numbers[y]

                if total == target: # if lower and upper index = target, return
                    return [x+1, y+1]

                elif total > target: # if sum too big, decrement upper limit
                    y -= 1
                
                else: # if sum too small, incremement lower bound
                    x += 1

        return []