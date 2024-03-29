class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.x=None
        self.next=None

    def push(self, x: int) -> None:
        j=self
        if j.x == None:
            j.x = x
        elif j.x != None:
            while j.next!=None:
                j=j.next
            j.next=MinStack()
            j.next.x=x

    def pop(self) -> None:
        j=self
        if j.next == None and j.x != None:
            j.x = None
        elif j.next != None:
            while j.next != None:
                n=j
                j=j.next
            n.next = None

    def top(self) -> int:
        
        if self.next == None and self.x != None:
            return self.x
        elif j.next != None:
            j = self
            while j.next != None:
                j=j.next
            return j.x

    def getMin(self) -> int:
        j = self
        i = self.x
        if j.next == None and j.x != None:
            return j.x
        elif j.next != None:
            while j.next != None:
                j = j.next
                if j.x < i:
                    i=j.x
            return i


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
