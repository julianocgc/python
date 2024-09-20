nome = str(input('Qual é o seu nome? '))
if nome == 'Juliano':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Carla Juliana Viviane':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia {}!'.format(nome))