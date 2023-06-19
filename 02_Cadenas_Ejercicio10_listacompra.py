compra=str("Arroz,cosas,mascosas,muchasmascosas" + ",")

while compra != "":
    palabramostrar=compra[0:compra.find(",")]
    print(palabramostrar)
    compra=compra[compra.find(",")+1:]
    
    #str(input("Pon la lista de la compra a continuación: "))