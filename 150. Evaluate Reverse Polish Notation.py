class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def executeOperator(num1: int, num2: int, operator: str) -> int:
            print("operating", num1, operator, num2)
            result = 0
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = int(num1 / num2)

            return result

        operators = {"+", "-", "*", "/"}
        stack = []
        res = 0

        if len(tokens) == 1 and tokens[0] not in operators:
            return int(tokens[0])

        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = executeOperator(num1, num2, t)
                stack.append(res)

        return res
