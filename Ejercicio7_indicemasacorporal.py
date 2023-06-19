print("Vamos a calcular tu índice de masa corporal")
peso=int(input("¿Cuánto pesas en kg?: "))
altura=int(input("¿Cuánto mides en cm?: "))
imd=round((peso / ((altura*0.01) **2)), 2)

print("Tu índice de masa corporal es " + str(imd))