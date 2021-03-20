dados = []
cadastro = []
gordo = magro = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        gordo = magro = dados[1]
    else:
        if dados[1] > gordo:
            gordo = dados[1]
        if dados[1] < magro:
            magro = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar [S/N]: ')).strip()[0]
    if r in 'Nn':
        break

print(f'Foram cadastradas {len(cadastro)} pessoas')
for p in cadastro:
    if p[1] == gordo:
        print(f'{p[0]}')
print()
print(f'As pessoas mais pesadas foram {gordo}')
for p in cadastro:
    if p[1] == magro:
        print(f'{p[0]}')

print(f'As pessoas mais leves foram {magro}')

