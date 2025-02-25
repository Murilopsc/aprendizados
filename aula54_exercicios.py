"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opcão ')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [s]air ')
    if opcao == 'i':
        os.system('cls')
        valor = input('item :')
        lista.append(valor)
    elif opcao == 'a':
        try:
            indece_del = int(input('Selecione o item para apagar: '))
            if 0 <= indece_del < len(lista):
                lista.pop(indece_del)
                print('Item apagado...')
            else:
                print('Item não existe')
        except ValueError:
            print('Digite um número valido')

    elif opcao == 'l':
        for indice, item in enumerate(lista):
            print(indice, item)
    elif opcao == 's':
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Por favor escolha i, a, l ou s')

