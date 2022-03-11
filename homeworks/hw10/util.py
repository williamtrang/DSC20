"""
DSC 20 Lab 10
Name: William Trang
PID:  A16679845
"""

# Question 1.1
class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """
        self.items = []
        self.num_items = 0

    def size(self):
        """ Get the number of items stored. """
        return self.num_items

    def is_empty(self):
        """ Check whether the collection is empty. """
        if self.size() == 0:
            return True
        return False

    def clear(self):
        """ Remove all items in the collection. """
        self.items = []
        self.num_items = 0


# Question 1.2
class Stack(Collection):
    """
    Stack class.

    >>> stk = Stack()
    >>> stk.size()
    0
    >>> stk.is_empty()
    True
    >>> str(stk)
    '(bottom) (top)'
    >>> stk.push(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> stk.push('LAB 10')
    >>> stk.size()
    1
    >>> stk.is_empty()
    False
    >>> stk.push('DSC')
    >>> stk.push(20)
    >>> stk.size()
    3
    >>> str(stk)
    '(bottom) LAB 10 -- DSC -- 20 (top)'
    >>> stk.pop()
    20
    >>> stk.pop()
    'DSC'
    >>> stk.peek()
    'LAB 10'
    >>> stk.size()
    1
    >>> stk.clear()
    >>> stk.pop()
    >>> stk.peek()
    """

    def push(self, item):
        """ Push `item` to the stack. """
        if item == None:
            raise ValueError('item cannot be None')
        self.items.append(item)
        self.num_items += 1

    def pop(self):
        """ Pop the top item from the stack. """
        if self.size() == 0:
            return None
        item = self.items[self.size() - 1]
        self.items.pop(self.size() - 1)
        self.num_items -= 1
        return item

    def peek(self):
        """ Peek the top item. """
        if self.size() == 0:
            return None
        return self.items[self.size() - 1]

    def __str__(self):
        """ Return the string representation of the stack. """
        string = '(bottom) '
        for val, item in enumerate(self.items):
            if val == self.size() - 1:
                string += str(item) + ' '
            else:
                string += str(item) + ' -- '
        return string + '(top)'


# Question 1.3
class Queue(Collection):
    """
    Queue class.

    >>> que = Queue()
    >>> que.size()
    0
    >>> que.is_empty()
    True
    >>> str(que)
    '(front) (rear)'
    >>> que.enqueue(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> que.enqueue('LAB 10')
    >>> que.size()
    1
    >>> que.is_empty()
    False
    >>> que.enqueue('DSC')
    >>> que.enqueue(20)
    >>> que.size()
    3
    >>> str(que)
    '(front) LAB 10 -- DSC -- 20 (rear)'
    >>> que.dequeue()
    'LAB 10'
    >>> que.dequeue()
    'DSC'
    >>> que.peek()
    20
    >>> que.size()
    1
    >>> que.clear()
    >>> que.dequeue()
    >>> que.peek()
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        if item == None:
            raise ValueError('item cannot be None')
        self.items.append(item)
        self.num_items += 1

    def dequeue(self):
        """ Dequeue the front item from the queue. """
        if self.size() == 0:
            return None
        item = self.items[0]
        self.items.pop(0)
        self.num_items -= 1
        return item

    def peek(self):
        """ Peek the front item. """
        if self.size() == 0:
            return None
        return self.items[0]

    def __str__(self):
        """ Return the string representation of the queue. """
        string = '(front) '
        for val, item in enumerate(self.items):
            if val == self.size() - 1:
                string += str(item) + ' '
            else:
                string += str(item) + ' -- '
        return string + '(rear)'
