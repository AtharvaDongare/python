"""
compare 1 element with remaining elements and swap for order
"""

def bubbleSort(inputArray):
    for i in range(len(inputArray)-1):
        for j in range(i+1, len(inputArray)):
            if inputArray[i] > inputArray[j]:
                temp = inputArray[j]
                inputArray[j] = inputArray[i]
                inputArray[i] = temp
        print("pass %d : " % i, inputArray)


inputArray = [23, 45, 67, 987, 92879, 62234, 900, 12, 56,78]

print("original input : ", inputArray)
bubbleSort(inputArray)
print("input after sorting : ", inputArray)

