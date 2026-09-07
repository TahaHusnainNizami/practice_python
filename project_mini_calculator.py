# project mini calculator

# numbers
a = float(input('a= '))
b = float(input('b= '))

# operators
operator = input("select operator: + , - , * , / ,% ,** = ")

# operations
if operator == '+':
    print('addition= ', a+b)
    
elif operator == '-':
    print('subtraction= ', a-b)
elif operator == '*':
    print('multiplication= ', a*b)
elif operator == '/':
    print('division= ', a/b)
elif operator == '&':
    if b !=0:
        print('modulus= ', a%b)
    else:
        print("value of variable is zero")
elif operator == '**':
    print('power= ', a**b)
    
else:
    print("invalid ooperator")
