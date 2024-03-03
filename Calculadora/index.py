import math
entrada = input('Deseja utilizar a calculadora?(S/N) ').upper()
while ( entrada == 'S'):
    print(' 1 - Simples\n 2 - Equação do segundo grau')
    entrada = input('Deseja realizar qual operação? ')
    if entrada == '2':
        a = int(input('Digite numero de A(x2): '))
        b = int(input('Digite o numero de B(x): '))
        c = int(input('digite o numero de C:'))
        x1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / 2 * a
        x2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / 2 * a
        print(x1, x2)
    elif entrada == '1':
        numeroA = int(input('Digite o primeiro numero: '))
        print(' 1 = Soma\n 2 = Subtração\n 3 = Divisão\n 4 = Multiplicação\n 5 = Porcentgem\n'' 6 = Fatorial\n '
              '7 = seno\n 8 = cosseno''\n 9 = tangente\n 10 = Raiz quadrada\n 11 = Binário\n 12 = Hexal')
        operacao = input('Escolha operação desejada: ')
        if operacao == '6':
            print('Resultado do fatorial de {} é {}'.format(numeroA, math.factorial(numeroA)))
        elif operacao == '7':
            print('Resultado do seno de {} é {}'.format(numeroA, math.sin(numeroA)))
        elif operacao == '8':
            print('Resultado do cosseno de {} é {}'.format(numeroA, math.cos(numeroA)))
        elif operacao == '9':
            print('Resultado do tangente de {} é {}'.format(numeroA, math.tan(numeroA)))
        elif operacao == '10':
            print('Resultado da raiz quadrada de {} é {}'.format(numeroA, math.sqrt(numeroA)))
        elif operacao == '11':
            print('O número {} convertido para binário é {}'.format(numeroA, bin(numeroA)))
        elif operacao == '10':
            print('O número {} convertido para octal é {}'.format(numeroA, oct(numeroA)))
        elif operacao == '10':
            print('O número {} convertido pra hexal é {}'.format(numeroA, hex(numeroA)))
        else:
            numeroB = int(input('Digite mais um numero: '))
            if operacao == '1':
                print('Resultado da soma: ', numeroA + numeroB)
            elif operacao == '2':
                print('Resultado da subtração: ', numeroA - numeroB)
            elif operacao == '3':
                print('Resultado da divisão: ', numeroA / numeroB)
            elif operacao == '4':
                print('Resultado da multiplicação: ', numeroA * numeroB)
            elif operacao == '5':
                print(numeroA, 'porcentos de ', numeroB, 'é: ', numeroA*numeroB/100)
            else:
                print('Operador não identificado')
    else:
        print('esse operador não existe')
    entrada = input('Deseja realizar nova operação?(S/N) ').upper()
print('Obrigado! Até a próxima')
