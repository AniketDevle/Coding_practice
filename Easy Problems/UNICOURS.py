"""

Couldn't think of a greedy attempt in the first time.....How noob are you aniket Rn

Here is the solution from the editorial


The solution to the problem is simply n−max(a), where max(a) denotes the maximum element in the array.
To see why the above claim holds true, we just use the fact that a given subject can act as the pre-requisite
for more than one subject too.
So, we apply greedy strategy here and find the subject which has most subjects as its pre-requisite.
So, we need atleast these many subjects which cannot count to our final answer.
Now, we claim that there is always a way to select these subjects only and form our answer such that remaining subject have no dependencies.

Just select the subject with the maximum number of dependencies.
If multiple such subjects exist, select the one with the lowest difficulty.
Then select subjects with least difficulty (will be the starting subjects only) and have difficulty less than the above-selected subject.
We claim that these subject can act as pre-requisite for all the courses.
These subjects can definitely act as pre-requisite for all courses that have difficulty greater than them.
Now, if some subjects among the selected ones also have dependencies, then subjects of lower difficulty as also present and can act as pre-requisite for these too.
(as there is no limit on the subject as to how many subjects have it as a pre-requisite).
Also, above selection is possible as it is given that a[i]<ia[i] < ia[i]<i.

Let us see this through an example as well. Let the array aaa be :

a={0,1,0,2,3,1,3,2}a = \{0, 1, 0, 2, 3, 1, 3, 2\}a={0,1,0,2,3,1,3,2}

From the above argument, we select the subject 555, first as it has the maximum number of dependencies
(subject 777 is not selected as it is of higher difficulty).
Now the claim is that the first 333 subject can act as pre-requisite for all the subjects.
This is because subject 111 can act as pre-requisite for subject {2,4,5,6,7,8}\{2, 4, 5, 6, 7, 8\}{2,4,5,6,7,8},
subject 222 can act as pre-requisite for {4,5,7,8}\{4, 5, 7, 8\}{4,5,7,8}
and subject 333 can act as pre-requisite for {5,7}\{5, 7\}{5,7}

"""
            
testcase = int(input())
for z in range(testcase):
    num = int(input())
    arr = [int(d) for d in  input().split()]
    print(num - max(arr))














    
