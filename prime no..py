m=int(input("enter the message:"))
flag=0
if m==0:
    flag==1
elif m==1:
    flag==0
else:
    for i in range(2,m):
        if m%1==0:
            flag=1
            break
if flag==1:
    print("invalid message")
else:
    print("valid message")
