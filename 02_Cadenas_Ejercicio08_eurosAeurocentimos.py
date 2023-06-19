precio=str(round(float(input("Dime el precio loco: ").replace("," , ".")), 1))
posicioncoma=precio.find(",")
print("los euros son estos: " + str(precio[:-2:]))
print("los centimmos son estos: " + str(precio[posicioncoma::]) + "0")