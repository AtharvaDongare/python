class example:
    def __init__(self):
        self.memberVariable=None

    def getValue(self):
        return self.memberVariable
    
    def setValue(self, value):
        self.memberVariable = value

e1 = example()
# e1.setValue(10)
print("member variable value : ", e1.getValue())