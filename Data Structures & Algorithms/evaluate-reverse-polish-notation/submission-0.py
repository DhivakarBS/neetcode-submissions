class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        # token={"}":"{",")":"(","[":']'}
        for ch in tokens:
            if ch in {"+","-","*","/"}:
                b=stack.pop()
                # print(type(b))
                a=stack.pop()
                # print(type(a))

                if ch=="+":
                    stack.append(a + b)
                elif ch=="-":
                    stack.append(a-b)
                elif ch=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(float(a)/b))
            else:
                stack.append(int(ch))
                print(stack)
        return stack[-1]