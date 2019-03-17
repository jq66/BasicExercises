#Adds two numbers
def add(a, b):
    return a + b

#Substracts two numbers
def substract(a, b):
    return a - b

#Multiplies two numbers
def multiply(a, b):
    return a * b

#Divides two numbers
def divide(a, b):
    return a / b

print('What do you want to do?')
print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')

choice = int(input('Choose one of 4: '))
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

def calculating():
    if choice == 1:
        print(num1, ' + ', num2, ' = ', num1+num2)
    elif choice == 2:
        print(num1, ' - ', num2, ' = ', num1-num2)
    elif choice == 3:
        print(num1, ' * ', num2, ' = ', num1*num2)
    elif choice == 4:
        print(num1, ' / ', num2, ' = ', num1/num2)
    else:
        print('You didn\'t choose one of 4!')

calculating()
