set1={"apple","banana","cherry"}
set2={"red","yellow","green","apple","banana"}
#set1.remove("apple")
#set1.pop()
set1.update(set2)
#set3=set2-set1
print(set1)

set1={1,2,3,4,5}
oldvalue=2
newvalue=6
if oldvalue in set1:
    set1.remove(oldvalue)
    set1.add(newvalue)
print(set1)