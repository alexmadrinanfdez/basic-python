class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self._size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def size(self):
        return self._size

    def empty(self):
        return self.size() == 0

    def add_front(self, value):
        new = Node(value)
        old = self.head.next

        self.head.next.prev = new
        self.head.next = new
        new.prev = self.head
        new.next = old

        self._size += 1

    def add_back(self, value):
        new = Node(value)
        old = self.tail.prev

        self.tail.prev.next = new
        self.tail.prev = new
        new.prev = old
        new.next = self.tail

        self._size += 1

    def rm_front(self):
        if self.empty():
            print("Can't remove from an empty queue!")
        else:
            old = self.head.next

            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next

            self._size -= 1
            return old.value

    def rm_back(self):
        if self.empty():
            print("Can't remove from an empty queue!")
        else:
            old = self.tail.prev

            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev

            self._size -= 1
            return old.value
    
    def items(self):
        lst = []
        current = self.head.next
        while(current.next):
            lst.append(current.value)
            current = current.next
        return lst

if __name__ == '__main__':
    dq = Deque()
    for i in range(5):
        dq.add_front(i)
    for i in range(5, 10):
        dq.add_back(i)
    print(dq.items())

    dq.rm_front()
    print(dq.items())
    dq.rm_back()
    print(dq.items())