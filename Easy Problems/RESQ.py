"""
it is absolutely necessary to understand that we dont have to iterate till Num
for getting  maximum efficiency
infact we only have to iterate till the square of iterator is less the num cause
after that no combination will suit the requirements

mistakes
Sbumission 1: iterated till Num and used an array to save difference
submission 2: removed the array part but still iterated till Num
submission 3: iterated till num//2

finally accepted when i*i < num condition is used 


"""

testcase = int(input())
for _ in range(testcase):
    num = int(input())
    arr = []
    mini = num+1
    i = 1
    while i*i <=num:
        if(num%i == 0):
            diff = abs(i - num//i)
            if diff<mini:
                mini = diff
        i = i+1
    print(mini)
