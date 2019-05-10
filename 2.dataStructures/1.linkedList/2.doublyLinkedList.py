class node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
    
    def displayList(self):
        print("----------------------------------------------")
        if self.start == None:
            print("cannot display : list empty!")
        else:
            tr = self.start
            while tr != None:
                print(tr.data)
                tr = tr.next
    def displayListReverse(self):
        print("----------------------------------------------")
        if self.end == None:
            print("cannot display reverse: list empty!")
        else:
            tr = self.end
            while tr != None:
                print(tr.data)
                tr = tr.prev

    def insertAtStart(self, value):
        temp = node(value, self.start, None)
        if self.start == None:
            self.end = temp
        else:
            self.start.prev = temp
        self.start = temp

    def insertAtEnd(self, value):
        temp = node(value, None, self.end)
        if self.end == None:
            self.start = temp
        else:
            self.end.next = temp
        self.end = temp

dll = doublyLinkedList()
dll.displayList()
dll.insertAtStart(10)
dll.insertAtStart(20)
dll.insertAtStart(30)
dll.insertAtStart(40)
dll.displayList()
dll.displayListReverse()
