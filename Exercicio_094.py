pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor Digite M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S para sim ou N para não.')
    if resp == 'N':
        break
print('=-='*25)
print(f'a) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'b) A média de idade das pessoas cadastradas foi de {media:5.2f} anos.')
print(f'c) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} e ', end='')
print()
print(f'd) Lista de pessoas acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'  {k} = {v};.  ', end='')
        print()
print('=-='*25)
print('<<<ENCERRADO>>>')
