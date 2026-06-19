class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "-", "/"]
        for token in tokens:
            if not token in operators:
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(second + first)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(second * first)
                elif token == "/":
                    stack.append(int(second / first))
        return stack[-1]