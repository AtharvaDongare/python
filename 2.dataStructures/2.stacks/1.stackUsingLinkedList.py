class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class stack:
    def __init__(self, size=5):
        self.top = None
        self.size = size
        self.length = 0

    def display(self):
        print("--------------------------------------------")
        if self.top == None:
            print("cannot display : stack empty!")
        else:
            tr = self.top
            while tr != None:
                print(tr.data)
                tr = tr.next

    def push(self, value):
        if self.size < self.length+1:
            print("cannot push : stack overflow!")
            return
        temp = node(value, self.top)
        self.top = temp
        self.length = self.length+1

    def pop(self):
        if self.top == None:
            print("cannot pop : stack empty!")
            return
        temp = self.top
        self.top = temp.next
        temp = None
        self.length = self.length-1

s1 = stack()
s1.display()
s1.push(10)
s1.display()
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.display()
s1.push(60)
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.push(30)
s1.display()
