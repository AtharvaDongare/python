"""
List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
"""


"""
Q : create a list of integers which specify the length of each word in a certain sentence, 
but only if the word is not the word "the".
"""

# sentence = " create the list of integers which specify the length of each word in the certain sentence, \
# but only if the word is not the word 'the'."
# outputList = [len(word) for word in sentence.split() if word != "the"]
# print(sentence)
# print(outputList)


"""
Q : Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
which contains only the positive numbers from the list, as integers.
"""
# numbers = [1, 3, -4, 17, 5.6, -44, -2, 6, -7, 0]
# newlist = [num for num in numbers if num >= 0]
# print(numbers)
# print(newlist)

"""
create a list of strings which contain only values "even" or "odd" 
based on the value on a number in input list 
"""
# numbers = [1, 3, -4, 17, 5.6, -44, -2, 6, -7, 0]
# outputList = ["even" if num%2 == 0 else "odd" for num in numbers]
# print(numbers)
# print(outputList)

"""
Using list comprehension, create a list of ip address in range 
10.10.10.1 to 10.10.10.20
"""
# outputList = ["10.10.10.%d" % i for i in range(1,21)]
# print(outputList)

"""
Given a list of numbers, write a list comprehension that produces a list of strings of each number,
that is divisible by 5.
# """
# inputList = [10, 23, 25, 44, 45]
# outputlist = [str(num) for num in inputList if num%5 == 0]
# print(inputList)
# print(outputlist)

"""
Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative.
"""
# inputList = [10, 23, 25, 44, 45, 34, 56, 78, 23, 45, 67]
# outputlist = [num*2 if num%2 ==0 else num*-1 for num in inputList]
# print(inputList)
# print(outputlist)

