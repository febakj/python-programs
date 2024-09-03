thislist=["apple","orange","mango"]
for x in thislist:
    print(x)'''

'''thislist=["apple","orange","mango"]
for i in range(len(thislist)):
    print(i)'''

'''thislist=["apple","orange","mango"]
for i in range(len(thislist)):
    print(thislist[i])'''


'''thislist=["apple","orange","mango"]
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1'''



'''thislist=["apple","orange","mango"]
newlist=[]
for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)'''



'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)'''


'''thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)'''



'''thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)'''


'''list comprehension'''

'''thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]