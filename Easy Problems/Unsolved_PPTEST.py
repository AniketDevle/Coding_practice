"""
Well this looks like an interesting problem

input :
Testcase
Number of Questions , Total Time available
for i in Number of Questions:
    get C[i] -> Number for test containing question i
    get P[i] -> Points for ith question
    get T[i] -> Time required to study ith question

_________________________________________________________________

The first thing that is comes to my mind is that total number of points a question
can offer is more important than the Number of test and Points of ith question
themselves.

number of points we get for studying one minute = (C[i] * P[i])/2 
Sort the question on basis of Number of points we get for studying for 1 minute

then get the max that we can get 

let T contains touples in form (Time[i] , total_points(i))

aniket maybe you have just messed up everything.....Not going with Dp didnt turned
out well ha!!

This mehod fails when the input is

1
3 5
1 8 1
2 5 2
4 5 3

S -> [(8,1) , (20 , 3) , (10 , 2)]
output by this method = 28
actual answer should be = 30

This is a dynamic programming question.....praactice some dp problems and then
try this once again 
"""

testcase =int(input())
for z in range(testcase):
    N , Total_time = [int(d) for d in input().split()]
    T = []
    for y in range(N):
        C , P , ti = [int(d) for d in input().split()]
        T.append(( C*P , ti ))
    S = sorted(T  , key = lambda x:x[0]/x[1] , reverse = True)

    Time_count = 0
    max_points = 0
    for i in S:
        if (Time_count + i[1] <= Total_time):
            Time_count = Time_count + i[1]
            max_points = max_points + i[0]
    print(max_points)            
        
