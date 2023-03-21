
import tkinter as tk

def calcular():
    casa = float(casa_entry.get())
    salario = float(salario_entry.get())
    anos = int(anos_entry.get())

    prestacao = casa / (anos * 12)
    minimo = (salario * 30) / 100

    prestacao_label.config(text='Prestação = R$ {:.2f}'.format(prestacao))

    if prestacao > minimo:
        aceito_label.config(text='Negado')
    else:
        aceito_label.config(text='Aceito')


# cria a janela principal
root = tk.Tk()
root.title("Calculadora de Empréstimo")

# cria os widgets
casa_label = tk.Label(root, text='Valor da casa: R$')
casa_entry = tk.Entry(root)

salario_label = tk.Label(root, text='Salário: R$')
salario_entry = tk.Entry(root)

anos_label = tk.Label(root, text='Anos:')
anos_entry = tk.Entry(root)

calcular_button = tk.Button(root, text='Calcular', command=calcular)

prestacao_label = tk.Label(root, text='')
aceito_label = tk.Label(root, text='')

# organiza os widgets na janela
casa_label.grid(row=0, column=0)
casa_entry.grid(row=0, column=1)

salario_label.grid(row=1, column=0)
salario_entry.grid(row=1, column=1)

anos_label.grid(row=2, column=0)
anos_entry.grid(row=2, column=1)

calcular_button.grid(row=3, column=1)

prestacao_label.grid(row=4, column=0, columnspan=2)
aceito_label.grid(row=5, column=0, columnspan=2)

# inicia o loop de eventos
root.mainloop()
