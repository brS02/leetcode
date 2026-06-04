class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []

        if numbers:
            x = 0 # lower bound
            y = len(numbers)-1 #upper bound

            while x < y:
                if (numbers[x] + numbers[y]) == target: # if lower and upper index = target, return
                    ans.append(x + 1)
                    ans.append(y + 1)
                    break

                elif (numbers[x] + numbers[y]) > target: # if sum too big, decrement upper limit
                    y -= 1
                
                else: # if sum too small, incremement lower bound
                    x += 1

        return ans