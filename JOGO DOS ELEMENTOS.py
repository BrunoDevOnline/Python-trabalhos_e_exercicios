from random import randint
itens = ('fogo', 'gelo', 'agua', 'planta')
computador = randint(0, 3)
print('''Suas opções:
[ 0 ] Fogo 
[ 1 ] Gelo
[ 2 ] Agua
[ 3 ] Planta ''')
jogador = int(input(('Qual é a sua jogada')))
print('<>-'*10)
print('Pc jogou: {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('<>-'*10)
if computador == 0:#FOGO
    if jogador == 0:#FOGO
        print('EMPATE')
    elif jogador == 1:#GELO
        print('JOGADOR VENCE')
    elif jogador == 2:#AGUA
        print('JOGADOR VENCE')
    elif jogador == 3:#PLANTA
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
if computador == 1:#GELO
    if jogador == 0: #FOGO
        print('JOGADOR VENCE')
    elif jogador == 1:#GELO
        print('EMPATE')
    elif jogador == 2:#AGUA
        print('COMPUTADOR VENCE')
    elif jogador == 3:#PLANTA
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
if computador == 2:#AGUA
    if jogador == 0:#FOGO
        print('COMPUTADOR VENCE')
    elif jogador == 1:#GELO
        print('JOGADOR VENCE')
    elif jogador == 2:#AGUA
        print('EMPATE')
    elif jogador == 3:#PLANTA
        print('JOGADOR VENCE')
    else:
        print('JOAGADA INAVALIDA')
if computador == 3:#PLANTA
    if jogador == 0:#FOGO
        print('JOGADOR VENCE')
    elif jogador == 1:#GELO
        print('JOGADOR VENCE')
    elif jogador == 2:#AGUA
        print('COMPUTADOR VENCE')
    elif jogador == 3:#PLANTA
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')