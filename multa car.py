carro = float(input('Qual velocidade do carro?'))
if carro >= 80:
    multa = (carro - 80 ) * 7
    print(f'Carro ultrapassou o limite de velocidade 80 km, correndo a {carro}, e tera q pagar {multa} reais')
else:
    print('tudo normal por aqu..')