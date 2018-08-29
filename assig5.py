#ques1
year=int(input("enter year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
    
#ques2
length=input("enter length:\n")
breath=input("enter breath:\n")
if length==breath:
    print("It is square")
else:
    print("It is rectangle")
    
#ques3
age1=int(input("enter first age:"))
age2=int(input("enter second age:"))
age3=int(input("enter third age:"))
if age1>age2 and age1>age3:
    print("first age is oldest")
elif age2>age3 and age2>age1:
    print("second age is oldest")
else:
    print("third is oldest")
if age1<age2 and age1<age3:
    print("first age is youngest")
elif age2<age3 and age2<age1:
    print("second age is youngest")
else:
    print("third age is youngest")

#ques4
sex=input("enter sex:")
age=int(input("enter age:"))
ms=input("enter marital atatus:")
if sex=='female':
    print("she work in urban area")
else:
    if age>20 and age<40:
        print("he may work anywhere")
    else:
        print("he work in urbun area")
if age<20 and age>40:
    print("ERROR")

#ques5
q=int(input("enter quantity"))
q=q*100
if q>1000:
    q=q-(q*0.1)
print("total cost: ",q)

#ques6
a=[]
for i in range(0,5):
    n=int(input("enter value"))
    a.append(n)
print(a)

#ques7
n=0
while n==0:
    print("aditya")

#ques8
a=[]
b=[]
for i in range(0,5):
    n=int(input(""))
    a.append(n)
    b.append(n*n)
print(a)
print(b)

#ques9
a=[14,18,'jain',7.9]
ints=[]
strs=[]
floats=[]
for i in range(0,4):
    if isinstance(a[i],int):
        ints.append(a[i])
    elif isinstance(a[i],str):
        strs.append(a[i])
    else:
        floats.append(a[i])
print(ints)
print(strs)
print(floats)

#ques10
a=[]
for i in range(1,101):
    flag=0
    if i==2:
        a.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break;
            else:
                flag=0
        if flag==0:
            a.append(i)
a.remove(1)
print(a)

#ques11
for i in range(0,4):
    for j in range(0,4):
        print("*",end='')
    print("\r")

#ques12
a=[]
for i in range(0,5):
    n=int(input("enter number"))
    a.append(n)
n=int(input("enter no. u want to delete"))
a.remove(n)
print(a)

