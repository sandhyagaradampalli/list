# a=[34.67, 12, -94.89, 'Python', 0, 'C#']
# c=[]
# for i in a:
#     if type(i)==int:
#         c.append(i)
#         print(c)


a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
c=[]
while i<len(a):
    if(type(i)==int):
        c.append(i)
    i=i+1
print(c)



