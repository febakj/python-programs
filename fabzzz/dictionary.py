dict1= {"name": "anu","age" : 23}
dict2={"names" : "anna", "ages" : 21}
dict3 = dict1 | dict2
print(dict3)
dict4={**dict1, **dict2}
print(dict4)
dict1.update(dict2)
print(dict2)
print(dict1.keys())
#x=dict1["name"]
print(dict1["name"])
dict1["name"]="ammu"
print(dict1)

'''#x=dict1["name"]
#dict1.update({"name":"anna"})
#print(dict1)



#def merge(child1,child2):
'''
'''child1 : {
        "name" : "anu",
        "age" : 23
    }
child2 : {
        "name" : "ammu",
        "age" : 28
    }
    #return(child2.update(child1))

family ={**child1 , **child2}
print(family)'''