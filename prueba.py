# Python 3.7.9 

animales = []

def setAnimals():
    print('Indique la cantidad de registros a cargar:')
    cantidad = int(input())
    mensaje = 'animales' if cantidad > 1 else 'animal'
    print(f'Se van a insertar {cantidad} { mensaje }')
    for x in range(cantidad):
        print('Ingrese Especie:', end=" ")
        especie = input()
        print('Ingrese Poblacion:', end=" ")
        poblacion = int(input())
        datapoblacion = ''
        if poblacion < 10000 and poblacion != 0:
            datapoblacion = 'En vias de extincion.'
        elif poblacion >= 10000:
            datapoblacion = 'Fuera de peligro de extincion.'
        elif poblacion == 0:
            datapoblacion = 'Extinto.'
        print('Ingrese Ubicacion:', end=" ")
        ubicacion = input()
        dic = {
            'especie' : especie,
            'poblacion' : datapoblacion,
            'ubicacion' : ubicacion
        }
        animales.append(dic)
    return True
    
def CargaDeAnimales():
    if len(animales) > 0:
        for animal in animales:
            especie = animal['especie']
            poblacion = animal['poblacion']
            ubicacion = animal['ubicacion']
            print('')
            print(f'Especie: { especie }. Poblacion: {poblacion}. Ubicacion : {ubicacion}')
            print('')
    else:
        print('')
        print('la lista esta vacia')
    return True
    
def inicio():
    print('Ingrese el número de la acción que quiere realizar')
    print('1. Ingrese registro de Animales')
    print('2. Consulte registros cargados')
    print('3. Salir del programa')
    print('')
    variable = int(input())
    if variable == 1:
        setAnimals()
        print('---------------------------')
        inicio()
    elif variable == 2:
        CargaDeAnimales()
        print('---------------------------')
        inicio()
    elif variable == 3:
        return False
    else:
        print('Opción no valida')
        inicio()
    
if __name__ == '__main__':
    print('Bienvenido')
    inicio()
        
    