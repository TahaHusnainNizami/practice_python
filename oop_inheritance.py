# # multilevel inheritance
# class car:
#     @staticmethod
#     def start():
#         print("Car is starting")

#     @staticmethod
#     def stop():
#         print("Car is stopping")

# class electric_car(car):
#     def __init__(self, brand , name):
#         self.brand = brand
#         self.name = name

# class hybrid_car(car):
#     def __init__(self, brand , name):
#         self.brand = brand
#         self.name = name

# c1 = electric_car("Tesla", "Model S")
# c2 = hybrid_car("Toyota", "Prius")
# c1.start()
# print(c1.brand, c1.name)
# c1.stop()
# c2.start()
# print(c2.brand, c2.name)
# c2.stop()

# # multiple inheritance
# class A:
#     varA = 'welcome to class A'

# class B:
#     varB = 'welcome to class B'

# class C(A, B):
#     varC = 'welcome to class C'

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# # public and private entities
# class Account:
#     def __init__(self, name, balance):
#         self.name = name  # public attribute
#         self.__balance = balance  # private attribute

#     def show_balance(self):
#         print(f"Account holder: {self.name}, Balance: {self.__balance}")

# acc1 = Account("John Doe", 1000)
# acc1.show_balance()  # Accessing public method to show balance

# # super method --> use to access parent class methods/constructors in child class
# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car is starting")

#     @staticmethod
#     def stop():
#         print("Car is stopping")

# class Toyota(car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)  # Calling the parent class constructor by super() method
    

# c1 = Toyota('land cruiser', 'desiel engine' )
# print(c1.name, c1.type)


# class decorator
class Person:
    name = 'anonymous'

    @classmethod  
    def new_name(cls, name):  # classmethod is used to define a method that is bound to the class and not the instance of the class. It takes the class itself as the first argument (cls) instead of the instance (self). This allows you to modify class-level attributes or call other class methods.
        cls.name = name

p1 = Person()
p1.new_name('taha husnain')
print(p1.name)  # Output: taha husnain

#property decorator
class Student:
    def __init__(self, phy , chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property # property decorator is used to define a method that can be accessed like an attribute. It allows you to create read-only attributes or computed properties without needing to call a method explicitly.
    def percentage(self):
        return f"{(self.phy + self.chem + self.math) / 3:.2f}%"

std1 = Student(85,77,98)
print(std1.percentage)  

std1.chem = 67
print(std1.percentage)  