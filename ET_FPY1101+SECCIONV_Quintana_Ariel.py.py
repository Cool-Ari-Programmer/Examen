# Variables


Products = {
    "Modelname": ['brand next to it display measurements:', 1.2, "RAM", "DDisk Type","Capacity", "PRocessor","Graphics card"],
    "G0081": ['HP', 1.2, "2GBs", "SSD","500GFs","Intern 900","GTX 106"],
    "G0082": ['HP', 1.2, "2GBs", "SSD","500GFs","Intern 900","GTX 106"],
    "G0083": ['DELL', 1.2, "2GBs", "SSD","500GFs","Intern 900","GTX 106"],
    "G0084": ['DELL', 1.2, "2GBs", "SSD","500GFs","Intern 900","GTX 106"],
    }

Stock= {
    "Modelname": ["brand", "Cost", "Stock"],
    "G0081": ["HP", 50000, 5],
    "G0082": ["HP", 60000, 2],
    "G0083": ["DELL", 40000, 1],
    "G0084": ["DELL", 45000, 2],
}

user_choice: 0
user_asking_brand: "Blank"
user_asking_price: 0
admin_asking_brand: "f"
total_stock: 0
marca: "blank"
# Variables/
   
def stock_marca(marca):
    marca = marca.lower()  
    found = False
    for model, details in Stock.items():
        if model != "Modelname" and details[0].lower() == marca:
            print(f"Modelo: {model}, Stock: {details[2]}")
            found = True
    if not found:
        print("No se encontró stock para la marca ingresada.")



def busqueda_precio(p_min, p_max):
    resultados = []
    for model, details in Stock.items():
        if model != "Modelname" and details[2] > 0 and p_min <= details[1] <= p_max:
            resultados.append(f"{details[0]}-{model}")
    
    if resultados:
        resultados.sort()
        print("Modelos encontrados dentro del rango de precios:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in Stock:
        Stock[modelo][1] = p  
        print("Precio de", modelo, "Actualizado")
    else:
        print("Modelo no encontrado.")


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
            print("Debe de ") 
        else: 
            break
    
    if user_choice == 1:
        marca = input("Ingrese la marca para buscar el stock: ").strip()
        stock_marca(marca)


    elif user_choice == 2 :
        while True:
            try:
                p_min = int(input("Ingrese el precio mínimo: "))
                p_max = int(input("Ingrese el precio máximo: "))
            except ValueError:
                print("Texto detectado, por favor ingrese números válidos.")
            else:
                break
        busqueda_precio(p_min, p_max)

    elif user_choice == 3:
        while True:
            modelo = input("Ingrese el modelo que desea actualizar: ").strip()
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Debe ingresar un valor entero para el precio.")
                continue
            
            resultado = actualizar_precio(modelo, nuevo_precio)
            if resultado:
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
            
            continuar = input("¿Desea actualizar otro precio? (si/no): ").strip().lower()
            if continuar == "no":
                break       

    elif user_choice == 4:
        print("Adios")
        break
    else:
        print("Porfavor introducir una opcion real! (1-4)")



        

