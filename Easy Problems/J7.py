"""
In this problem we are asked to optimise the volume of the rectangular box.
we can solve this problem easily because they have mentioned that there will
always be an optimum solution

l = length of the rectangular box
b = breadth of the rectangular box

solve these 2 equations to get the result

8* b + 4 * l = Total length of edges

2*b*b + 2*l*b = area of paper
"""
testcase = int(input())

for z in range(testcase):
    x,y =[int(i) for i in input().split()]

    b = (x - (x**2 - 24*y)**0.5)/12
    l = (x-8*b)/4

    print(round(l*b*b , 2))
     
