from datetime import datetime
from time import sleep
from cabecalho import

inicio('71', 'Caixa Eletrônico')

frase = ('R$100', 'R$50', 'R$20', 'R$10', 'R$5', 'R$2', 'R$1') 
n = (100, 50, 20, 10, 5, 2, 1)  
cedula = list()
cedula1 = list()
frase1 = list()
num = list()
rest = list()
valor1 = 0

for c in range(0, len(n)):
    frase1.append(frase[c])
    cedula.append(0)
    cedula1.append(0)
    num.append(0)
    rest.append(0)

print()

for c in range(0, len(n)):
    while True:
        opc = input('Informe o número de cédulas de {}: '.format(frase[c]))
        if opc.isnumeric():
            opc = int(opc)
            break
        else:
            print('Isso não é um valor')

    cedula[c] = opc
    valor1 += cedula[c] * n[c]

print('\nSALDO DISPONÍVEL NO CAIXA ELETRÔNICO R${:.2f}'.format(valor1))
while True:
    hora = datetime.today().hour
    opc = ' '

    for c in range(0, len(n)):
        if cedula[c] > 0:
            frase1[c] = frase[c]
        else:
            frase1[c] = ''

    for c in range(0, len(n)):
        cedula1[c] = cedula[c]
        num[c] = 0

    print('\n' + '==========================' * 2)
    print(' ' * 17 + 'CAIXA ELETRÔNICO')
    print('NOTAS DISPONÍVEIS: ', end='')
    for c in range(0, len(n)):
        print('{}'.format(frase1[c]), end=' ')
    print('\n' + '==========================' * 2)

    while True:
        valor = input('SAQUE R$: ')
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('Dado invalido')

    if valor1 >= valor and valor1 > 0:
        for c in range(0, len(n) - 1):

            if cedula1[c] > 0:
                num[c] = valor // n[c]
                rest[c] = valor % n[c]

                if num[c] < cedula1[c]:
                    cedula1[c] -= num[c]
                    valor = rest[c]
                else:
                    num[c] = cedula1[c]
                    valor -= cedula1[c] * n[c]
                    cedula1[c] = 0

        if cedula1[len(n) - 1] > 0:
            if valor <= cedula1[len(n) - 1]:
                num[len(n) - 1] = valor
                rest[len(n) - 1] = 0
                cedula1[len(n) - 1] -= num[len(n) - 1]
                valor1 = 0

                for c in range(0, len(n)):
                    cedula[c] = cedula1[c]
                    valor1 += cedula1[c] * n[c]

                print('==' * 14)
                print('Saque feito com sucesso')
                print('\nCONTANDO CÉDULAS...\n')
                sleep(2)
                for d in range(0, len(n)):
                    print('CÉDULAS DE {}: {}'.format(frase[d], num[d]))
                print('==' * 14 + '\n')
                while True:
                    opc = input('DESEJA REALIZAR OUTRO SAQUE? (S/N): ')
                    if opc not in '\n':
                        opc = opc[0].lower().strip()
                    else:
                        print('Dado invalido')
                    if opc == 'n' or opc == 's':
                        break
            else:
                print('Saldo do caixa insuficiente')
                print('SAQUE NÃO REALIZADO!')
                print('==' * 14 + '\n')
                while True:
                    opc = input('TENTAR NOVAMENTE? (S/N): ')
                    if opc not in '\n':
                        opc = opc[0].lower().strip()
                    else:
                        print('DADO INVÁLIDO!')
                    if opc == 'n' or opc == 's':
                        break

    else:
        print('Saldo do caixa insuficiente')
        print('SAQUE NÃO REALIZADO!')
        print('==' * 14 + '\n')
        while True:
            opc = input('TENTAR NOVAMENTE? (S/N): ')
            if opc not in '\n':
                opc = opc[0].lower().strip()
            else:
                print('DADO INVÁLIDO!')
            if opc == 'n' or opc == 's':
                break

    if opc == 'n':
        print()
        if 6 <= hora <= 12:
            print('TENHA UMA BOM DIA!')
        elif 12 < hora < 18:
            print('TENHA UMA BOA TARDE!')
        else:
            print('TENHA UMA BOA NOITE!')
        print('OBRIGADO!\nVOLTE SEMPRE.')
        break


fim()
