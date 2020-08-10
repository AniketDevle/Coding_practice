arr = [3,2,2,3]

val = 3
counter = 0
length = len(arr)
for i in range(length):
    if (arr[i] == val):
        length -= 1
    else:
        arr[counter] = arr[i]
        counter = counter + 1 

print(arr)
print(length)
