sexo = str(input('Digite F/M? ')) .upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidados. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')