class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def substract(self):
        return self.a-self.b

    def multiply(self):
        return self.a*self.b

    def divide(self):
        return self.a/self.b

    def power(self):
        return self.a**self.b

    def mod(self):
        return self.a%self.b

def main():
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))

    c1 = Calculator(n1, n2)
    print("addition : ", c1.add())
    print("substraction : ", c1.substract())
    print("multiplication : ", c1.multiply())
    print("division : ", c1.divide())
    print("power : ", c1.power())
    print("mod : ", c1.mod())
main()