#Some functions mentioned in the task were available only in R
#As the assignment was to be done in pyton, alternatives were used for functions like cbind,rbind etc.

import numpy as np
import pandas as pd
from datar import *
from datar.datasets import mtcars as df
import re

#partA
#q1
print("2 raise to power of 5 is:",pow(2,5))
#q2
v=np.array([23,27,25,45,67])
print(v)
#q3
days=np.array(["Monday","Tuesday","Wednesday","Thursday","Friday"])
df1=pd.DataFrame(v,days)
print(df1)
#q4
print("Mean:",df1[0].mean())
#q5
print("Max on:",df1[df1[0]==df1[0].max()].index.values," :",df1[0].max())

#partD
#q1
print(df.head(6))
#q2
print("Average mpg:",df["mpg"].mean())
#q3
print(df[df['cyl']==6])
#q4
print(df[['am','gear','carb']])
#q5
df['performance']=(df['hp']/df['wt'])
print(df.head(6))
#q6
print("mpg of hornet sportabout:",df.loc['Hornet Sportabout']['mpg'])

#partB
#q1
def f1():
    s=input("Enter your name:")
    return (print("Hello ",s))
f1()
#q4
def f4():
    n=int(input("Enter a positive number:"))
    f=0
    if(n==1):
        return print(False)
    else:
        for i in range(1,n):
            if(n%i==0):
                f=f+1
    if(f==1):
        return print(True)
    else:
        return print(False)
f4()
#q3
def f3():
    v1=int(input("Enter value 1:"))
    v2=int(input("Enter value 2:"))
    v3=int(input("Enter value 3:"))
    s=0
    q1=v1//3
    q2=v2//3
    q3=v3//3
    r1=v1%3
    r2=v2%3
    r3=v3%3
    if(r1!=0 or (r1==0 and (q1%2!=0))):
        s=s+v1
    if(r2!=0 or (r2==0 and (q2%2!=0))):
        s=s+v2
    if(r3!=0 or (r3==0 and (q3%2!=0))):
        s=s+v3
    print(s)
    return
f3()
#q2
def f2():
    i=int(input("Enter integer:"))
    #input vector in form (n1,n2,n3....)
    s=input("Enter vectors of nos:")
    n=re.findall(r"\((\d+(?:,\d+)*)\)", s)
    n = [part.split(',') for part in n]
    print(n)
    ct=0
    for j in n:
        for k in j:
            if k==str(i):
                ct=ct+1
    print(ct)
    return
f2()

#partC
#q1
a=(np.array([1,2,3]))
b=(np.array([4,5,6]))
d=pd.DataFrame([a,b])
print(d)
#q2
mat2=np.arange(1,26).reshape(5,5)
print(mat2)
#q3
print(mat2[1:3,1:3])