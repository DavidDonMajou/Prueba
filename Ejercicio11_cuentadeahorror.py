dinero=float(input("Cuánto dinero vas a meter: "))
dinero1=round(float(dinero * 1.04) , 2)
dinero2=round(float(dinero1 * 1.04) , 2)
dinero3=round(float(dinero2 * 1.04) , 2)
print("El primer año vas a recibir " + str(dinero1))
print("El segundo año vas a recibir " + str(dinero2))
print("El tercer año vas a recibir " + str(dinero3))