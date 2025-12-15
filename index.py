# a ='umer'
# print(a)

# b ='hanan'
# print(b)

# c ='ubaid'
# print(c)

# d ='ali'
# print(d)

# e ='wasiq'
# print(e)


# abc =['wasiq', 3.5, True, 'ubaid'] #we have created an list
# abc.append('umer') # we have added an element in the list using append function
# abc.remove(3.5) # we have removed an element from the list using remove function
# abc.insert(1,'hanan') # we have inserted an element at index 1 using insert function
# abc.pop(4) # we have removed the last element from the list using pop function
# abc[0]='burhan'
# print(abc)


#tuple
# So Basically Tuple is same as list but the only difference is that tuple is immutable means we cant change the value of tuple once it is created
# thistuple = ('umer',5.6,'hanan',True,'hanan')
# thistuple[0]='musaib'
# print(thistuple)


#set
# So Basically Set is a collection of unordered and unindexed elements
# We can not access the elements of set by referring to an index because sets are unordered the items has no defined order
# Sets are mutable means we can add or remove items from it but we can not change the items of set
# thisset ={'umer',3.4,True,'burhan','umer'}
# thisset.add('ali')
# thisset.remove('burhan')
# print(thisset)

#slicing
# thelist=['wasiq','ubaid',3.5,True,'hanan']
# print(thelist[1:5])

#dictionary
#it store data in key:value pairs
# thisdict = {
#     'name': 'umer',
#     'age': 25,
#     'gender': 'male',
#     'sex':'male'
# }
# thisdict['age']=26  #we can change the value of a key
# print(thisdict)

# thislist = ['apple','umer',3.5,10, True]
# thislist[1]='hanan'  #editing the value at index 1
# thislist.append('ubaid')
# thislist.insert(2,'burhan')
# thislist.remove('apple')
# thislist.pop(0)
# print(thislist)


# #tupple
# thistuple = ('umer',3.5,True,'hanan')
# print(thistuple[0])

#set
# thiset = {'umer',3.5,True,'hanan','umer'}
# thiset.add('ubaid')
# thiset.remove('hanan')
# print(thiset)

thisdict = {
    'Name': 'umer',
    'Age': 25,
    'Gender': 'male',
    'Sex': 'male'
}
thisdict['State'] ="kashmir"
thisdict['Name']='hanan'
thisdict.update({'Age':26})
thisdict.pop('Gender')
print(thisdict)