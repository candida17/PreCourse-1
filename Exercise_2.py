#Time Complexity - O(1)
#Space Complexity- O(n)

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.top = None #points to top of stack
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node  #new node becomes top
        
    def pop(self):
        if self.top is None  #check if the stack is empty
            return None
        popped_node = self.top
        self.top = self.top.next #move top pointer to down in stack
        return popped_node.data
        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
