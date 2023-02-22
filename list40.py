# a=[[1, 2, 4],
#    [2, 4, 4],
#    [1, 2]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum1=0
#     while j<len(a[i]):
#         sum1+=a[i][j]
#         j=j+1
#     b.append(sum1)
#     i=i+1
# print(b)

# o/p:[7,10,3]
        
a=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
b=[]
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        s=s+a[j][i]
        j=j+1
    b.append(s)
    i=i+1
print(b)

# o/p:[4, 8, 8]

