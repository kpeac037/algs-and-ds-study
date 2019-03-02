class Stack:
    # Every textbook says something along the lines of "A stack is a
    # first-in-last-out data structure".
    # You put some stuff in by PUSHing it, and you remove that stuff
    # by POPping it. If you don't wish to change the underlying data,
    # and only want to take a look at the top element, you can PEEK
    # at the Stack instead
    def __init__(self):
        self.items = []    # The underlying data is held in an array
        self.count = 0     # We'll also track count

    # Add an ITEM to the top of our stack
    def push(self, item):
        self.items.append(item)
        self.count += 1

    # Remove an item from the top of our stack.
    # If there is nothing to remove, self.items[-1] will throw an error.
    # However we can catch it with a try/except block.
    # I believe it is approriate to return None (easy to test for in
    # boolean statements). But I know many people would argue with me
    # about that, and insist an error must be thrown.
    def pop(self):
        try:
            a = self.items[-1]  #array[-1] returns the last element
            self.count -= 1
            self.items = self.items[:-1] #[array:-1] returns everything
            return a                     #BUT the last element
        except:
            return None

    def peek(self):
        try:
            a = self.items[-1]
            return a
        except:
            return None


def test():
    a = Stack()
    a.push(4)
    a.push(5)
    a.push(6)
    
    item = a.pop()
    while(item):
        print(item)
        item = a.pop()
    print("Done")
    
