class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = []
        for x in tokens:
            if x in ['+','-','*','/']:
                r = n.pop()
                l = n.pop()
                if x == '+':
                    result = l + r
                elif x == '-':
                    result = l - r
                elif x == '*':
                    result = l * r
                elif x == '/':
                    result = int(l / r)
                n.append(result)

            else:
                n.append(int(x))
        return n.pop()