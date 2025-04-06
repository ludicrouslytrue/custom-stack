
#Divyam Agrawal, 24BIT0423

class TheStackOfAllTime:
    def __init__(self):
        self.stack = [] # Makes stack, exists outside of the function
        self.min_stack = [] # Makes min_stack, exists outside of the function
        self.max_stack = [] # Makes max_stack, exists outside of the function

    def push(self, x):
        self.stack.append(x) # Append x to stack, basically push x to stack

        if not self.min_stack:
            self.min_stack.append(x) # If empty, append the current element
        elif x <= self.min_stack[-1]:
            self.min_stack.append(x) # If the current element is <= the top of min_stack, append it
        else:
            self.min_stack.append(self.min_stack[-1]) # Otherwise, append the current top of min_stack again to maintain the minimum


        if not self.max_stack:
            self.max_stack.append(x) # If empty, append the current element
        elif x >= self.max_stack[-1]:
            self.max_stack.append(x) # If the current element is >= the top of max_stack, append it
        else:
            self.max_stack.append(self.max_stack[-1]) # Otherwise, append the current top of max_stack again to maintain the maximum


    def pop(self):
        if not self.stack:
            return "Error! Stack is empty." # If stack is empty, return error
        self.stack.pop()
        self.min_stack.pop() 
        self.max_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else "Error! Stack is empty." # Return the top of stack

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else "Error! Stack is empty." # Return the top of min_stack, which is the minimum

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else "Error! Stack is empty." # Return the top of max_stack, which is the maximum

# Example Usage:
stack = TheStackOfAllTime()
stack.push(5) # Append to stack, min_stack and max_stack
stack.push(2) # Append to stack, min_stack and max_stack
stack.push(8) # Append to stack, min_stack and max_stack
stack.push(1) # Append to stack, min_stack and max_stack
print("Top:", stack.top()) # Should give 1
print("Min:", stack.getMin()) # Should give 1
print("Max:", stack.getMax()) # Should give 8
stack.pop() # Should pop 1
print("Min after pop:", stack.getMin()) # Should give 2, since 1 is popped
print("Max after pop:", stack.getMax()) # Should give 8, since 1 is popped
print("Top after pop:", stack.top()) # Should give 8, since 1 is popped
