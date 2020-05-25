def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
print('+ for addition \n - for subtraction \n * for multiplication \n / for division')
operator = input('What operation would you like to perform?: ')
if operator == '+':
    add(num1, num2)
elif operator == '-':
    sub(num1, num2)
elif operator == '*':
    mult(num1, num2)
elif operator == '/':
    div(num1, num2)
else:
    print('Invalid operator. Run again')

    