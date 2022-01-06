# basic-python

Basic (and **not** so basic) examples of the `Python` programming language.
Modified from these tutorials:
- [x] [Python Software Foundation](https://docs.python.org/3/tutorial/index.html)
- [x] [Programiz](https://www.programiz.com/python-programming)
- [x] [W3Schools](https://www.w3schools.com/python/default.asp)
- [ ] [LeetCode](https://leetcode.com/)
- [ ] [GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/)
- [ ] [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

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
- `algos`
    + `complexity.py`: basic analysis of common orders of growth.
- `problems`
    + `valid_parenthesis.py`: checks a given string to see if the use of parenthesis is correct. Parenthesis include the following characters: _(_, _)_, _[_, _]_, _{_ and _}_. The string can contain other any character.
    + `sum_subarray.py`: returns the number of contiguous subarrays that sum up less than the target.