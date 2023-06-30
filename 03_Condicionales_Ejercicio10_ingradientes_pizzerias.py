tipo=int(input("1-Vegetariana\n2-Carnivora\nElige el número correspondiente al tipo de pizza que deseas: "))
vegetarianas=["Pimiento", "Tofu"]
noVegetarianas=["Peperoni", "Jamon", "Salmón"]
if tipo==1:
    ingrediente=int(input("Los ingredientes de las pizzas vegetarianas son:\n1-Pimiento\n2-Tofu\nEscribe el numero correspondiente al ingrediente que deseas: "))
    print("Los ingredientes de la pizza son: Mozzarela, Tomate y ", vegetarianas[ingrediente-1])
if tipo==2:
    ingrediente=int(input("Los ingredientes de las pizzas no vegetarianas son:\n1-Peperoni\n2-Jamón\n3-Salmón\nEscribe el numero correspondiente al ingrediente que deseas: "))
    print("Los ingredientes de la pizza son: Mozzarela, Tomate y ", noVegetarianas[ingrediente-1])
else: print("No has escrito un número correcto")   