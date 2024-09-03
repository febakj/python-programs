tuple1=("apple","banana","cherry")
list1=list(tuple1)
list1.append("mango")
list1.insert(0,"kiwi")
list1[0]="pineapple"
tuple1=tuple(list1)
print(tuple1)
print(tuple1[1:])
if 'apple' in tuple1:
    print("yes, 'apple' is in this tuple1")'''
