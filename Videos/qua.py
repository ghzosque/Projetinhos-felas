dist = float(input('Qual a distancia da viagem ? -> '))

if dist <= 200:
    valor1 = dist * 0.5
    print('Valor', valor1)

if dist > 200:
    valor1 = dist * 0.45
    print('Valor', valor1)

