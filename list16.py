# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=0
# c=[]
# while i<len(a)-1:
#     b=a[i+1]
#     d=a[i]
#     e=b-d
#     c.append(e)
#     i=i+1
# print(c)


# o/p:[1, 1, 1, 1, 1, 1, 1, 1, 1]


a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
c=[]
while i<len(a)-1:
    b=a[i+1]-a[i]
    c.append(b)
    i=i+1
print(c)

