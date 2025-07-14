# Variables


Products = {
    "Modelname": ['brand next to it display measurements:', 1.2, "RAM", "DDisk Type","Capacity","PRocessor","Graphics card"]
}

Stock= {
    "Modelname": ["Cost", "Stock"]
}

user_choice: 0


# Variables/

print("******Menu principal******")
print("1. Stock disponible")
print("2. Busqueda por precio")
print("3. Actualizar precio")
print("4. Salir")


while True:

    while True:

        try:
            user_choice  = int(input())
        except ValueError:
            print("Texto detectado") 
        else: 
            break
    
    if user_choice == 1:
        print("Working on it")

    elif user_choice == 2 :
        print("workin on it")

    elif user_choice == 3:
        print("workin on it")
    elif user_choice == 4:
        print("Goobie")
        break
    else:
        print("Porfavor introducir una opcion real! (1-4)")



        









