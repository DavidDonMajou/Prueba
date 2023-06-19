numerador=float(input("Escribe el numerador de la división es "))
denominador=float(input("Escribe el denominador de la división es "))
resto=numerador % denominador
cociente=numerador / denominador

print("El numerador es: ", numerador)
print("El denominador es: ", denominador)
print("El resto es: ",  round(resto))
print("El cociente es: ", round(cociente))