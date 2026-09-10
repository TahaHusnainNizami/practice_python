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
class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")

class Toyota(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # Calling the parent class constructor by super() method
    

c1 = Toyota('land cruiser', 'desiel engine' )
print(c1.name, c1.type)