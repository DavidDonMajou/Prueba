# puntuacion=float(input("Qué puntuación tiene? "))
# extra=int(2400*puntuacion)
# if puntuacion == 0.0: print("Inaceptable")
# elif puntuacion == 0.4:
#     print("Aceptable")
#     print("El salario extra es de ", extra, "€")
# elif puntuacion >= 0.6:
#     print("Meritorio")
#     print("El salario extra es de ", extra, "€")
# else: print("La puntuacion debe ser 0.0, 0.4 0.6 o superior")



bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))