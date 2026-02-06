a=int(input("Enter no:"))
b=a
d=a
n=0
while d!=0:
    d=d//10
    n+=1
k=0
while a!=0:
    k=k+((a%10)**n)
    a=a//10
if k==b:
    print("It is armstrong")
else:
    print("It is not armstrong")
