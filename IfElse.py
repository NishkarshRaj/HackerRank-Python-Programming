num = int(input())
if (num%2==1):
    print("Weird")
else:
    if((num>=2) and (num<=5)):
        print("Not Weird")
    if ((num>=6) and (num<=20)):
        print("Weird")
    if (num>20):
        print("Not Weird")

"""
In python there are no {} blocks of code.
Here Indentation is a must
All looping and conditions must be followed by :
&& is not present like C C++ and Java and keyword is used here
elif is used not else if
"""
