class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value_stack = []
        for token in tokens:
            if token not in ['+', '-', '/', '*']:
                value_stack.append(int(token))
            else:
                if len(value_stack) < 2:
                    return None
                else:
                    val2 = value_stack.pop(-1)
                    val1 = value_stack.pop(-1)
                    if token == '+':
                        res = val1 + val2
                    elif token == '-':
                        res = val1 - val2
                    elif token == '*':
                        res = val1 * val2
                    elif token == '/':
                        res = int(val1 / val2)
                    value_stack.append(res)
        return value_stack[0]