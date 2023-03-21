import matplotlib.pyplot as plt
from sklearn import tree
import tkinter as tk


'''
=============================================
PESO            SUPERFICIE      RESULTADO
=============================================
LARANJA         IRREGULAR       130-144
TANGERINA       IRREGULAR       114-120
LIMAO           IRREGULAR       93-100
MORANGO         IRREGULAR       08-14
=============================================
PESO            SUPERFICIE      RESULTADO
=============================================
MAÇA            LISA            135-141
PERA            LISA            119-126
BANANA          LISA            79-86
UVA             LISA            04-11
=============================================
'''



lisa = 1
irregular = 0

laranja = 0
maça = 1
morango = 2
banana = 3
pera = 4
tangerina = 5
uva = 6
limao = 7

X = [[135, lisa], [141, lisa], 
     [130, irregular], [144, irregular],
     [8, irregular],[14, irregular],
     [79, lisa],[86, lisa],
     [119, lisa],[126, lisa],
     [114, irregular],[120, irregular],
     [4, lisa],[11, lisa],
     [93, irregular],[100, irregular],]

Y = [maça, maça, 
     laranja, laranja,
     morango, morango,
     banana, banana, 
     pera, pera,
     tangerina, tangerina,
     uva, uva, 
     limao, limao]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

def predict_fruit():
    peso = int(peso_entry.get())
    superficie = int(superficie_var.get())
    
    resultadoUsuario = clf.predict([[peso, superficie]])

    if resultadoUsuario == 1:
        resultado_label.config(text='MAÇÃ')
    elif resultadoUsuario == 2:
        resultado_label.config(text='MORANGO')
    elif resultadoUsuario == 3:
        resultado_label.config(text='BANANA')
    elif resultadoUsuario == 4:
        resultado_label.config(text='PERA')
    elif resultadoUsuario == 5:
        resultado_label.config(text='TANGERINA')
    elif resultadoUsuario == 6:
        resultado_label.config(text='UVA')
    elif resultadoUsuario == 7:
        resultado_label.config(text='LIMAO')
    else:
        resultado_label.config(text='LARANJA')

root = tk.Tk()
root.title("Classificador de Frutas")

# Frame para as entradas
inputs_frame = tk.Frame(root)
inputs_frame.pack(pady=10)

peso_label = tk.Label(inputs_frame, text='Peso: ')
peso_label.grid(row=0, column=0)

peso_entry = tk.Entry(inputs_frame)
peso_entry.grid(row=0, column=1)

superficie_label = tk.Label(inputs_frame, text='Superfície:')
superficie_label.grid(row=1, column=0)

superficie_var = tk.IntVar()
superficie_var.set(1)

lisa_radio = tk.Radiobutton(inputs_frame, text='Lisa', variable=superficie_var, value=1)
lisa_radio.grid(row=1, column=1)

irregular_radio = tk.Radiobutton(inputs_frame, text='Irregular', variable=superficie_var, value=0)
irregular_radio.grid(row=1, column=2)

# Botão para prever o resultado
predict_button = tk.Button(root, text='Prever', command=predict_fruit)
predict_button.pack(pady=10)

# Label para o resultado
resultado_label = tk.Label(root, text='')
resultado_label.pack()

root.mainloop()
tree.plot_tree(clf)
plt.show()
