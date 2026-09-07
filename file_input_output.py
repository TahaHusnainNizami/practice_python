# # read mode
# f = open("demo.txt" , 'r')
# data = f.read()
# print(data)
# f.close()

# # write mode
# f = open("demo.txt" , 'w')
# data = f.write("file input and output helps to store data in files and read and write form that file")
# print(data)
# f.close()

# append mode
# f = open("demo.txt" , 'a')
# data = f.write("\nfile input and output helps to store data in files and read and write form that file")
# print(data)
# f.close()

#read and overwrite mode without turncate
# f = open("demo.txt" , 'r+')
# f.write("abc")
# print(f.read())
# f.close()

#read and overwrite mode with turncate
# f = open("demo.txt" , 'w+')
# f.write("abc")
# f.read()
# f.close()

# #read and append mode
# f = open("demo.txt" , 'a+')
# print(f.read())
# f.write("fgh")
# f.close()

# file opening and closing using with statement

# with open("demo.txt" , 'r') as f:
#     print(f.read())

# with open("demo.txt" , 'w') as f:
#     f.write('abc')


# moduling os module to delete a file
import os

os.remove("demo.txt")