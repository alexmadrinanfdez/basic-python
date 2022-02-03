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
            old = self.head.next
            self.head.next = self.head.next.next
        # at the end (append)
        else:
            current = self.head
            # traverse the list
            while(current.next.next):
                current = current.next
            old = current.next
            current.next = current.next.next
        
        self._size -= 1
        return old.value
    
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
    
    def has_cycle(self):
        # Floyd’s cycle-finding algorithm
        try:
            slow_ptr = self.head
            fast_ptr = self.head
            while slow_ptr is not fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            return True
        except:
            return False
    
    def get_intersection(lla, llb):
        pa, pb = lla.head, llb.head
        while pa is not pb:
            # if either pointer hits the end
            # switch head and continue the second traversal
            pa = llb.head if not pa else pa.next
            pb = lla.head if not pb else pb.next
        # only 2 ways to get out of the loop 
        # they meet or they both hit the end = None
        return pa

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

    print("Does the linked list have a loop?", linkedList.has_cycle())
    # artificial loop
    linkedList.head.next.next.next.next = linkedList.head.next
    print("Can the new loop be detected?", linkedList.has_cycle())

    other_ll = LinkedList()
    other_ll.add(4)
    other_ll.add(5)
    other_ll.add(1)
    other_ll.head.next.next.next = linkedList.head
    intersec = LinkedList.get_intersection(linkedList, other_ll)
    print("Where is the intersection? At value", intersec.value)