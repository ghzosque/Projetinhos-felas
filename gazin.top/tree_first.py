import matplotlib.pyplot as plt
from sklearn import tree

'''
PESO        SUPERFICIE      RESULTADO
150           LISA            MAÇA
130           LISA            MAÇA
180         IRREGULAR        LARANJA
160         IRREGULAR        LARANJA
'''

lisa = 1
irregular = 0

laranja = 0
maça = 1
morango = 2
banana = 3
pera = 4 

X = [[140, lisa], 
     [130, lisa], 
     [150, irregular], 
     [170, irregular],
     [8, irregular],
     [12, irregular],
     [83, lisa],
     [100, lisa],
     [108, lisa],
     [133, lisa]]

Y = [maça, 
     maça, 
     laranja, 
     laranja,
     morango,
     morango,
     banana,
     banana,
     pera,
     pera]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

peso = input('Peso: ')
superficie = input('Superficie - 1 LISA - 0 IRREGULAR: ')

resultadoUsuario = clf.predict([[peso, superficie]])

if resultadoUsuario == 1:
    print('E UMA MAÇA')
elif resultadoUsuario == 2:
    print('E UM MORANGO')
elif resultadoUsuario == 3:
    print('E UMA BANANA')
elif resultadoUsuario == 4:
    print('E UMA PERA')
else:
    print('E UMA LARANJA')
