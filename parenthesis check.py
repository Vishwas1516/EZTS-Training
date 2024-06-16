class stack:
    def __init__(self):
        self.items =[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

e="[3+7{52/11(3+5)}]"
s=stack()
ob='[{('
cb=')}]'
flag = 0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x=s.pop()
        if x=="{" and i=="}":
            pass
        elif x=="(" and i==")":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag=1
            
            break
if flag==0:
    print("valid")
else:
    print("invalid")
