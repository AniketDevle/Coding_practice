def calculate(num):
    remainder = 103993 % 33102
    num2 = 33102
    stri = "3."
    if num == 0:
        return "3"
    else:
        for i in range(num):
            remainder = remainder*10
            stri = stri + str(remainder/num2)[0]
            remainder = remainder % num2
        return stri    

testcase = int(input())
for z in  range(testcase):
    num = int(input())
    print(calculate(num))
