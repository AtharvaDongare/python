"""
Functions are like factories that take in some material, 
do some operation, and then send out the resulting object.
"""

# function definition
def add(a, b):
    # function body
    c = a+b
    # function returning a value
    return c

# function call
addition = add(5,6)

# printing the result
print(addition)

# ^ the print() is also a function call to a function which displays output on console.

# function calls as a part of complex expression
print(add(3,4))

# more complex
print(add(add(3,4), add(2,8)))
"""
print(
    add(
        add(3,4), 
        add(2,8)
        )
    )
"""