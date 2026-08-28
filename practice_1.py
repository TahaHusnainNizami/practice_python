print("HELLO , Taha")
name=input('whats your age')
print('Taha',name,',you r young good for u')

print(24/4) #give ans with decimal values
print(24//4) # does not give ans with decimal values
print(21%2)
print(3*4-7+99/5)

# logical condition

nic_age=18
your_age=int(input('whats your age: '))
print('eligible for making a nic , ', nic_age==your_age)

a=6
b=9
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

# conditions

nic = 18
your_age = int(input('whats your age: '))

if  your_age >= nic :
    print('congrats you r eligible')
elif your_age <=12 :
    print('you should make b-form')
else:
    print('you r not eligible...')

def cnic(your_age):
    nic = 18

    if  your_age >= nic :
        print('congrats you r eligible')
    elif your_age <=12 :
        print('you should make b-form')
    else:
        print('you r not eligible...')
cnic(23)

# while loop
a=10
while(a>=1):
    print(a)
    a -=1

# for loop
for a in range(0,11):
    print(a)

# array
arry_of_days = ['mon','tues','wed' ,'thur','fri','sat','sun']
for a in arry_of_days:
    print(a)

arry_of_days = ['mon','tues','wed' ,'thur','fri','sat','sun']
for a in arry_of_days:
    if(a=='wed'):break
    print(a)

arry_of_days = ['mon','tues','wed' ,'thur','fri','sat','sun']
for a in arry_of_days:
    if(a=='fri'):continue # continue mean it skips that thing which you wnat to skip
    print(a)