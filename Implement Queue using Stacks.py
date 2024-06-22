class MyQueue(object):

    def __init__(self):
        self.input = []    # Stack to handle push operations
        self.output = []   # Stack to handle pop and peek operations

    def push(self, x):
        """
        Push element x to the back of the queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from the front of the queue and returns it.
        :rtype: int
        """
        self._transfer()
        return self.output.pop()

    def peek(self):
        """
        Returns the element at the front of the queue.
        :rtype: int
        """
        self._transfer()
        return self.output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.input and not self.output

    def _transfer(self):
        """
        Helper method to transfer elements from input stack to output stack if output stack is empty.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

# Example usage:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
