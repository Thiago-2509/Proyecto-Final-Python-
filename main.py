print('===========================')
print('Bienvenido a Smart Training')
print('===========================')

ejercicios = []


# ==========================================
# OPCIÓN 1: AGREGAR EJERCICIO
# ==========================================

def agregarEjercicio(ejercicios):
    print('AGREGAR EJERCICIO')
    while True:
        try:
            semana = int(input('¿En qué semana desea agregar el ejercicio?: '))
            break
        except ValueError:
            print('Debe ingresar un número para la semana.')
    nombre = input('¿Qué ejercicio desea agregar?: ')
    while True:
        try:
            series = int(input('¿Cuántas series son?: '))
            break
        except ValueError:
            print('Debe ingresar un número para las series.')
    while True:
        try:
            repeticiones = int(input('¿Cuántas repeticiones son?: '))
            break
        except ValueError:
            print('Debe ingresar un número para las repeticiones.')
    ejercicio = {
        'semana': semana,
        'nombre': nombre,
        'series': series,
        'repeticiones': repeticiones
    }
    ejercicios.append(ejercicio)
    print('Ejercicio agregado correctamente')

# ==========================================
# OPCIÓN 2: VER HISTORIAL
# ==========================================

def verHistorial(ejercicios):
    print('== HISTORIAL SEMANAL ==')
    if len(ejercicios) == 0:
        print('No hay ejercicios registrados.')
    else:
        for ejercicio in ejercicios:
            print('-------------------------')
            print('Semana:', ejercicio['semana'])
            print('Ejercicio:', ejercicio['nombre'])
            print('Series:', ejercicio['series'])
            print('Repeticiones:', ejercicio['repeticiones'])
        print('-------------------------')


# ==========================================
# OPCIÓN 3: CALCULAR PROGRESO
# ==========================================

def calcularProgreso(ejercicios):
    print('CALCULAR PROGRESO')
    if len(ejercicios) == 0:
        print('No hay ejercicios registrados.')
    else:
        print('Cantidad de ejercicios registrados:', len(ejercicios))
        for ejercicio in ejercicios:
            total = ejercicio['series'] * ejercicio['repeticiones']
            print('-------------------------')
            print('Ejercicio:', ejercicio['nombre'])
            print('Semana:', ejercicio['semana'])
            print('Repeticiones totales:', total)

# ==========================================
# OPCIÓN 4: BUSCAR EJERCICIO
# ==========================================

def buscarEjercicio(ejercicios):
    print('== BUSCAR EJERCICIO ==')
    nombre = input('¿Qué ejercicio desea buscar?: ')
    encontrado = False
    for ejercicio in ejercicios:
        if ejercicio['nombre'].lower() == nombre.lower():
            print('-------------------------')
            print('Semana:', ejercicio['semana'])
            print('Ejercicio:', ejercicio['nombre'])
            print('Series:', ejercicio['series'])
            print('Repeticiones:', ejercicio['repeticiones'])
            encontrado = True
    if encontrado == False:
        print('No se encontró ese ejercicio.')

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

opcion = 0
while opcion != 5:
    print("""
¿Qué deseas hacer?
    1. Agregar ejercicio del día
    2. Ver historial semanal
    3. Calcular progreso
    4. Buscar ejercicio
    5. Salir
    """)
    # Validar que la opción sea un número
    while True:
        try:
            opcion = int(input('Elige una opción: '))
            break
        except ValueError:
            print('Debes ingresar un número.')
    # Ejecutar la opción seleccionada
    if opcion == 1:
        agregarEjercicio(ejercicios)
    elif opcion == 2:
        verHistorial(ejercicios)
    elif opcion == 3:
        calcularProgreso(ejercicios)
    elif opcion == 4:
        buscarEjercicio(ejercicios)
    elif opcion == 5:
        print('Saliendo de Smart Training...')
    else:
        print('Opción no válida.')
print('Gracias por utilizar el programa.')  