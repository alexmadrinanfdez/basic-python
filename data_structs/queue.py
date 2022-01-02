from linked_list import Node

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self._size = 0
    
    def items(self):
        lst = []
        current = self.head.next
        while(current):
            lst.append(current.value)
            current = current.next
        return lst
    
    def size(self):
        return self._size
    
    def empty(self):
        return self.size() == 0
    
    def enqueue(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self._size += 1
    
    def dequeue(self):
        if(self.empty()):
            print("Can't remove from an empty queue!")
        else:
            old = self.head.next
            self.head.next = self.head.next.next
            self._size -= 1
            # edge case (with one item)
            if(self.empty()):
                self.tail = self.head

            return old.value

if __name__ == "__main__":
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    print(queue.items())
    
    while queue.empty() == False:
        print(queue.dequeue())
    # try to remove from an empty queue
    queue.dequeue()