# # create class student that take name and marks of 3 students as argument in constructor.Then creates method to find avg of marks
# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):
#         return sum(self.marks)/len(self.marks)

# s1 = Students("ali", [80,98,8765])
# s2 = Students("taha", [90,85,92])
# s3 = Students("ahmed", [70,75,80])
# print(s1.avg())
# print(s2.avg())
# print(s3.avg())


# create class account in which we debit and credit methods are used .
class Account:
    def __init__(self, bal , acc):
        self.bal = bal
        self.acc = acc

    def debit(self, amount):
        self.bal -= amount
        print(f"Your account has been debited with Rs. {amount}. Your new balance is Rs. {self.bal}.")

    def credit(self, amount):
        self.bal += amount
        print(f"Your account has been credited with Rs. {amount}. Your new balance is Rs. {self.bal}.")


acc1 = Account(500000, 98760976)
acc1.debit(20000)
acc1.credit(50000)
