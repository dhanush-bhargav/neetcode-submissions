class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        for c in s:
            if c in ['{', '[', '(']:
                parentheses_stack.append(c)
            else:
                if len(parentheses_stack) == 0:
                    return False
                else:
                    temp = parentheses_stack.pop(-1)
                    if (c == ')') and (temp != '('):
                        return False
                    if (c == ']') and (temp != '['):
                        return False
                    if (c == '}') and (temp != '{'):
                        return False
        if len(parentheses_stack) == 0:
            return True
        else:
            return False