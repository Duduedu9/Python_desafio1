resp= 'S'
soma= quant = média= maior= menor= 0
while resp in 'Ss':
    num=int(input('Digite um numero: '))
    soma+=num
    quant+=1
    if quant == 1:
        maior = menor= num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor= num
    resp= str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média=soma / quant
print('Você digitou {} numeros e a média foi {}'.format(num, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))