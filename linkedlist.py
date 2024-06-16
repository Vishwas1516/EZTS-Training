class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
Head=Tail=Node(10)
Tail.next=Node(20)
Tail=Tail.next
Tail.next=Node(30)
Tail=Tail.next
Tail.next=Node(40)
Tail=Tail.next

print(Head)
print(Tail)
print(Head.next.next.next)
