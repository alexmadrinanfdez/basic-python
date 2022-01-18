class PriorityQueue:
    def __init__(self):
        self.arr = [None]
    
    def __str__(self):
        return str(self.arr)
    
    def _swim(self):
        i = len(self.arr) - 1
        # parent - i // 2
        while (i // 2 > 0) and (self.arr[i // 2] < self.arr[i]):
            # swap current index with its parent
            self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]
            i //= 2

    def _sink(self):
        i = 1
        # left child  - i * 2
        # right child - i * 2 + 1
        while i * 2 < len(self.arr):
            p = self.arr[i]
            l = self.arr[i * 2]
            if i * 2 + 1 < len(self.arr):
                r = self.arr[i * 2 + 1]
            else:
                r = float("-inf")
            # swap current index with either child
            if p < l:
                p, l = l, p
            elif p < r: 
                p, r = r, p
            # heap-ordered
            else:
                return

    def empty(self):
        return len(arr) == 1

    def size(self):
        return len(arr) - 2
    
    def insert(self, key):
        self.arr.append(key)
        self._swim()

    def get_max(self):
        assert not self.empty()
        return self.arr[1]

    def del_max(self):
        assert not self.empty()
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        self._sink()
        return self.arr.pop()

if __name__ == "__main__":
    from random import randint

    # worst case
    pq = PriorityQueue()
    arr = []
    for i in range(10):
        arr.append(i)
        pq.insert(i)
    print(arr, "->", pq)
    # random case
    pq = PriorityQueue()
    arr = []
    for i in range(10):
        r = randint(0, 9)
        arr.append(r)
        pq.insert(r)
    print(arr, "->", pq)