# a=[1,2,2,5,8,4,4,8]
# b=list(set(a))
# c=0
# while c<len(b):
#     c=c+1
# print(c)




a=[1,2,2,5,8,4,4,8]
b=[]
c=0
for item in a:
    if item not in b:
        c=c+1
        b.append(item)
print(c)
 

 
 

