class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort list

        ans = [] # base case
        
        for x in range(len(nums) - 2): # 0 to y value
            y = x + 1 # start after x
            z = len(nums)-1 # end pointer for 2 pointer

            if x > 0 and nums[x] == nums[x-1]:
                continue

            while y < z: # while y is less than z
                total = nums[x] + nums[y] + nums[z] # calc total
                if total == 0: # if total is 0, append if not already in list
                    ans.append([nums[x], nums[y], nums[z]])
                    y += 1 # move y
                    z -= 1

                    # Skip duplicate y values
                    while y < z and nums[y] == nums[y - 1]:
                        y += 1

                    # Skip duplicate z values
                    while y < z and nums[z] == nums[z + 1]:
                        z -= 1
                    
                elif total > 0: # if total is too big, decrement z for smaller number
                    z -= 1
                else: # if total is too small, increment y
                    y += 1

        return ans