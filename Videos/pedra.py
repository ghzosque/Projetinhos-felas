from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print('''Opções:
      [0]PEDRA
      [1]PAPEL
      [2]TESOURA''')

jogada = int(input('Escolha: '))
print('Computador : {}' .format(itens[computador]))
print('Jogador : {}' .format(itens[jogada]))

if computador == 0: #pedra
    if jogada == 0:
        print('Empate')
    elif jogada == 1:
        print('Vitoria')
    elif jogada == 2:
        print('Derrota')
    else:
        print('Jogada invalida')

if computador == 1: #papel
    if jogada == 0:
        print('Derrota')
    elif jogada == 1:
        print('Empate')
    elif jogada == 2:
        print('Vitoria')
    else:
        print('Jogada invalida')

if computador == 2: #tesoura
    if jogada == 0:
        print('Vitoria')
    elif jogada == 1:
        print('Derrota')
    elif jogada == 2:
        print('Empate')
    else:
        print('Jogada invalida')
