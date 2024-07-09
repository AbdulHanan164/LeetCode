from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # Move elements from q1 to q2 except the last one
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Pop the last element from q1
        top_element = self.q1.popleft()
        
        # Swap q1 and q2 to maintain the invariant
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # Move elements from q1 to q2 except the last one
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Get the last element without removing it
        top_element = self.q1[0]
        
        # Move the last element to q2
        self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2 to maintain the invariant
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0 and len(self.q2) == 0
