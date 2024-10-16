'''print("hello world")

num=int(input("enter the number:"))
rev=0
temp=num
while temp>0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
if rev==temp:
    print("anil")
else:
    print("dileep")
char="A"
print(ord(char)
for i in range(65,91):
      print(chr(i))
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config sre",self.cpu,self.ram)
com1=computer("i5",6)
com2=computer("i6",8)
com1.config()
com2.config()
com2.config()
com1.config()
class anil():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print("sum is",self.a+self.b)
    def sub(self):
        print("sub is",self.a-self.b)
    def mul(self):
        print("mul is",self.a*self.b)
    def div(self):
        print("div is",self.a/self.b)
    
    
a1=anil(2,3)
a1.sum()
a1.sub()
a1.mul()
a1.div()
l=[1,2,3,4,5]
size=len(l)
temp=l[0]
l[0]=size-1
size-1=temp
l=["anil",True,12]
l.enumerate()
print(l)
def swaplist(lis):
    a[0],a[-1]=a[-1],a[0]
    return a
a=[1,2,3,4,5]
print(swaplist(a))
n=2
r=2
z=pow(12,21)/1000000007
print(z)

class Solution:
    #Complete this function
    def power(self,N,R):
        MOD = 10**9+7
        result = pow(N,R,MOD)
        return result

n=int(input())
if n%2==1:
    print("weird")
elif ofr n in range(2,5):
    print("not weird")
elif:
    for n in range(6,20):
        print("weird")
              
elif n>20:
    print("not weird")
a=[1,2,3,4,5]
count=0
for i in a:
    count+=i
print(count)
a=[1,2,3,4,5]
l=[]
for i in a:
    l.append(i)
print(list(l))
class A:
    def ff(self):
        print("this is f1")
    def gg(self):
        print("this is f2")
class B():
    def aa(self):
        print("anil")
    def bb(self):
        print("dilep")
        super.(
            )
b=B()
b.bb()s
print("before swapping")
a=10
b=20
print(a,b)
print("after swapping")
a,b=b,a
print(a,b)
a=10
b=20
def anil():
  a,b=b,a 
anil(a,b)
print(a,b)
a=int(input("a: "))
b=int(input("b: "))
print(f ,"before swapping"\n "a:"{a}\n "b:"{b})
a=int(input("a:"))
b=int(input("a:") )
a=a*b
b=a//b
a=b//
print(f "a:{a}\n b:{b}")


 a=10
a=30
print(bin(30))
print(bin(7))
a=int(input("a:"))
b=int(input("b:"))
print(f"before swapping\na:{a}\nb: {b}")
c=a
a=b
b=c
print(f"after swapping\na:{a}\nb: {b}")'''

#print("-----THE END-------")
'''row=int(input())

for i in range(row):
    for j in range(row):
        print("*",end=" ")
    print()'''
'''row=int(input())
for i in range(row):

    print(chr(65) * row)
a=int(input())
b=int(input())
for i in range(b):
    for j in range(a):
        print("*",end="")
    print()
n=int(input())
for i in range(n):
    print("*",end="")

n=int(input())
for i in range(n):
    print("5"*n,end="\n")
n=int(input())
for i in range(n):
    print((str(n)+' ')*n)
n=int(input())
for i in range(n):
    print((str(i+1)+ " ")*n)
n=int(input())
str=1
spc=n-1
for i in range(n):
    for j in range(spc):
        print('',end=" ")
    for k in range(str):
        print("*",end=" ")
    print()
    str+=2
    spc-=1
n=int(input("a:"))
spc=n-1
str=1
for i in range(n):
    print(" "*spc+"*"*str)
str+=2
spc-=1
n=int(input("a:"))
for i in range(n):
    for j in range(n-1-i):
        print(" ")'''

'''n=int(input("a:"))
val=1
for i in range(n):
    print(" "*(n-1-i)+(str(val)+" ")*(2*i+1))
    val+=1
    if val>9:
       val=1'''
'''n=int(input("a:"))
val=ord("A")
for i in range(n):
    print(" "*(n-1-i)+(chr(val)+" ")*(2*i+1))
    val+=1
n=int(input("n:"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()
n=int(input())
for i in range(n):
    print(str("1")*4,end=" ")
print()
n=int(input("a:"))
for i in range(n):
    print("*",end= " ")'''

'''n=int(input("a:"))
for i in range(n):
    print("* "*n)
n=int(input("a:"))
for i in range(n):
   for j in range(i+1):
      print("* ",end="")'''
'''def anil(a,b):
    print(f"the sum of {a} and {b}",a+b)
    print(f"the sum of {a} and {b}",a*b)
    print(f"the sum of {a} and {b}",a-b)

    
   
anil(2,3)
anil(4,6)
def dil(b):
    a="anil"
    print(a+b)
    print("dil"+b)
dil("kumar")'''
'''n=int(input("n:"))
for i in range(n):
   for j in range(n):
      print(j,end=" ")
   print()
n=int(input("n:"))
for i in range(n):
    for j in range (n):
        print(i,end=" ")
    print()
n=int(input("n:"))
for i in range(n):
   for j in range(i+2):
      print(chr(65),end=" ")
   print()
n=int(input("n:"))
for i in range(n):
class calculator(a,b):
    def add(self,a,b):
        print(self.a+self.b)
    def sub(self,a,b):
        print(self.a-self.b)
    def mul(self,a,b):
        print(self.a*self.b)
c=calculator(1,2)
c.add()
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i+j==0 or i+j==2 or i+j==5:
            print("*",end=" ")
        else:
            print("$",end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        print((j*2)+1,end=" ")
    print()'''
'''a=65
print(chr())
for i in range(65,98):
    print(ord("i"))'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print(ord(97)*n,end=" ")
    print()
print(chr(65))
print(chr(90))
for i in range(65,91):
    print(chr(i),end=' ')
n=int(input())
for i in range(n):
    for j in range(n):
        print(ord(i))
for i in range(65,69):
    for j in range(65,69):
        print(chr(j),end=" ")
    print()
n=int(input())
for  i in range(n):
    for j in range(n):
        if i+j==0 or i+j==2 or i+j==4:
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()'''
'''n=int(input()) 
fact=1
for i in range(1,n+1):
    fact=fact*i  
print(fact)

def anil(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
#n=int(input())
anil(5)
a=10
b=20
c=a
a=b
b=c
print(a,b)
a=10
b=20
c=30
a,b,c=c,a,b
print(a,b,c)
a=10
b=20
a=a*b
b=a//20
a=a//10
print(a,b)'''
'''def is_subsequence(s1, s2):
    i = 0
    for c in s2:
        if i < len(s1) and c == s1[i]:
            i += 1
    return i == len(s1)

# Example usage
s1 = "abc"
s2 = "ahbgdc"
print(is_subsequence(s1, s2))'''
'''from collections import counter 
print(counter([1,2,3,1,2,3,1,2,3,,1,2,3,4]))
from collections import Counter 
  
# With sequence of items  
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))

class car:
    wheel=4
    paint="red"
    def anil(self):
        self.mil=15
        self.com="bmw"
c1=car()
c2=car()
c1.mil=20
c2.mil=35
c1.com="rr"
c2.com="thar"

print(c1.mil,c1.com,c2.paint)
print(c2.com,c2.mil,c1.paint)
print(c2.mil)
print(c2.wheel,c1.paint)
def anil(self):
    self.a=10
anil()
class A:
    def show(self):
        print("thhis is anil")
class B(A):
    def show(self):
        print("thhis is anil")
B1=B()
B1.show()

class A:
    def anil(self):
        print("thhis is anil")
class B(A):
    def dil(self):
        print("thhis is dileep")
A1=A()
B1=B()
A1.dil()
_a=10
def anil():
    print(_a)
anil()
n=int(input("n"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
n=int(input("n:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
print(c)'''
'''c=0
#print(len(str(n)))
m=str(n)
n=int(input())
c=0
while n>0:
   n=n//10
   c=c+1
print(c) 
a=-12.4
print(abs(a))
a=int(input())
print(a=str(a)[::-1])'''
'''n=int(input())
new=0
while n!=0:
    rem=n%10
    new=(new*10)+rem
    n=n//10
print(new)'''
'''n=int(input())
new=0
temp=n
while n!=0:
    rem=n%10
    new=(new*10)+rem
    n=n//10
if temp==new:
    print("its is palindrome")
else:
       print("its is  not palindrome")
n=int(input())
zc,oc,ec=0
while n>0:
    rem=n%10:
    if rem==0:
        zc+=1
    elif rem%2==0:
        ec+=1
    else:
        od+=1
    n=n//10
print(zc,ec,oc)
n=int(input())
max=0
for i in str(n):
    if int(i)>max:
        print(int(i))'''
'''
a,b=0,1
n=int(input("n:"))
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b 
    b=c'''
'''a,b=0,1
n=int(input("n:"))
i=0
while(i<n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

l=[1,56,"anil",34.5,True,1+2j,45,67,100]

print(l[-2:-10:-1])
#print(l)ssssssss
n=int(input("n:"))
a=0
b=0
for i in range(1,n+1):
    if i%2!=0:
        if i==1:
            a=1
        else:
            a=a*2
    else:
        if i==2:
            b=1
        else:
            b=b*2
if n%2!=0:
    print(n,a)
else:
     print(n,b)'''

'''n=int(input())
arr=list(map(int,input().split()))'''
#choclate factory
'''n=int(input())
j=0
l=[0 for  i in range(n)]
for i in range(n):
    a=int(input("a:"))
    if a!=0:
        l[j]=a 
        j+=1
for i in l:
    print(l,end=" ")'''
'''l=list(input().split())
print(l)
m=0
for i in l:
    m=max(m,len(i))
print(m)'''
'''str=str(input())
for i in range(len(str)):
    for j in range(i+1,len(str+1)):
        print(i,j)'''
'''a=str(input())
b=str(input())
c=str(input())
vowel=["a","e","i","o","u"]
for i in a:
    if x in vowel:
        a.replace'''

'''Vowel =[“a”,”e”,”I”,”o”,”u”]
A= str(input ())
B= str(input())
C=str(input())
For X in a:
If x in vowel:
A=a. Replace (a,”*”)
For y in b :
If y in vowel:
B= b.replace(b,”@”)
C= c.upper()
Word= a+b+c
Print (word)'''
'''A=str(input())
B=str(input())
C=str(input())
vow=['a','e','i','o','u']
for i in A:
   if  i in vow:
      A=A.replace(i,"%")
print(A)
for i in B:
   if i not in vow:
      B=B.replace(i,"@")
print(B)
C=C.upper()
print(C)'''
'''num = str(input())
print(int(num,17))
def base17_to_decimal(base17_num):
    base17_num = base17_num.upper()
    decimal_num = 0
    power = 0
    for digit in reversed(base17_num):
        if digit.isdigit():
            decimal_num += int(digit) * (17 ** power)
        else:
            decimal_num += (ord(digit) - 55) * (17 ** power)
        power += 1
    return decimal_num

base17_num = input("Enter a base 17 number: ")
print("The decimal equivalent is:", base17_to_decimal(base17_num))'''
'''num=str(input)
odd,even=0,0
for i in range(0,len(num)+1):
    if i%2==0:
        even+=num[i]
    else:
        odd+=num[i]
print(abs(even-odd))'''
'''num = [int(d) for d in str(input("Enter the number:"))]
print(type(num))
print(num)
even,odd = 0,0
for i in range(0,len(num)):
    if num[i]% 2 ==0:
        even = even + num[i]
    else:
        odd = odd + num[i]

print(even-odd)'''
'''n=input()
#keyword_l={break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type
keyword = {"break", "case", "continue", "default", "defer", "else", "for", 
"func", "goto", "if", "map", "range", "return", "struct", "type", "var"}

if n in keyword:
    print(f"{n} is already keyword")
else:
    print(f"{n} is not  already keyword")'''
'''n=input()
p=1
for i  in n: 
   p*=int(i)
print(p)
n=input()
p=1
for i in n:
    p*=int(i)
print(p)'''
'''a=input()
for i in a:
    print((chr(ord(i)+5)),end="")'''
#a=int(input("enter the number:"))
#a=0
#print(bool(0.0))
#string functions
a="@@@anil@@@"
'''print(a.isupper())
print(a.islower())
print(a.isdigit())
print(a.count('a'))
#print(a.center())
print(a.isprintable())
print(a.upper())
print(a.replace('a','d'))
#print(a.('a','d'))
print(a.casefold())
print(a.split("@"))
print(a)
print(a.strip())
print(a.find("i"))
print(a.lstrip())'''
#codecheff
'''x,y=map(int,input().split())
print(x*6+y*1)'''
'''n=int(input())
if n>12:
    print("yes")
else:
    print("no")'''
'''n=int(input())
if n<25 or n>25:
    print("ordinary")
else:
    print("christmas")
def twosum(num,tar):
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i]+num[j]==tar:
                return [i,j]
retutn[]'''
#n=int(input())
#for i in n:
#EXCEPTION HANDLING
'''f=open("mydata",'w')
f.write("my name is dileep")
f.write("hlo ,hi")
f.write("good")'''
'''def sum(a,b):
    return a+b
print(sum(1,3))'''
'''class test:
    def sum(self,a,b):
        return a+b
t=test()
print(t.sum(1,2))'''
'''test=str(int(input()))
for i in test:
    N=int(input())
    s=str(input())
    new=s.replace("00",'A') or s.replace("01","T") or s.replace("10",'C') or s.replace("11",'G')
    test=test-1
print(new)
print("anil kumar")  
print("dileep")
print("ani")

def sum(a,b):
    return a+b
print("sum of two numbers",sum(1,2))
print("sum of two numbers",sum(4,5))
print("sum of two numbers",sum(4,8))
l=("anil",1,2)
print(l[1])
print("sum of two numbers",sum(4,8))'''
'''test=input()
while test<5:
    for i in test:
        k=int(input("enter the value:"))
        L=int(input("enter the value:"))
        print(k+l)
        test-=1'''
'''i=0
while i<10:

    i=i+1
    if i==5:
        continue
    print(i)'''
'''l=[]
le=[]
lo=[]
for i in range(1,10):
    l.append(i)
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)
print(le)
print(lo)
dict={
"name":"anil",
"age":22,
"place":"kdp",

}
print(dict)
print(len(dict))
print(type(dict))
print(dict["name"])
print(dict.get("name"))
print(dict.keys())
print(dict.values())'''
# cook your dish here
'''TEST=int(input())
M=""
for i in range(TEST):
    S=str(input())
    T=str(input())
    for j in range(len(S)):
        if S[j]==T[j]:
            M=M+"G"
        else:
            M=M+"B"
    print(M)
    M=""'''
'''N,X=map(int,input().split())
#x=[3]
A=[7,3,5,2,1]
if X in A:
    print("yes")
else:
    print("No")
T=int(input())
for i in range(T):
    N=int(input())
    for j in range(N):
        if j=="00":
            print("A")'''
'''n=str(input())
z=""
for i in range(0,len(n),2):
    if n[i]+n[i+1]=="00":
        z=z+"G"
    elif n[i]+n[i+1]=="01":
        z=z+"b"
    elif n[i]+n[i+1]=="10":
        z=z+"c"
    else:
        z=z+"a"
print(z)
T=int(input())
z=""
for i in range(0,T):
    N=int(input())
    S=str(input())
    for j in range(0,len(S),2):
        if S[j]+S[j+1]=="01":
            z=z+"A"
        elif S[j]+S[j+1]=="01":
            z=z+"T"
        elif S[j]+S[j+1]=="10":
            z=z+"C"
        elif S[j]+S[j+1]=="11":
            z=z+"G"'''
'''print(z)
n=int(input())
for i in range(1,n+1):
    a=int(input())
    z=""
    h=str(input())
    for j in range(0,a,2):
        if(h[j]+h[j+1]=="00"):
            z=z+"A"
        elif(h[j]+h[j+1]=="01"):
            z=z+"T"
        elif(h[j]+h[j+1]=="10"):
            z=z+"C"
        else:
            z=z+"G"
    print(z)'''
'''print(eval('1+2'))
print(eval("sum([1, 2, 3, 4])"))
x = 'print(55)'
eval(x)'''
# This function uses global variable s
'''def anil():
    s="anilkumar"
    s="anil"
    s="kumar"
    print(s)
    s="dil"
anil()
print("outside",s)'''
'''class anil:
    def __init__(self,a):
        print(a+10)
a=anil(20)'''
#sets
'''a={10,20,30,40,50}
b={60,75,20,50}
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.union(b))
s={}
print(scl'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("A",end=" ")
    print()'''
'''a=(1,2,3)
b=(4,5,6)
x=zip(a,b)
y=list(x)
print(y)
print(type(y))
a=[[10,20,30],
   [10,20,30]]
b=[[1,2,3],
   [1,2,3]]
x=zip(a,b)
y=list(x)
print(list(y))
print(type(y))
class anil:
    def dil(self,n):
        if n%2==0:
            print("even")
        else:
            print("odd")
    'def dil(self,n):
        if n==0:
            print("it is zero")'''
'''a=anil()
a.dil(10)
for i in range(5):
    print("anil kumar")'''
'''class dil:
    def __init__(self):
        n=int(input("enter the number:"))
        if n%2==0:
            print("even")
        else:
            print("odd")
d=dil()
#d=dil()
def oe(n):
    #n=int(input("enter the number"))
    if n%2==0:
        print("even")
    else:
        print("odd")
oe(int(input("enter the number:")))'''
'''n=int(input("enter the number"))
new=123
if n==new:
    print("yes")
else:
    print("no")'''
#print(24233//2)
'''n=int(input("enter the number:"))
temp=n
new=0
while temp!=0:
    rem=temp%10
    new=(new*10)+rem
    temp=temp//10
    print(temp)
#print(new)
print(temp)
if temp==new:
    print("yes")
else:
    print("no")
#print(new)
n=int(input())
new=0
temp=n
for i in range(n):
    rem=temp%10
    new=(new*10)+rem
    temp=temp//10
print(new)
n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        print("*")   
dict={
"name":"anil kumar",
"age":20,
"gender":"male",
"graduation":"btech",
'year':2024
}
#print(dict)
#print(dict.keys())
#print(dict.values())
#print(dict.get(""))

#print(list(dict.items()))'''


'''class anil:
    def add(self,n1,n2):
        return n1+n2
    def add(selef,n1,n2,n3=1):
        return n1+n2+n3
a=anil()
#print(a.add(10,20)'''

'''def add(a,b):
    return (a+b)
print(add(10,20))'''
'''class name:
    def __init__(self,a,b):
        print(a+b)
a=name(10,20)'''
'''class cat():
    def sound(self):
        print("meow")
    def sleep(self):
        print("sleep")
class lion(cat):
    def sound(self):
        print("roar")
a=cat()
a.sound(
a={
    "name":"anil",
    "age":20,
}
print(a["name"])
#a.update("study":"btech")
#a.update(col)
a["color"]='green'
print(a.keys())
print(a.values())
print(a.items())

print(a)'''
'''class parent:
    def older(self):
        print("respect them")
class child(parent):
    def older(self):
        print("take and give respect")
        super().older()
c=child()
c.older()
class anil: 
    def add(self,n1,n2,n3):
        print(n1+n2+n3)
class dil(anil):
    def add(self,n1,n2):
        print(n1+n2)
        #super().add()
d=dil()
#d.add(1,2,3)
d.add(1,2)
d.add(5,6,8)'''
#p=parent()
#c.younger()
#c.older()
#c.older()
'''a=input()
for i in range(::2):
    print(i*(a[i+1]))'''
'''class anil:
    def an(self):
        print("my name is anil kumar")
        print("i am from andhra")
class dil(anil):
    def di(self):
        print("currently i am  ina banglore")
        print("searching for a job")
        #return dileep
        #super().an()
        var=an()
        print(var)
d=dil()
d.di()
a=anil()
import re 
name="anil kumar"
res=re.findall("a",name)
print(res)
#print(d.di())
#d.an()
#a.an()
#a.di()'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print(i+1,end=" ")
    print()'''
'''n=int(input())
for i in range(n):
    for j in range(n):
        print(j+1,end= " ")
    print()
def isyear(y):
    if y%4==0 or y%400==0:
        print("leap year")
    else:
        print("not leap year")
isyear(int(input())
class anil:
    def dil():

        print("this method belongs to class anil")
class anil1(anil):
    def dil1():
        print("this method belongs to class anil1 ")
        super().dil()
a=anil1
a.dil1()

import re
txt="the rain in spain"
#print(re.findall("a",txt))
print(re.split("\s",txt,2))'''
'''sum=0
l=[10,20,30,40]
for i in l:
    sum=sum+i
print(sum//4)
max=0
arr=[1,23,45,12,68,34]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)
str="my name is anil"
#print(str.reverse())
lis=[]
rev_str=""
for i in str:
    lis.append(i)
print(lis)
for k in lis:
    rev_str=k+rev_str
print(rev_str)
print(lis)
x=lis.reverse()
print(x)
for i in range(10):
    print(f"bin of{i}",bin(i))
print(15 & 20)
print(~15,~20,~44)
print(15^20)
print(2<<3)
print(bin(1))
print(bin(2))
print(15^7)
print(1|2)
print(bin(3))
l=[10,20,55,11,34,23,55]
li1=[]
se=set()
for i in l:
    se.add(i)
    li1.append(i)
print(li1)
print(se)'''
'''l=[10,20,55,33,44]
max=0
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
print(f"first max element is:{max}")'''
'''l=[10,20,55,33,44,33]
new=list(set(l))
new.sort()
print(new[-2])'''
'''def max2():
    new=list(set(l))
    new.sort()
    print(new[-2
max2()'''
'''x, y = map(int,input().split())
print(x,y)
import turtle
skk=turtle.Turtle()
skk.fd(100/2)
skk.rt(45)
skk.fd(100)
skk.rt(90)
for i in range(5 ):
    skk.forward(100)
    skk.rt(45)
skk.rt(90)
skk.backward(200)
skk.lt(7)
skk.fd(250)
turtle.done()'''
'''num=int(input("enter the number:"))
if 0<=num<=8 or -8<=num<=-1:
    print(f"{num} is between range 1 to 8")
else:
    print(f"{num} is between range 8 to infinte")'''

'''num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)'''
'''num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)'''
#num=int(input("enter the number:"))
'''a=0
b=1
for i in range(1,10):
    num=a+b
    a=1
    b=num
print(num)'''
'''a=0
b=1
n=int(input("enter the number:"))
while n>=2:
    t=a+b
    a=b
    b=t
    '''
'''num=int(input('enter the number:'))
count=0
m=num
while num>0:
    r=num%10
    count=count+r*r*r
    num=num//10
if m==count:
    print("armstrong")
else:
    print("both are not equal")'''

'''num=int(input("enter the number:"))
rev=0
new=num
while num>0:
    ls=num%10
    rev=(rev*10)+ls
    num=num//10'''
#print(new)
#print(rev)
#armstrong
'''num1=int(input("enter a number"))
new=num1
count=0
while num1>0:
    r=num1%10
    count=count+r*r*r 
    num1=num1//10
print(num1)
print(new)
print(count)'''
'''sum=0
for i in range(1,101):
    sum=sum+i
print(sum)'''
'''sum=0
n=int(input("enter the n:"))
for i in range(1,n):
    if n%i==0:
        sum=sum+i
print(sum)'''
'''n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()'''
'''n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

n=int(input("enter a number:"))
#spc=3
for i in range(1,n+1):
    for j in range(i):
        print(i,end= " ")
    print()
second_max=0
list=[10,20,6.5,30]
fm=max(list)
for i in range(len(list)):
    if list[i]<fm:
        second_max=list[i]
print(second_max)'''
'''char='A'
for row in range(5):
    for row in range(5):
        print(char,end=" ")
        char=chr(ord(char)+1)
    print()
    char=chr(ord(char)-2)'''
'''from time import sleep
print("anil")
import phonenumbers
from phonenumbers import geocoders
colors = ["red", "green", "blue"]
for i,j in enumerate(colors):
    print(i,j)
def f1(msg):
    print(msg)
f1("anil kumar")
f2=f1
f2("this is dilepe")'''
'''def f1():
    print("this is my f1")
    def f2(msg):
        print("this is my f2")
    def f3():
        print("this is my f3")
    f2("this is also f2")
    f3()
f1()
def dil(msg):
    print("hi,dil")
    print(msg)
dil("anil kuamr")
dil("dileepe")
def anil():
    print("this is my outer fun")
    def dil():
        print("this is myh inner fun")
        def dil1():
            print("this is  my second inner")
        dil1()
    dil()
anil()'''

'''class anil:
    def sum(self,a):
        print("anil kuamr")
        print(a)
    def __init__(self):
        print("thihs  is my init method")
a=anil()
a.sum("dileep")
a.sum("anil")
'''
'''class anil:
    def dil(self,n):
        l=[]
        l.append(n)
        print(l)
a=anil()
#for k in range(4):
a.dil(n=int(input("enter a number:")))'''
'''class dil:
    def anil(self):
        print("this is class")
d=dil()
for i in range(3):
    d.anil()

'''
'''print(hash(42))
print(hash(42.1))
print(hash(42.3))
print(hash("42"))
'''
'''print(any([]))
print(all([]))
print(dir(__builtins__))'''
#print(dir(abs))
import keyword
print(keyword.kwlist())
print("------THE END-------")
    




























