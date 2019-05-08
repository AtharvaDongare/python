class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

n1 = node(10)
n2 = node(20, n1)
n3 = node(30, n2)
n4 = node(40, n3)

tracer = n4

while tracer != None:
    print(tracer.data)
    tracer = tracer.next

