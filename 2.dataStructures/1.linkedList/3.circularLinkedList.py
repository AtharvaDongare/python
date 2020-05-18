class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class circularLinkedList:
    def __init__(self):
        self.start = None
    
    def display(self):
        print("-------------------------------------------------------")
        if self.start == None:
            print("cannot display : list empty !!!")
        else:
            tr = self.start
            while (True):
                print(tr.data)
                if tr.next == self.start:
                    break
                tr = tr.next
    
    def insertAtStart(self, data):
        temp = Node(data, self.start)
        if self.start == None:
            temp.next = temp
        else:
            tr = self.start
            while tr.next != self.start:
                tr = tr.next
            tr.next = temp
        self.start = temp
    
    # def insertAtEnd(self, data):
    #     temp = Node(data, self.start)
    #     if self.start == None:
    #         self.start = temp
    #     else:
    #         tr = self.start
    #         while tr.next != self.start:
    #             tr = tr.next
    #         tr.next = temp
        


cll = circularLinkedList()
cll.display()
# cll.insertAtEnd(50)
# cll.display()
cll.insertAtStart(10)
cll.display()
cll.insertAtStart(20)
cll.display()
cll.insertAtStart(30)
cll.display()
# cll.insertAtEnd(40)
# cll.display()