renta=float(input("Cuál es tu renta anual: "))
if renta < 9999:
    tipoimpositivo=0.05
elif renta > 10000 and renta < 20000:
    tipoimpositivo=0.15
elif renta >= 20000 and renta < 35000:
    tipoimpositivo=0.2
elif renta >= 35000 and renta < 60000:
    tipoimpositivo=0.3
else: tipoimpositivo=0.45

print("Tienes que pagar", renta * tipoimpositivo, "€", sep='')