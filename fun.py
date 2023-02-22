# def counting (list):
#     c=0
#     i=0
#     while i<len(list):
#         if list[i][0]==list[i][-1] and len(list)>=2:
#             c+=1
#         i=i+1
#     return c
# print(counting(["abc",'xyz','aba','1221']))


# def counting (list):
#     c=0
#     for i in list:
#         if i[0]==i[-1] and len(i)>1:
#             c+=1
#     return c
# print(counting(['abc','xyz','aba','1221']))


# def maximum(a,b,c):
#     if (a>=b) and (b>=c):
#         largest=a
#     elif (b>=a) and (b>=c):
#         largest=b
#     else:
#         largest=c
#     return largest
# a,b,c=10,14,12
# print(maximum(a,b,c))

# def maximum(a,b,c):
#     list=[a,b,c]
#     list.sort()
#     return list[-1]
# a,b,c=10,14,12
# print(maximum(a,b,c))



# a=[[1, 2], [2, 4]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#        c=a.count(a[i])
#        d=a.count(a[j])
#        j=j+1
#     b.append(c,d)
#     i=i+1
# print(b)

def sum(a,b):
    k=int(a)+int(b)
    return "'"+str(k)+"'"
a=input()
b=input()
print(sum(a,b))
    
