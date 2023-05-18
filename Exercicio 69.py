print('='*40)
print('Validação de dados'.center(40))
print('='*40)

while True:
    idade = int(input('Qual a idade '))
    sexo = ' '
    print('-'*20)
    resposta = ' '
    th = 0
    maior_idade = 0
    mulher_menor = 0

    while sexo not in 'MmFf':
        sexo = str(input('Qual o sexo? [M/F]: ')).strip().upper()[0]
        if idade >= 18:
            maior_idade += 1
        
        if sexo == 'M':
            th += 1
        
        elif sexo == 'F' and idade < 20:
            mulher_menor += 1


    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if resposta == 'N':
        print('Saindo do programa...')
        break

print(f'O total de homens é {th}')
print(f'O total de mulheres com menos de 18 anos é {mulher_menor}')
print(f'O total de pessoas maiores de 18 é {maior_idade}')
print('Fim')    