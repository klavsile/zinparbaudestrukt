class Node:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def is_empty(self):
        return self.height == 0

    def push(self, value, position):
        new_node = Node(value, position)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp

def balancets(s):
    stack = Stack()
    brackets_open = ['(', '{', '[']
    brackets_closed = [')', '}', ']']
    brackets_map = {')': '(', '}': '{', ']': '['}

    for i in range(len(s)):
        if s[i] in brackets_open:
            stack.push(s[i], i)
        elif s[i] in brackets_closed:
            if stack.top != None:
                if stack.top.value == brackets_map[s[i]]:
                    stack.pop()
                else:
                    return i+1
            else:
                return i+1
    if stack.height != 0:
        temp = stack.top
        while temp.next != None:
            temp = temp.next
        return temp.position+1
    
    return "Success"

s = input("Ievadiet rindu: ")
print(balancets(s))