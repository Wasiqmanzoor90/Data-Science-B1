# # #output function
# # print("hello world")

# # #addition
# # a = 12
# # b = 10
# # z = a+b
# # print(z)

# # #subtraction
# # c = 19
# # d = 10
# # e = c-d
# # print(e)

# # #multiplication
# # f = 3
# # g = 5
# # h = f*g
# # print(h)

# # #division
# # de = 8
# # cd = 4
# # zd = de/cd
# # print(zd)

# # #If we have to find reminder
# # fg = 8
# # cg = 4
# # wa = fg%cg
# # print(wa)


# # #exponent(raise power)
# # n1 = 2 ** 3
# # print(n1)

# # #floor division
# # n2 = 7 // 2
# # print(n2)

# #addition
# # a = 8
# # b = 8
# # z = a-b
# # print(z)

# #subtraction
# # x = 8
# # y = 2
# # yz = a%b
# # print(yz)


# # xyz = 5**5
# # print(xyz)


# # b = 7/3
# # print(b)

# # c = 7//3
# # print(c)


# #its a int data type
# a = 10
# print(a)

# #its is string data type
# b = '20'
# print(b)

# # its bool data type
# c = True
# print(type(c))

# #its float data type
# d = 24.65
# print(type(d))

#comparison
# a = 10
# b = a
# print(b)

# #equal to
# a =20
# b=30
# print(a == b)

# #greater than equal to
# c = 40
# d =20
# print(c>=d)

# #less than equal to 
# c = 30
# d = 30
# print(c<=d)

# #greate than equal to
# age =18
# print(age>=18)


# #not equal to
# df =20
# de = 10
# print(df!=de)


#Assigment operator
# a = 10
# b = a
# print(b)

# a = 10
# # a = a + 5 
# a += 5
# print(a)

# b = 14
# # b = b - 4
# b-=4
# print(b)

# c = 4
# c*=4
# print(c)

# f = 6
# f/=6
# print(f)

# n = 7
# n%=3
# print

# l = 9
# l%=2
# print(l)

# k = 11
# k%=3
# print(k)

# o = 13
# o%=3
# print(o)

# j = 17
# j%=3
# print(j)

# a =input("Enter your name:-")
# print(a)

# a= 'aiman'
# print(a)


# b= 'aqib'
# print(b)

# c= 12
# print(c)
# a = input("enter your name")
# print(a)

#list is an an data type which is used to store multiple values in a single variable, its indexed
#its ordered and allows duplicate values, its mutable(changeble)

lst = ['aiman','aqib',12,67.89,True,13,'reeba','adnan','reeba']
lst[6] = 'jasira'  #update by index 
lst.append("Hena")  #add by direct value where we dont give index so thats why it comes in last position
lst.insert(5,'adnan malik')  #add by index at particular place
lst.remove('adnan malik')   #remove by direct by value
lst.pop(1) #remove by index
print(lst)