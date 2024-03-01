class Node:
    def __init__(self, value):
        self. value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        height = self.height()
        length = 2**height - 1
        # empty canvas
        out = [[' ' for _ in range(length)] for _ in range(height)]
        # draw the nodes
        self._helper_print(self.root, 0, 0, length-1, out)
        # array -> string
        str_out = ''
        for row in out:
            for c in row:
                str_out += c
            str_out += '\n'
        return str_out

    def _helper_print(self, curr, height, lo, hi, out):
        if not curr:
            return
        mid = (lo + hi) // 2
        out[height][mid] = str(curr.value)
        self._helper_print(curr.left, height+1, lo, mid-1, out)
        self._helper_print(curr.right, height+1, mid+1, hi, out)

    def _height(self, curr):
        if not curr:
            return 0
        return max(self._height(curr.left), self._height(curr.right)) + 1

    def height(self):
        return self._height(self.root)

    def _insert(self, value, curr):
        if not curr:
            return Node(value)
        if curr.value > value:
            curr.left = self._insert(value, curr.left)
        elif curr.value < value:
            curr.right = self._insert(value, curr.right)
        # do not modify the tree if there is a match
        return curr

    def insert(self, value):
        # update every traversed node
        self.root = self._insert(value, self.root)

    def _get(self, value, curr):
        if not curr:
            return False
        elif curr.value == value:
            return True
        elif curr.value > value:
            return self._get(value, curr.left)
        else:
            return self._get(value, curr.right)

    def get(self, value):
        return self._get(value, self.root)

    def _substitute(self, curr, lt):
        # either find largest element in left subtree...
        if lt:
            while curr.right:
                curr = curr.right
        # ...or smallest in right subtree.
        else:
            while curr.left:
                curr = curr.left
        
        return curr
        
    def _delete(self, value, curr):
        if not curr:
            raise ValueError("The node is not present in the tree.")
        elif curr.value > value:
            curr.left = self._delete(value, curr.left)
        elif curr.value < value:
            curr.right = self._delete(value, curr.right)
        # find the node and...
        else:
            #  ...has no children
            if not curr.left and not curr.right:
                return None
            # ...has both children
            elif curr.left and curr.right:
                sub = self._substitute(curr.left, lt=True)
                curr.left = self._delete(sub.value, curr.left)
                # another valid solution (changes the tree)
                # sub = self._substitute(curr.right, lt=False)
                # curr.right = self._delete(sub.value, curr.right)
                # replace current node with its substitute
                sub.left = curr.left
                sub.right = curr.right
                return sub
            # ...has only one child
            else:
                if curr.left:
                    return curr.left
                else:
                    return curr.right
        # in case the node is not found, return current node
        return curr

    def delete(self, value):
        # update every traversed node
        self.root = self._delete(value, self.root)

    def _traversal(self, curr):
        if not curr:
            return
        # in-order traversal (left, current, right)
        self._traversal(curr.left)
        print(curr.value, end=' ')
        self._traversal(curr.right)

    def traversal(self):
        return self._traversal(self.root)

    def _invert(self, node):
        if node:
            node.left, node.right = \
                self._invert(node.right), self._invert(node.left)
            return node

    def invert(self):
        self._invert(self.root)

    def _trim(self, node, lo, hi):
        if node:
            if node.value < lo:
                return self._trim(node.right, lo, hi)
            if node.value > hi:
                return self._trim(node.left, lo, hi)
            node.left = self._trim(node.left, lo, hi)
            node.right = self._trim(node.right, lo, hi)
        return node
    
    def trim(self, lo: int, hi: int):
        if hi < lo:
            raise ValueError("The upper limit is smaller than the lower!")
        self._trim(self.root, lo, hi)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(2)
    bst.insert(4)
    bst.insert(8)
    bst.insert(6)
    bst.insert(9)
    print(bst)
    print("Is 4 in the tree?", bst.get(4))
    print("Is 7 in the tree?", bst.get(7))
    print("Is 8 in the tree?", bst.get(8), end="\n\n")
    bst.trim(3, 6)
    bst.insert(7)
    print(bst)
    print("Is 8 still in the tree?", bst.get(8))
    print("Is 7 now in the tree?", bst.get(7))
    print("The height of the tree is", bst.height())
    print("Tree inversion results in a non-search tree:", end="\n\n")
    bst.invert()
    print(bst)
    bst.invert() # invert again to keep properties
    print("The nodes in order are:", end=' ')
    bst.traversal()
    print("\nDeleting the root of the tree:", end="\n\n")
    bst.delete(5)
    print(bst)