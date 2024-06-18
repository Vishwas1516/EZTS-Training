l= [64, 34, 25, 5, 22, 11, 90, 12]

n = len(l)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if l[j] < l[min_index]:
            min_index = j
    min_value = l.pop(min_index)
    l.insert(i, min_value)

print("Sorted array:", l)
