# Variables


Products = {
    "Modelname": ['brand next to it display measurements:', 1.2, "RAM", "DDisk Type","Capacity", "PRocessor","Graphics card"],
    "G0081": ['HP', 1.2, "2GBs", "SSD","500GFs","Intern 900","GTX 106"],
    "G0082": ['HP', 1.2, "2GBs", "SSD","500GFs","Intern 900","GTX 106"],
    
    }

Stock= {
    "Modelname": ["brand", "Cost", "Stock"],
    "G0081": ["HP", 50000, 5],
    "G0082": ["HP", 60000, 2]
}

user_choice: 0
user_asking_brand: "Blank"
user_asking_price: 0
admin_asking_brand: "f"
total_stock: 0
marca: "blank"
# Variables/
   
def stock_marca(marca):
    marca = marca.lower()  # Convertir la marca a minúsculas para comparación
    found = False
    for model, details in Stock.items():
        if model != "Modelname" and details[0].lower() == marca:
            print(f"Modelo: {model}, Stock: {details[2]}")
            found = True
    if not found:
        print("No se encontró stock para la marca ingresada.")



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
        marca = input("Ingrese la marca para buscar el stock: ").strip()
        stock_marca(marca)


    elif user_choice == 2 :
        print("workin on it")
        while True:
            try:
                    user_asking_price  = int(input())
            except ValueError:
             print("Texto detectado") 
            else: 
                break
        if user_asking_price in Products:
            print("cool")
        else:
            print("aint here")

    elif user_choice == 3:
        print("workin on it")
        


            
        if user_asking_brand in Products:
            print("ijole")
        else:
            print("No existe")

    elif user_choice == 4:
        print("Goobie")
        break
    else:
        print("Porfavor introducir una opcion real! (1-4)")



        

