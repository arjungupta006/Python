a=int(input())
temp=0
if a==1 | a==2:
    print("itr is  prime")
if a>2:
    for i in range(2,a):
        if a%i==0:
            print("It is not prime")
            break
    else:
        print("It is prime")
        