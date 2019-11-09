""" 
Stack Data Structure

"""

class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def peek(self):
        if not self.is_empty():
            return self.item[-1]

    def get_stack(self):
        return self.item

s = Stack()

(s.push('A'))
(s.push('B'))

print(s.get_stack())

print(s.peek())