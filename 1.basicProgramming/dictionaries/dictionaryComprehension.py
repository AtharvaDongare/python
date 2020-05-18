"""
Advantages
As we can see, dictionary comprehension shortens the process of dictionary initialization by a lot. 
It makes the code more pythonic.
Using dictionary comprehension in our code can shorten the lines of code 
while keeping the logic intact.
Disadvantages
They can sometimes make the code run slower and consume more memory.
They can also decrease the readability of the code.

"""


"""
Using dictionary comprehension create a dictionary of 1-10 numbers with their squares
"""
# squaresDict = {x:x**2 for x in range(1,11)}
# print(squaresDict)

"""
change in price :
update all values in dict
"""
# old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
# newPrice = {key:value+10 for (key,value) in old_price.items()}
# print(old_price)
# print(newPrice)

"""
given a dict of student name : marks
create a new dictionary and allot 5 grace marks to those who have marks below 40 but equal to 35 or above
"""
# studs = {"Norton" : 35, "Peach":80, "sam":90, "ron":33, "james":38}
# newStuds = {name:marks+10 for (name,marks) in studs.items() if marks>=35 and marks<=40}
# print(studs)
# print(newStuds)

"""
create a dictionary to display status of students pass/fail based on if they have marks more than 50
"""
studs = {"Norton" : 35, "Peach":80, "sam":90, "ron":33, "james":38}
newStuds = {name:"pass" if marks>50 else "fail" for (name,marks) in studs.items()}
print(studs)
print(newStuds)


