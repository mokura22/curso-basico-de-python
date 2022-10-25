
utiles_escolares = []


var2 = 1
var1 =int(input("cuantos utiles va a ingresar:  "))
if var1 == 1:
    var1 =int(input("la variable debe ser mayor a 1:  "))
 
while var2 != var1:
     
        elemento = input("ingresar util escolar: ") 
        utiles_escolares.insert(var1-1, elemento)
        if "tijera" in utiles_escolares:
            
            var2 += 1
        else:
            print("debes ingresar tijera")
         
    
print(utiles_escolares)


# utiles_escolares.insert (2,"carpeta de codigos")
# utiles_escolares.append("cuadernos de pruebas")

# print(utiles_escolares)

# utiles_escolares.pop(2)

# utiles_escolares.remove("tijera")

# print(utiles_escolares)






