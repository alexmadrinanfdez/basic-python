# helper linked list class to handle collisions
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    # initializes an emtpy hash map
    def __init__(self, capacity):
        self.cap = capacity
        self.map = [Node(None, None) for _ in range(self.cap)]

    # overrides toString method for representation
    def __str__(self):
        out = ""
        for idx in range(self.cap):
            curr = self.map[idx]
            while(curr.next):
                out += str(curr.next.key) + ':' + str(curr.next.value) + " -> "
                curr = curr.next
            out += '\n'
        return out

    # private function to compute an integer hash value for a given key
    def _hash(self, key):
        return key % self.cap

    # given a key, will return the value associated with that key if it’s in the table
    # this function will return None if the key is not in the hash map
    def get(self, key): 
        idx = self._hash(key)
        curr = self.map[idx]
        while(curr.next):
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next

    # inserts the key-value pair into the hashmap
    # if the key already exists it will overwrite the previous value with the new value
    # performs separate chaining, in case there is a collision between different keys
    def put(self, key, value):
        idx = self._hash(key)
        curr = self.map[idx]
        while(curr.next):
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = Node(key, value)

    # removes a key and its associated value from the hashmap
    def delete(self, key):
        idx = self._hash(key)
        prev = self.map[idx]
        curr = prev
        while(curr.next):
            curr = curr.next
            if curr.key == key:
                prev.next = curr.next
            prev = curr

    # returns true if it contains the key
    def contains(self, key):
        return bool(self.get(key))

if __name__ == '__main__':
    map = HashMap(3)

    for i in range(10):
        map.put(i, i*2)
    print(map)

    print(map.get(4))

    for i in range(3):
        map.delete(i)
    print(map)

    print(map.contains(2))
    print(map.contains(4))