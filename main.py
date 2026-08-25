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
        ejercicio = input('Que ejercicio quieres agregar:')
        ejercicios.append(ejercicio)
        for ejercicio in ejercicios:
            print(f"Agregaste esto ejercicios:",ejercicio)
    elif opcion == 2:
        print(ejercicios)
    elif opcion == 3:
        print('en proceso')
    elif opcion == 4:
        print('en proceso')
    elif opcion == 5:
        print('Saliendo...')
print('Gracias por utilizar el sistema')