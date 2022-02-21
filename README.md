# basic-python

Basic (and **not** so basic) examples of the `Python` programming language.
Modified from these tutorials:
- [x] [Python Software Foundation](https://docs.python.org/3/tutorial/index.html)
- [x] [Programiz](https://www.programiz.com/python-programming)
- [x] [W3Schools](https://www.w3schools.com/python/default.asp)
- [x] [Brilliant](https://brilliant.org)
- [ ] [LeetCode](https://leetcode.com)
- [ ] [Techie Delight](https://www.techiedelight.com)
- [ ] [GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language)
- [ ] [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python)

and others...

## Structure

- `intro`
    + `hello.py`: a must in every programming language.
    + `ascii.py`: accepts as input an integer given by the user and transforms it to an ASCII character.
    + `reverse_number.py`: swaps the order of the digits of a number provided by the user.
    + `prime_number.py`: checks if a given number is a prime number.
- `oop`
    + `card_deck.py`: exemplifies Object Oriented Programming defining the classes `Card` and `Deck` to represent a deck of cards.
    + `stopwatch.py`: start and stop watch that measures time since its creation.
- `data_structs`
    + `linked_list.py`: implementation of a linked list, a list where each element (`Node`) points to the next. Includes a reverse method and loop detection.
    + `stack.py`: implementation of a stack. Stacks are linked lists which can only operate (add/remove) from the top of the list.
    + `queue.py`: implementation of a queue. Also similar to a linked list, the class has been optimized to have constant runtime operations and so it does not inherit directly from the `LinkedList` class.
    + `hashmap.py`: implementation of a hash map. Stores key-value pairs through a hash function and handles collisions through separate chaining.
    + `deque.py`: doubly ended queue. This means it allows addition and removal from both, the front and the back of the queue.
    + `trie.py`: implementation of a trie, efficient storage for words that can have additional functionality when the prefix of the word is important.
    + `bst.py`: implementation of a binary search tree. Similar to a binary tree, but with ordered children, which allows for efficient operations. Each node has two children.
    + `graph.py`: implementation of a graph without explicitly implementing the nodes. It is defined as a set of relationships.
    + `heap.py`: implementation of a priority queue through a binary heap. Similar to a binary tree, but the parents have higher priority than the children.
- `algos`
    + `complexity.py`: basic analysis of common orders of growth.
    + `sort`
        * `select_sort.py`: selection sort iteratively searches for the minimum non-sorted element and puts it at the end of the sorted array.
        * `insert_sort.py`: insertion sort selects the next element in the list and adds it (in the correct order) into the ordered list.
        * `merge_sort.py`: the **mergesort** algorithm works by dividing the list to order in halves recursively until we end up with single elements. Afterwards, it sorts in a _bottom-up_ manner each half by merging while respecting order.
        * `quick_sort.py`: **quicksort** recursively orders partitions of arbitrary length until every element is sorted.
        * `string_sort.py`: because the number of characters in the alphabet is limited, sorting a string of characters can be made more efficient than general sorting.
        * `heap_sort.py`: the binary heap structure can be used to efficiently sort an array.
    + `search`
        * `string`: different pattern matching algorithms.
        * `binary_search`: the binary search algorithm divides the list in halves recursively to search for a given element.
- `problems`
    + `valid_parenthesis.py`: checks a given string to see if the use of parenthesis is correct. Parenthesis include the following characters: _(_, _)_, _[_, _]_, _{_ and _}_. The string can contain other any character.
    + `sum_subarray.py`: problems involving sums of sub-arrays. A sub-array  is a **contiguous** part of an array.
    + `fibonacci.py`: computes the Fibonacci series. With and without recursion.
    + `pascal.py`: computes the Pascal triangle. Its first row is numbered as zero. With and without recursion.
    + `unique_paths.py`: returns the total number of paths that, starting from the top left square of a given grid (which can include obstacles), lead to the bottom right square.
    + `egg_dropping.py`: class of problems in which it is important to find the correct response without exceeding a (low) number of certain failure states.
    + `roman_numeral.py`: translates from roman numbers to alphanumeric integers.
    + `count_primes.py`: returns the number of prime numbers that are strictly less than a given integer.
    + `string`
        * `palindrome.py`: checks if a string, which can contain any character, is a palindrome. A string is a palindrome if the first half of the string is equal to the second half.
        * `isomorphic.py`: checks if two strings are isomorphic. Two strings are isomorphic if characters in one of them can be replaced to get the other.
        * `anagram.py`: checks if two strings are anagrams. Two strings are anagrams if characters in one of them can be rearranged to get the other.
    + `combinatorial`
        * `subsets.py`: returns every possible subset of a list of elements. With and without considering duplicate elements.
        * `permutations.py`: returns every possible permutation of elements in an array.
- `bit`
    + `basic.py`: miscellaneous, simple and useful bit-wise operations.
    + `kth_bit.py`: operations with the k'th bit.
    + `rightmost_set.py`: problems related with the first (rightmost) bit set to one.
    + `letters.py`: bit-wise operations with letters. They require explicit conversion (in `Python`).