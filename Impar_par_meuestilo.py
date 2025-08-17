from random import randint

n1 = 0
tot = 0
n2 = 0
imp = par = ''
v = 0
while v <= 10 :
    par = str(input('Escolhe Par ou Impar: ')) .upper(P)
    n1 = int(input('fale um numero de 1 a 10:'))
    n2 = int(randint(0, 10))
    tot = (n1 + n2) % 2
    print(f'O computador escolheu {n2}')
    print(f'Voce escolheu {par}')
    if tot == 0:
        print('Parabens Par venceu!')
    if tot == 1:
        print('Parabens Impar venceu!')
    print('')
print(f'Game Over, o jogo acabou, total de pontos {v}')