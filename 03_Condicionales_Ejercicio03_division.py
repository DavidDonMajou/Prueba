numerador=float(input("Numerador de la división: "))
denominador=float(input("Denominador de la división: "))
if denominador!=0:
    division=float(numerador/denominador)
    print(numerador, " dividido entre ", denominador, " da como resultado ", round(division,2))
else: print("infinitísimo")         