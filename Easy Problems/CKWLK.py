"""
find power of 2
find if there are enough zeros
"""
import math

testcase = int(input())
for z in range(testcase):
    S = input()
    S = S[::-1]
    Ending_zeros=""
    Num_reverse = ""
    for i in range(len(S)):
        if S[i] != '0':
            Num_reverse = S[i:]
            break
        else:
            Ending_zeros = Ending_zeros + "0"
    Num = int(Num_reverse[::-1])

    if (str(math.log(Num ,2)).split("."))[1] != '0':
        print("No")
        continue
    elif (len(Ending_zeros)< int(math.log(Num ,2))):
        print("No")
        continue
    else:
        print("Yes")
