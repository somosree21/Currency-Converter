from tkinter import  *
from tkinter import ttk,messagebox

with open('currency.txt') as f:
    a=f.readlines()
cur=[]
inv=[]
conv=[]
for i in a:
    word=i.split()
    cur.append(word[0])
    conv.append(word[3])
cur.append("INDIAN")
def fromcurrency(n):
    flag=0
    for i in cur:
        if n==i:
            flag=1
            print(f"CONVERTING FROM {n}")
    if flag==0:
        print("CURRENCY NOT IN LiST")
        quit()

def tocurrency(n):
    flag=0
    for i in cur:
        if n==i:
            flag=1
            print(f"CONVERTING TO {n}")
            break
    if flag==0:
        print("CURRENCY NOT IN LiST")
        quit()
def getindex(cur,a):
    if a == 'INDIAN':
        return  0
    obj=list(enumerate(cur))
    for item in obj:
        if item[1]==a:
            return item[0]

def convert(a,b,aindex,bindex,lst,x):
    p = float(lst[aindex])
    q = float(lst[bindex])
    if a!='INDIAN' and b!='INDIAN':
        ans=((x*p)/q)
        return  ans
    elif a=='INDIAN':
        return x/q
    else:
        return x*p
print("WELCOME TO CURRENCY CONVERTER!!")
n=input("FROM WHAT CURRENCY DO YOU WISH TO CONVERT?\n")
fromcurrency(n)
m=input("TO WHAT CURRENCY DO YOU WISH TO CONVERT?\n")
tocurrency(m)
l=float(input("HOW MUCH DO YOU WISH TO CONVERT?\n"))
if n==m:
    print(f"{l} {n} is equal to {l} {m}")
    quit()
g= getindex(cur,n)
h= getindex(cur,m)
result = convert(n, m, g, h, conv, l)
print(f"{l} {n} is equal to {result} {m}")


