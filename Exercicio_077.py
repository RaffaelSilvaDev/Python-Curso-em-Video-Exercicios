
palavras = ('Casa', 'Tomada', 'Lampada', 'Cadeira', 'Lustre', 'Notebook')
print('-'*50)
print(f'{"Encontre Vogais em cada Palavra da Tupla abaixo".upper():^40}')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='  ')

           
       