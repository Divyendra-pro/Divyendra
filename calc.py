print('Welcome to the simple project of python calculator')
num1=float(input('Enter the first number: '))
op = input('Enter the second number: ')
num2=float(input('Enter the second number: '))

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num1)
elif op == '/':
    print(num1/num2)
else:
    print('Enter a valid input')
    
