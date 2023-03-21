from random import randint

computador = randint(0,5)
print('Pensei =', computador)
print('Qual é o numero que pensei')
n = int(input())
while computador != n:
    print('ERROU, qual é o numero que pensei')

    n = int(input())
if n == computador:
    print('BOA')


