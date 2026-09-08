## class and object
# class Students:   # class
#     name = 'taha husnain'

# s1 = Students()  # object
# print(s1.name)



# creating class with constructor
# class Students:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

# s1 = Students('ali' , 21)
# print(s1.name , s1.age)

# s2 = Students('taha' , 22)
# print(s2.name , s2.age)



# # class and object attributes
# class Car:
#     category = 'vechicle' # class attribute

#     def __init__(self , name , brand):
#         self.name = name # object attribute
#         self.brand = brand # object attribute

# c1 = Car('land cruiser' , ' toyota')
# print(c1.category , c1.name , c1.brand)

# class with methods
class Car:
    category = 'vechicle' # class attribute

    def __init__(self , name , brand):
        self.name = name # object attribute
        self.brand = brand # object attribute

    def car_category(self):  # methods are functions that are defined inside a class
        return self.name , self.brand, self.category

c1 = Car('land cruiser' , ' toyota')
print(c1.car_category())

