import linked_list

class Stack(linked_list.LinkedList):
    def push(self, value):
        return self.add(value, start=True)
    
    def pop(self):
        return self.remove(start=True)

if(__name__ == "__main__"):
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack)

    print("Removing (in order):", stack.pop(), stack.pop())
    print(stack)