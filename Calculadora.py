
#Função que chama o input do numero já com restrições:
def insert_number(message):
    while True:
        try:
            return float(input(f'{message}: '))
        except ValueError:
            print("❌ Invalid number. Please try again.")

#Função que chama a operation já com restrições:
def call_operation(message):
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input(f'{message} (+, -, *, /): ')
        if op in valid_operations:
            return op
        else:
            print("❌ Invalid operation. Please choose one of +, -, *, /")

#Função que executa o calculo
def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return round(a * b,4)  #round arredonda o valor
    elif op == '/':
        if b != 0:
            return round(a / b,4) #round arredonda o valor
        else:
            return "❌ Cannot divide by zero."

# Main
while True:
    first_value = insert_number('Insert the first number')
    operation = call_operation('Insert an operation')
    second_value = insert_number('Insert the second number')

    result = calculate(first_value, operation, second_value)

    print(f'Result: {result}')
    print('-'*30)
