class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self._size = 0
    
    def __str__(self):
        current = self.head
        out = str()
        # traverse the list
        while(current):
            out += str(current.value) + " -> "
            current = current.next
        return out
    
    def size(self):
        return self._size
    
    def add(self, value, start=True):
        # at the beginnning (push)
        if(start):
            old = self.head.next
            self.head.next = Node(value)
            self.head.next.next = old
        # at the end (append)
        else:
            current = self.head
            # traverse the list
            while(current.next):
                current = current.next
            current.next = Node(value)
        
        self._size += 1
    
    def remove(self, start=True):
        assert(self.size() > 0)
        # at the beginnning (push)
        if(start):
            self.head.next = self.head.next.next
        # at the end (append)
        else:
            current = self.head
            # traverse the list
            while(current.next.next):
                current = current.next
            current.next = current.next.next
        
        self._size -= 1
    
    def reverse(self):
        # keep track of the current, previous and posterior nodes
        curr = self.head.next
        prev = None
        while(curr):
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        # update the head of the list to point to the first node
        self.head.next = prev

if __name__ == "__main__":
    linkedList = LinkedList()

    for i in range(1, 6):
        linkedList.add(i)
    print(linkedList)

    linkedList.remove(start=True)
    linkedList.remove(start=False)
    print(linkedList)

    for i in range(6, 10):
        linkedList.add(i, start=False)
    print(linkedList)

    linkedList.reverse()
    print(linkedList)