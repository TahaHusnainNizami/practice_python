# sum program

a = int(input("enter a: "))
b = int(input("enter b: "))

sum = a + b
print("sum of a and b = " , sum)

# biling program

p1 = float(input("entre p1= "))
p2 = float(input("entre p2= "))
p3 = float(input("entre p3= "))

total_bil = p1 + p2 + p3
print(total_bil)

avg_price = (p1 + p2 + p3)/3
print(avg_price)

name = "superhero"
print(name.find('s' or 'S'))

# print odd number 1  20

for i in range(1 , 21):
    if (i % 2 !=0):
        print(i)

# talble of 3

i = 1
while i<=10:
    print('3 *' , i ,'=' ,3*i )
    i +=1


# employee record using list of tuple

record = [(1,"ali",1000),(2,'john',2000),(3,'auon',3000)]
search = int(input('id: '))

for emp in record:
    if emp[0] == search:
        print(emp)
        break
else:
     print("invalid id")

