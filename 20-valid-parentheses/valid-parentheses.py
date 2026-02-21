class Solution:
    def isValid(self, s: str) -> bool:
        chars = []
        
        for char in s:
            if char in "({[":
                chars.append(char)
            else:
                if not chars:
                    return False
                if char == ")" and chars[-1] != "(":
                    return False
                if char == "}" and chars[-1] != "{":
                    return False
                if char == "]" and chars[-1] != "[":
                    return False
                chars.pop()
        return len(chars) == 0