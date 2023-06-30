dinero=float(input("¿Cuánto dinero vas a invertir?: "))
interes=0.01*float(input("¿Cuál es el porcentaje de interés anual?: "))
time=int(input("¿Cuantos años va a estar ahí?"))
for i in range(1,time+1):
    dinero=dinero+(dinero*interes)
    print("El año", i, "tendras", dinero, "euros en total")