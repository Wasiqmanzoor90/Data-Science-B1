#file handling is a process of creating, reading, updating, and deleting files using programming languages.
#r,w,a



#w reprsents writing a file
# file = open("file.txt", "w")
# file.write("Hello, this is a file handling example.")
# file.close()

# r represents reading a file
# file = open("file.txt", "r")
# # content = file.read()
# line = file.readline()
# print(line)
# file.close()


# file = open('file.txt','a')
# file.write("hello again")
# file.close()




#with open automatically closes the file 

# with open('file.txt',"r") as f:
#     data = f.read()
#     print(data)



# with open('file.txt',"w") as f:
#      f.write("Hello ahsan")
    

# with open(r"C:\Users\Dell\Desktop\file.txt",'w',encoding="utf8") as f:
#     f.write("Hello, World!")
    
# try:
#     with open(r"C:\Users\Dell\Desktop\fil.txt",'r',encoding="utf8") as f:
#         data=f.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found!")