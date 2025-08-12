from pedrapapel import randint
comp = randint(0, 5)
print('><><><' * 15)
print('Que numero vc deseja?:')
print('><><><' * 15)
jog = int(input('Qual numero vc deseja:'))
if comp == jog:
    print('parabens!')
else:
    print(f'nao foi dessa vez, eu escolhi {comp}, não {jog}')