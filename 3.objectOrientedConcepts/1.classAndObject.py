class example:
    def __init__(self):
        self.memberVariable=None

    def getValue(self):
        return self.memberVariable
    
    def setValue(self, value):
        self.memberVariable = value
    
    def getSquare(self):
        return self.memberVariable**2

# create an object of example class
e1 = example()

# use class method to set member variable value
e1.setValue(10)

# use class method to get member variable value
print("member variable value : ", e1.getValue())

# perform operation on member variable
print("variable square : ", e1.getSquare())