cas = float(input('Qual Valor da casa?'))
sal = float(input('Qual seu salário?'))
ano = float(input('Por quantos anos pretende pagar?'))
porc = cas / (ano * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos '.format(cas, ano), end='')
print(' a prestação será de R${:.2f}'.format(porc))

if porc <= min:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo não concedido')