correo=input("Dime tu correo loco: ")
posicion=correo.find("@")
nombremail=correo[:posicion:]
print(nombremail + "@ceu.es")