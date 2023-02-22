# list=[['g','f','g'],['i','s'],['b','e','s','t']]
# for i in list:
#     for j in i:
#         print(j,end="")   
        
        
        
        
# list=[['g','f','g'],['i','s'],['b','e','s','t']] 
# st=" "
# for i in list:
#     st=st+''.join(i)
# print(st)   


list=[['g','f','g'],['i','s'],['b','e','s','t']] 
i=0
a=""
while i<len(list):
    # s=list[i]
    j=0
    while j<len(list[i]):
        a=a+str(list[i][j])
        j=j+1
    i=i+1
print(a)




