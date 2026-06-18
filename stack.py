class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        character = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in character:
                if stack and stack[-1] == character[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack == []:
            return True 
        else:
            return False  