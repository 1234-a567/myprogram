'''print("anil")
x='anil'
rev=x[::-1]
if x==rev:
    print("yes")
else:
    print("no")'''

'''n=int(input())
rev=0
print(n//2)
for i in range(0,(n//2)+1):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)
n=int(input())
a=0
b=1
count=0
while n>0:
    print(a)
    nth=a+b
    b=a
    nth=b
    count=count+1
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(5)'''
'''word=input("enter a word:")
output=""
index=0
while index<len(word):
    if word[index] in word:
        output=word[index]+output
        index+=1
print(output)'''
'''word=input("enter a word:")
output=""
for i in range(len(word)):
    if word[i] in word:
        output=word[i]+output
print(output)'''
'''list=["anil","dileep","my","python"]
output={}
for item in list:
    if item not in output:
        output[item]=len(item)
print(output)'''
'''list=["anil","dileep","my","python","my"]
index=0
output={}
while index<len(list):
    if list[index] in output:
        print("error")
    elif list[index] not in output:
        output[list[index]]=len(list[index])
    index+=1
print(output)'''
'''def user():
    count=0
    for i in range(1,5):
        num=int(input("enter a number:"))
        count+=num
    print(count)
user()

def fun():
    even=[]
    odd=[]
    for i in range(1,21):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)
    print(type(even))

num=int(input("enter a val"))
print(num)
fun()
class anil:
    def fun(self):
        even=[]
        odd=[]
        for i in lis:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        print(even)
        print(odd)
lis=eval(input("enter a list:")) 
a=anil()
a.fun()'''

'''n=int(input("enter  a num:"))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1:
            print("*",end=" ")
    print()
n=int(input("enter  a num:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0:
            print("*",end=" ")
    print()'''
'''n=int(input("enter  a num:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n//2 or col==0 or row==n-1:
            print("*",end=" ")
    print()
n=int(input("enter  a num:"))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
n=int(input("enter a num:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print("*",end=" ")
        else:
            print(end="")
    print()'''

'''n=int(input("enter a number:"))
for row in range(n,0,-1):
    for col in range(row):
        print(col+1,end=" ")
    print()
'''
'''n=int(input("enter a number:"))
for row in range(n):
    for col in range(n,0,-1):
        print(chr(65+col),end=" ")
    print()
n=int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if row==(1,n-1)  or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(end=" ")
    print()'''
def anil():
    vo=[]
    con=[]
    vow=['a','e','i','o','u','A','E','I','O','U']   
    for i in string:
        if i in vow:
            vo.append(i)
        else:
            con.append(i)
    print(vo)
    print(con)
string=input("enter a string:")
anil()






























print("-----THE END-------")


            





