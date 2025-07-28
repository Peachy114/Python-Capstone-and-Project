def add (n1, n2) :
    return n1 + n2

def subtract (n1, n2) :
    return n1 - n2

def multiply (n1, n2) :
    return n1 * n2

def divide (n1, n2) :
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

accumulate = True
num1 = float(input('Whats the first number? '))

while accumulate:
    for symbols in operations:
        print(symbols)
    operation_symbols = input('pick a symbol ')
    num2 = float(input('whats the next number? '))
    answer = round(operations[operation_symbols](num1, num2), 2)

    question = input(f'y to continue calculate with {answer}, n to exit ')

    if question == 'y':
        num1 = answer
    else:
        print('Thankyou!')
        accumulate = False


