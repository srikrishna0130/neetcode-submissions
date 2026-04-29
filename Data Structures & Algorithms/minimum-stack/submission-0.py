class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []
        
    def push(self, val: int) -> None:
        self._stack.append(val)
        
        if (self._min_stack == []):
            self._min_stack.append(val)
            return None

        curr_min = self._min_stack[-1]
        self._min_stack.append(min(curr_min, val))

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()    
        return None  

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
        
