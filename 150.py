class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in range(len(tokens)):
            if(tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/"):
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if(tokens[i] == "+"):
                    stack.append(num1 + num2)
                elif(tokens[i] == "-"):
                    stack.append(num1 - num2)
                elif(tokens[i] == "*"):
                    stack.append(num1 * num2)
                elif(tokens[i] == "/"):
                    res = abs(num1) // abs(num2)
                    if (num1 < 0) ^ (num2 < 0):  # XOR for different signs
                        res = -res
                    stack.append(res)
            else:
                stack.append(tokens[i])

        return int(stack[0])