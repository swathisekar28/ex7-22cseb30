list=[]
for i in range(0,8):
    list.append(i)
list.append(7)
list.append(5)
print("created list which contains duplicate elements:",list)
x=set(list)
print("after creating set removes duplicate elements:",x)
