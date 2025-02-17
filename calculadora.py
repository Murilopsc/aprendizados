while True:
    numero_1 = input('Digite o primeiro número ')
    operadores = input('Digite o operador (+-*/%) ')
    numero_2 = input('Digite o segundo número ')

    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Digite um número para fazer a operação')
        continue

    operadores_permitidos = ('+','-','*','/','%')

    if operadores not in operadores_permitidos:
        print('Operador não permitido')
        continue
    
    if len(operadores) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta confira o resultado abaixo...')
    if operadores == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    if operadores == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    if operadores == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    if operadores == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    if operadores == '%':
        print(f'{num_1_float} % {num_2_float} = ', (num_1_float * num_2_float)/100)


    sair = input('Deseja sair? Digite [S]air ').lower() .startswith('s')
    if sair is True:
        break