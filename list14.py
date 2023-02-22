l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max=1
min=1
for i in range(len(l)):
    length=len(l[i])
    if length>max:
        max=length
    if length<=min:
        min=length
print(max,l[max+1])
print(min,l[min-1])



