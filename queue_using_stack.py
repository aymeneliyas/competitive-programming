class MyQueue(object):

    def __init__(self):
        self.arr = []
        self.arr2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.arr:
            self.arr2.append(self.arr.pop())
        self.arr.append(x)
        while self.arr2:
            self.arr.append(self.arr2.pop())
    def pop(self):
        """
        :rtype: int
        """
        return self.arr.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.arr
        
