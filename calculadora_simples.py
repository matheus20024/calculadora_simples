print('Vamos fazer uma calculadora! Ok.')
number1 = float(input("Digite o primeiro valor: "))
number2 = float(input("Digite o segundo valor: "))
print('Escolha uma operação! ')
print("1 - Adição")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multpiplicação")
print("5 - potenciação")
operacao = int(input('Digite a operação que deseja fazer? '))
if operacao == 1:
    resultado = number1 + number2
    print(f'O resultado da adição é:{resultado}')
elif operacao == 2:
    resultado = number1 - number2
    print(f'O resultado da subtração é: {resultado}')
elif operacao == 3:
    resultado = number1 // number2
    print(f'O resultado da subtração é: {resultado}')
elif operacao == 4:
    resultado = number1 * number2
    print(f'O resultado da multiplicação é: {resultado}')
elif operacao == 5:
    resultado = number1 ** number2
    print(f'O resultado da potenciação é: {resultado}') 
else: 
    print('operação invalida')