pasta=float(input("Cuánta pasta le has metido loco: "))
interes=float(float(input("Qué intereses tiene al año ").replace("%", "")) / 100).__add__(1)
anios=float(float(input("Cuántos meses lleva metido el dinero ")) / 12)


print("Por ahora llevas ganado " + str((pasta * interes)))