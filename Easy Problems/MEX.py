"""
add elements of arr in a dictionary for easy lookup
brr => all possible si
while K > 0 => if an element is not already in a dictionary then add it

after k is zero simple iterate over brr and check which is the first element in
brr which is not there in the dictionary

NOTE: I have used try and except because the interpreter will throw an error
      when i is not present in the dictionary 
"""

testcase = int(input())

for _ in  range(testcase):

    N , K  = [int(i) for  i in input().split()]
    arr = [int(i) for  i in input().split()]
    brr = [i for i in range(200001)]

    dc = {}
    for i in arr:
        if i not in dc:
            dc[i] = 0
        dc[i] = dc[i] + 1
        
    for i in brr:
        if K == 0:
            break
        if i not in dc:
            dc[i] = 1
            K = K - 1

    for i in brr:
        try:
            if dc[i] == 1:
                pass
        except:
            print(i)
            break
