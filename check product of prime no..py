def check_prime(m):
    flag=0
    if m==0:
        flag=1
    elif m==1:
        flag=1
    else:
        for i in range(2,int(m/2)+1):
            if m%i==0:
                flag=1
                break
    if flag==0:
        return 1
    else:
        return 0
result=[]
m=int(input("enter a number"))
flag=0
k=m+1
while k<1:
    flag=check_prime(m)
    if flag==1:
        result.append(k)
    else:
        k=k+1
sum=0
for i in range(m+1,k):
    sum+=1
result.append(sum)
p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1
p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
prime_key=tuple(result)
print(prime_key)
