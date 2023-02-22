   
a=[[0,1,2,0,0],[2,3,4,0,0],[3,4,5,6,0],[7,8,9,10,11],[12,13,14,0,0]]
i=0
b=[]
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        s=s+a[j][i]
        c=s/len(a)
        j=j+1
    b.append(c)
    i=i+1
print(b)

# o/p:[4.8, 5.8, 6.8, 8.0, 11.0]

# a=[[0,1,2,0,0],[2,3,4,0,0],[3,4,5,6,0],[7,8,9,10,11],[12,13,14,0,0]]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     s=0
#     k=0
#     while j<len(a):
#         b=a[j][i]
#         if type(b)==int:
#             s=s+b
#         if b=="":
#             k=k+0
#         else:
#             k=k+1
#         j=j+1
#     avg=s/k
#     c.append(avg)
#     i=i+1
# print(c)