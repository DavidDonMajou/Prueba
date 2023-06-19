fecha=str(input("Fecha de nacimiento formato xx/xx/xxxx: "))
primera=int(fecha.find("/"))
segunda=int(fecha[primera+1::].find("/")+primera+1)
print("Tu dia de nacimiento es el: " + fecha[0:primera])
print("Tu mes de nacimiento es el: " + fecha[primera+1:segunda])
print("Tu año de nacimiento es el: " + fecha[segunda+1:])


