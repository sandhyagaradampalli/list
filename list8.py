# a=[6,1,3,5,6,3,1]
# b=list(set(a))
# p=1
# for i in b:
#     p=p*i
# print(p)



list=[6,1,3,5,6,3,1]
p=1
n=[]
for i in list:
    if i not in n:
        p=p*i
    n.append(i)
print(p)