class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-', '*','/']
        stack = []
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                right = stack.pop()
                left = stack.pop()
                if item == '+':
                    stack.append(left + right)
                elif item == '-':
                    stack.append(left - right)
                elif item == '*':
                    stack.append(left * right)
                elif item == '/' and right != 0:
                    stack.append(int(left / right))

        return stack.pop()
