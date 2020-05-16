"""
problem set by gennady
Ohh yeah the solution got accepted in the  first time

 step 1 : find the occurance of each character in each string
 step 2 : for all characters ==> find the minimum occurance of a character
          in all strings       and save them in a dictionary
 step 3 : find the cahracters whose value is not zero by sorting the keys
 step 4 : make answer string 

In step 3 we sort the keys because we want lexicographically smaller string
"""


def result(arr):
    s = ""
    for i in arr:
        x,y = i
        for _ in range(y):
            s = s + x
    return s        



def fn(Num_char_str , key):
    z = 1000
    for i in Num_char_str:
        if i[key]<z:
            z = i[key]
    return z        


di = {'a':1 , 'b':2 , 'c':3 , 'd': 4 , 'e':5 ,'f' :6 ,'g' :7 ,'h' :8 ,'i':9 ,
      'j':10, 'k':11 , 'l':12 ,'m':13 , 'n':14 , 'o':15 , 'p':16 , 'q':17 ,
      'r':18 , 's':19 , 't':20 , 'u':21 ,'v' :22 , 'w':23 , 'x':24 ,'y':25 ,
      'z':26}


num = int(input())
s = []
for _ in range(num):
    s.append(input())

##step1
Num_char_str = []
for i in s:
    d = {}
    for j in di.keys():
        d[j] = 0
    for j in i:
        d[j] = d[j]+1
    Num_char_str.append(d)
    
##step2
final_min = {}
for j in di.keys():
        final_min[j] = fn(Num_char_str , j)

##step3
arr = []
for i in sorted(di.keys()):
    if(final_min[i]>0):
        arr.append((i , final_min[i]))

##step4
if len(arr) == 0:
    print('no such string')
else:
    s = result(arr)
    print(s)    
