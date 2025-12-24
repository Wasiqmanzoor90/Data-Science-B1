# #strring
# a = 'Musa'
# print(type(a))

# #int
# b = 12
# print(type(b))

# #float
# c = 12.7
# print(type(c))


# d = True
# print(type(d))
#so list basically stores multiple items in a single variable, its ordered, its indexed , its mutbale
# lst = ["Musa",12.3,45,True]
# lst[1]='Seerat'  #update
# lst.append('hanan')  #when add without index
# lst.insert(1,'wasiq') #when we add on particular index
# lst.remove('wasiq')  #when we remove direct with value
# lst.pop(0)  #when we remove with index
# print(lst)

#so tuple basically in a single variable, its orderd, its inexed, its un changable
# tple = ("Musa",12.3,45,True,"Musa")
# print(tple)

#so in set we store multiple values but its un orders, un indexed , and sometimes mutable
# vset = {"Musa",12.3,45,True,"Musa"}
# vset.add("owais")
# vset.remove('Musa')
# print(vset)

#We store multiple items in dict in the form of key value values, its orders, its mutable
dicto = {
    "name":"wasiq",
    "Roll no":24,
    "Pin code": 190001,
    'Pin code':190002,
}
dicto['name']='seerat' # we update here
dicto['city']='srinagr'  # we add 
dicto.pop('name') #we delete
print(dicto)