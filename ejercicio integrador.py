def CargaDeAnimales():
    
    var1 = int(input("Cantidad de registros que desea: "))   
    while var1 > contador:

        contador = contador + 1 
        dato1 = str(input("Especie:"))
        dato2 = int(input("Poblacion:"))
        if dato2 < 10000:
            print ("En vias de exticion")
        elif dato2 >= 10000:
            print ("“Fuera de peligro de extincion") 
        elif dato2 == 0:
            print ("Extinto") 
                  
        dato3 = str(input("Ubicacion:"))
        
        animal = {"especie": dato1,"poblacion": dato2, "ubicacion": dato3}
        
        animales.append(animal)
        
        for animales1 in animales:
            print (animales1)
            
# def consulta (animales[]):
#     print(animales)  
          
animales = []
animal = {}
contador = 0            
print("_______Bienvenido_______")
print("Seleciones unas de las siguientes opciones")
print("1- Ingresar registro de animales")
print("2- Consultar registro de animales cargados")
print("3- Salir del programa agradeciendo al usuario")
opcion1 = input("Ingrese la opcion deseada: ")

if opcion == 1:
    print()
               

            

    
