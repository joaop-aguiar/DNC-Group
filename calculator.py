number_1 = float(input('Escolha um número: '))
operation = str(input('Escolha sua operação: ')).lower()
number_2 = float(input('Escolha o segundo número: '))

while True:
    if operation == 'x': 
        result = number_1 * number_2
        print(result)
        break
    elif operation == '/': 
        result = number_1 / number_2
        print(result)
        break
    elif operation == '-':  
        result = number_1 - number_2
        print(result)
        break
    elif operation == '+': 
        result = number_1 + number_2
        print(result)
        break
    else:
        operation = str(input('Error! Operação inválida, digite uma operação válida: ')).lower()
        


