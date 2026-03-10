class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for operation in operations:
            if operation == "++X":
                ans += 1
            if operation == "X++":
                ans += 1
            if operation == "X--": 
                ans -= 1
            if operation == "--X":
                ans -= 1
        return ans