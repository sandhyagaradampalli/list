# a=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
# k=int(input("enter the removing last elements:"))
# i=0
# v=0
# while i<len(a):
#     v=v+1
#     i=i+1
# v=v-k
# j=0
# c=[]
# while j<v:
#     n=a[j]
#     c.append(n)
#     j=j+1
# print(c)




# a=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
# k=int(input("enter the removing last elements:"))
# for i in range(len(a)):
#     s=a[:len(a)-k]
# print(s)
# o/p:[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]





a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
i=0
k=int(input())
b=[]
while i<len(a)-k:
    b.append(a[i])
    i=i+1
print(b)


