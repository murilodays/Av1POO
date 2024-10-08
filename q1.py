numero = int(input("Insira um número para descobrir a tabuada: "))

if (numero >= 1 and numero <= 10):
    contador = 1
    while(contador < 11):
        print(f'{numero} x {contador} = {numero * contador}')
        contador = contador + 1
else:
    print("O número deve ser entre 1 e 10!")



