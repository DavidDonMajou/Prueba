nombre=input("Cuál es tu nombre: ")
sexo=input("Cuál es tu sexo: ").lower()
inicial=nombre[0:1]

if sexo=="mujer" and inicial<'m':
    print("Grupo A")
if sexo=="mujer" and inicial>'m':
    print("Grupo B")
if sexo=="hombre" and inicial<'n':
    print("Grupo A")
else:print("Grupo B")