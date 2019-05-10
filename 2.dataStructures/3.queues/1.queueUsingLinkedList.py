class node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
    
class queue:
    def __init__(self):
        self.start = None
        self.end = None

    def display(self):
        print("-------------------------------------------------")
        if self.start == None:
            print("cannot display : queue empty!")
            return
        else:
            tr = self.start
            while tr != None:
                print(tr.data)
                tr = tr.next

    def enqueue(self, value):
        temp = node(data=value)
        temp.prev = self.end
        if self.start == None and self.end == None:
            self.start = temp
            self.end = temp
        else:
            self.end.next = temp
            self.end = temp

    def dequeue(self):
        if self.start==None and self.end == None:
            print("cannot deque : queue empty!")
            return
        temp = self.end
        self.end = temp.prev
        self.end.next = None
        temp = None

# driver code

q = queue()
q.display()
q.enqueue(10)
q.display()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
q.dequeue()
q.dequeue()
q.display()