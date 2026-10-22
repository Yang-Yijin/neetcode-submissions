class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for m in s:
            if m in pairs:
                if stack and stack[-1] == pairs[m]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(m)
        return not stack