# a=[3,8,9,4,5,0,5,0,3]
# i=0
# b=[]
# while i<len(a):
#     c=a[i]
#     d=c+3
#     b.append(d)
#     i=i+1
# print(b)


a=[3,8,9,4,5,0,5,0,3]
i=0
b=[]
c=int(input("enter the adding element:"))
while i<len(a):
    d=a[i]+c
    b.append(d)
    i=i+1
print(b)

o/p:[6, 11, 12, 7, 8, 3, 8, 3, 6]