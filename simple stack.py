class stack:
    def __init__(self):
        self.items =[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

wardoor = stack()
wardoor.push(100)
wardoor.push(200)
wardoor.push(200)
print(wardoor.size())
