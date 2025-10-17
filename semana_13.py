import os  # Importa el módulo 'os' para usar comandos del sistema, como 'os.system("pause")' 

# Se crean listas vacías para almacenar los nombres de los alumnos y sus calificaciones
alumnos = []
calificaciones = []

# --------------------------------------
# FUNCIÓN: menu()
# --------------------------------------
def menu():
    # Lista de opciones válidas
    selecciones = ["1", "2", "S"]
    
    while True:
        # Muestra el menú principal
        print("""
        Hola, ¿cómo te encuentras? Espero que bien.
        Por favor, ingresa una opción:
        1. Para agregar alumnos ingrese [1]
        2. Para agregar calificaciones ingrese [2]
        S. Para salir y ver resultados ingrese [S]
        """)
        
        # Se solicita la opción al usuario, eliminando espacios y convirtiendo a mayúsculas
        seleccion = input("Ingrese una opción válida: ").strip().upper()
        
        # Si la opción ingresada es válida, se devuelve
        if seleccion in selecciones:
            return seleccion
        else:
            # Si no es válida, se muestra un mensaje de error y se repite
            print("Tecla incorrecta")

# --------------------------------------
# FUNCIÓN: cantidad_alu()
# --------------------------------------
def cantidad_alu():
    # Solicita al usuario cuántos alumnos o calificaciones desea ingresar
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            return cantidad
        except ValueError:
            # Si el usuario ingresa algo que no es un número entero, se muestra un error
            print("Dato incorrecto. Por favor ingresa un número entero.")

# --------------------------------------
# BUCLE PRINCIPAL DEL PROGRAMA
# --------------------------------------
while True:
    # Se muestra el menú y se obtiene la opción seleccionada
    opcion = menu()

    # --------------------------------------
    # OPCIÓN 1: Agregar alumnos
    # --------------------------------------
    if opcion == "1":
        alumnos_a_ingresar = cantidad_alu()  # Se pide la cantidad de alumnos a ingresar
        
        # Se repite según la cantidad indicada
        for i in range(alumnos_a_ingresar):
            while True:
                nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
                
                # Valida que el nombre no esté vacío
                if nombre == "":
                    print("No se puede dejar el espacio en blanco.")
                else:
                    alumnos.append(nombre)  # Se agrega el nombre a la lista
                    break

    # --------------------------------------
    # OPCIÓN 2: Agregar calificaciones
    # --------------------------------------
    elif opcion == "2":
        # Si no hay alumnos, no se puede continuar
        if not alumnos:
            print("Primero debes ingresar alumnos antes de agregar calificaciones.")
            continue

        calificaciones_a_ingresar = cantidad_alu()  # Pide cuántas calificaciones agregar

        # Pide una calificación por cada alumno
        for i in range(calificaciones_a_ingresar):
            while True:
                try:
                    nota = float(input(f"Ingrese la calificación para el alumno {i+1}: "))
                    calificaciones.append(nota)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        
        # Muestra los alumnos con sus calificaciones
        for alumno, nota in zip(alumnos, calificaciones):
            print(f"El alumno {alumno} tiene una calificación de {nota}")
        
        os.system("pause")  # Pausa el programa (solo funciona en Windows)

    # --------------------------------------
    # OPCIÓN S: Salir del programa
    # --------------------------------------
    else:
        while True:
            try:
                opcion == "S"
                
                # Pide confirmación antes de salir
                verificacion = input("¿Seguro desea salir? Presione [1] para Sí o [2] para No: ")
                
                if verificacion == "2":
                    # Si elige no salir, se rompe el bucle interno (regresa al menú)
                    break
                elif verificacion == "1":
                    # Si confirma salida, muestra los resultados finales
                    print("---------- RESULTADOS --------------")
                    for alumno, nota in zip(alumnos, calificaciones):
                        print(f"El alumno {alumno} tiene una calificación de {nota}")
                
                os.system("pause")  # Espera antes de cerrar
                break

            except ValueError:
                print("Valor incorrecto.")
