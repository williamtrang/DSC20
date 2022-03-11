"""
DSC 20 HW10 Utility File
Please copy and paste your Stack and Queue implementation from Lab 10.
"""

class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """
        # YOUR CODE GOES HERE #
        self.items = ...
        self.num_items = ...

    def size(self):
        """ Get the number of items stored. """
        # YOUR CODE GOES HERE #
        return ...

    def is_empty(self):
        """ Check whether the collection is empty. """
        # YOUR CODE GOES HERE #
        return ...

    def clear(self):
        """ Remove all items in the collection. """
        # YOUR CODE GOES HERE #


class Stack(Collection):
    """
    Stack class.
    """

    def push(self, item):
        """ Push `item` to the stack. """
        # YOUR CODE GOES HERE #

    def pop(self):
        """ Pop the top item from the stack. """
        # YOUR CODE GOES HERE #
        return ...

    def peek(self):
        """ Peek the top item. """
        # YOUR CODE GOES HERE #
        return ...

    def __str__(self):
        """ Return the string representation of the stack. """
        # YOUR CODE GOES HERE #
        return ...


class Queue(Collection):
    """
    Queue class.
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        # YOUR CODE GOES HERE #

    def dequeue(self):
        """ Dequeue the front item from the queue. """
        # YOUR CODE GOES HERE #
        return ...

    def peek(self):
        """ Peek the front item. """
        # YOUR CODE GOES HERE #
        return ...

    def __str__(self):
        """ Return the string representation of the queue. """
        # YOUR CODE GOES HERE #
        return ...
