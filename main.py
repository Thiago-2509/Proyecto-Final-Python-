print('===========================')
print('Bienvenido a Smart Training')
print('===========================')
#Se creo una lista ejercicios para guardarlos cuando el cliente los agregue en la opcion 1
ejercicios = []
#Se creo el while para asi seguir preguntando que opcion desea realizar el cliente 
opcion = 0
while opcion != 5:
    print("""Que deseas hacer:
        1.Agregar ejercicio del dia
        2.Ver historial semanal
        3.Calcular progreso
        4.Buscar ejercicio
        5.Salir""")
#Se creo la opcion 1 donde el cliente puede agregar el ejercicio deseado y se guarda en la lista creada anteriormente 
    opcion = int(input("Elije una opcion: "))
    if opcion == 1:
        ejercicio = {
            'nombre': input('Que ejercicio desea agregar: '),
            'series': int(input('Cuantas series son: ')),
            'repeticiones': int(input('Cuantas repeticiones son: '))
        }
        ejercicios.append(ejercicio)
        print('Ejercicios arreglados correctamente')
    elif opcion == 2:
        print('==Historial semanal==')
        if len(ejercicios) == 0:
            print("Todavia no has hagregado ejercicios")
        else:
            for ejercicio in ejercicios:
                print('-------------------------') 
                print('Ejercicio:', ejercicio['nombre'])
                print('Series:', ejercicio['series'])
                print('Repeticion:', ejercicio['repeticiones'])   
    elif opcion == 3:
        print('en proceso')
    elif opcion == 4:
        print('en proceso')
    elif opcion == 5:
        print('Saliendo...')
print('Gracias por utilizar el sistema')