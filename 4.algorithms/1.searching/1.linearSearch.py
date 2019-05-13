def findPosition(input, query):
    for i in range(0, len(input)):
        if query == input[i]:
            return i,True
    return 0,False

input = [3, 56, 34, 90, 19, 56]
query = 56
result = findPosition(input, query)
if result[1]:
    print("%d found at location %d" % (query, result[0]))
else:
    print("element not found")