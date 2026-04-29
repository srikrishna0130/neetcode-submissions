class Solution:
    # assuming we're not encountering invalid states
    def evalRPN(self, tokens: List[str]) -> int:
        evaluate_stack = []
        operators = ['+', '-', '*', '/']

        for i in tokens:
            if i in operators:
                b = evaluate_stack.pop()
                a = evaluate_stack.pop()
                result = self.evaluate(int(a), int(b), i)
                evaluate_stack.append(int(result))
            else:
                evaluate_stack.append(int(i))
        
        return evaluate_stack[-1]
 
    def evaluate(self, a: int, b: int, operator: str) -> int:
        match operator:
            case '+':
                return a+b
            case '-':
                return a-b
            case '*':
                return a*b
            case '/':
                return a/b
            

        