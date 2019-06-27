class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class singlyLinkedList:
    def __init__(self):
        self.start = None
    
    def displayList(self):
        print("-----------------------------------------")
        if self.start == None:
            print("cannot display : List empty!")
        else:
            tracer = self.start
            while tracer != None:
                print(tracer.data)
                tracer = tracer.next

    def insertAtStart(self, value):
        temp = node(value, self.start)
        self.start = temp

    def deleteFromStart(self):
        if self.start == None:
            print("cannot delete : list empty!")
        else:
            temp = self.start
            self.start = temp.next
            temp = None

    def insertAtEnd(self, value):
        temp = node(value)
        if self.start == None:
            temp.next = self.start
            self.start = temp
        else:
            tracer = self.start
            while tracer.next != None:
                tracer = tracer.next
            tracer.next = temp
    
    def deleteFromEnd(self):
        if self.start == None:
            print("cannot delete : list empty!")
        else:
            tr = self.start
            while (tr.next).next != None:
                tr = tr.next
            tr.next = None

#driver code


sll = singlyLinkedList()
sll.displayList()
sll.insertAtStart(10)
sll.insertAtStart(20)
sll.insertAtStart(30)
sll.displayList()
sll.insertAtEnd(40)
sll.displayList()
sll.deleteFromEnd()
sll.displayList()
sll.deleteFromStart()
sll.displayList()