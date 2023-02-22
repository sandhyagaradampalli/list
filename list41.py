# a=[[0, 1, 2], [2, 4, 5]]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a):
#         b=a[j][i]
#         s=s+b
#         j=j+1
#     c.append(s)
#     i=i+1
# print(c)





a=[[0, 1, 2],
   [2, 4, 5], 
   [2, 3, 4]]
i=0
count=0
c=[]
count12=0
while i<len(a):
    count+=1
    j=0
    count12=0
    while j<len(a[i]):
        count12+=1
        j=j+1
    i=i+1
c.append(count)
c.append(count12)
print(tuple(c))









