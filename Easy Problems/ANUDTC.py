"""
1 -> if 360 % N == 0 -> y -> else -> n
2 -> if N<=360 -> y-> else -> n
3 -> if fibonacci will N is < than 360 -> y else -> n


use try and catch to eliminate cases of dividing by 0
ie if N == 0 :
print ("y y y")

When N is equal to 27 then 1+2....+27 = 378 which is more than 360 so 27
different parts cant be made
"""

testcase = int(input())
for _ in range(testcase):
    num =  int(input())
    try:
        s = ""
        if(360%num ==0):
            s = s + "y "
        else:
            s = s + "n "

        if(num<=360):
            s = s + "y "
        else:
            s = s + "n "

        if (num<27):
            s = s + "y "
        else:
            s  = s+"n "

        print(s)    
    except:
        print("y y y")
