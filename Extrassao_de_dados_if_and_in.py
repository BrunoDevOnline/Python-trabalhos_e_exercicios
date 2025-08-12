somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0


for p in range(1, 5):
    print(f'======== {p} Pessoa ==========')
    nome = str(input('Qual nome dela(a)?'))
    idade = int(input('Qual idade dele(a)?'))
    sexo = str(input('Qual sexo dessa pessoa?'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1



media = (somaidade) / 4
print(f'Média de idade será de {media}')
print(f'O Homem mais velho é o {nomevelho}.')
print(f'Tem {mulher20} mulheres com idade menor de 20 anos.')

