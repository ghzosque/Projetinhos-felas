n1 = int(input("Velocidade: "))

if n1 > 80:
    n = (n1 - 80) * 7

    print("Vc sera multado em ", n)
else:
    print("Vc esta na velocidade normal")