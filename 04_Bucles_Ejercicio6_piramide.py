numero=int(input("Introduce un numero: "))

for i in range(numero):
    for j in range(i):
        print("*", end="")
    print("")    