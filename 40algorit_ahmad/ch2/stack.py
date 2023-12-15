class Stack:
    """
    A class object to represent a Stack. Abides by 
    LIFO/FILO.

    Attributes
    ----------
    stack : list
        Values of the Stack stored as a list
    
    Methods
    -------
    isEmpty():
        Checks to see if the stack is empty
    push(item):
        Push item onto the stack
    peek(item):
        See the element that would be returned if the pop()
        method is called
    pop():
        Returns the next element in the stack
    size():
        Return the size of the stack
    """
    def __init__(self):
        self.stack    = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.isEmpty(): return None
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
if __name__ == '__main__':
    stack = Stack()
    stack.push('Yellow')
    stack.push('Red')
    stack.push('Orange')
    stack.push('Green')

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())