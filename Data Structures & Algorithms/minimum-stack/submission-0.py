class MinStack:

    def __init__(self):
        """
        Initializes the stack object.
        Each element in the stack will be a list/tuple: [val, current_min]
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.
        """
        if not self.stack:
            # If the stack is empty, the element itself is the minimum
            self.stack.append((val, val))
        else:
            # Compare the new value with the current minimum at the top of the stack
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """
        Gets the top element of the stack.
        """
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        """
        if self.stack:
            return self.stack[-1][1]
        return None

        
