def selectionSort(inputArray):
    for i in range(len(inputArray)):
        least = i
        for j in range(i+1, len(inputArray)):
            if inputArray[j] < inputArray[least]:
                least = j
        temp = inputArray[i]
        inputArray[i]=inputArray[least]
        inputArray[least] = temp

        print("pass %d : "% i, inputArray)



inputArray = [34, 345, 987, 890, 23, 976, 12, 76, 34, 10, 38]
print("before sort : ", inputArray)
selectionSort(inputArray)
print("after sort : ", inputArray)