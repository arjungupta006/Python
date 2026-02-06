a=int(input())
temp=0
while(a!=0):
    temp=temp+a%10
    a=a//10
print(temp,end="")