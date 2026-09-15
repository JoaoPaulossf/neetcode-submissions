class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            else:
                if not stack:
                    return False

                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False

                elif char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False

                elif char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            
        return len(stack) == 0