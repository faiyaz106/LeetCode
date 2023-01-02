# https://leetcode.com/problems/implement-queue-using-stacks/description/

# 1st Solution: Time complexity: O(n), Space Complexity: O(n)
class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack1)==0:
            return
        if len(self.stack1)==1:
            return self.stack1.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        output=self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return output


    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack1)==0:
            return
        if len(self.stack1)==1:
            return self.stack1[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        output=self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return output

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1)==0:
            return True
        else:
            return False
        

# 2nd Solution: Time Complexity: O(1) Amortized and Space Complexity: O(n)
class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.top=None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack1 :
            self.top=x
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack2: 
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            return self.top
        else:
            return self.stack2[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2
 
        
