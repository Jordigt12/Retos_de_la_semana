import os
alumnos = []
calificaciones = []

def menu():
    selecciones=["1", "2", "S"]
    while True:
        print("""
        Hola, ¿cómo te encuentras? Espero que bien.
        Por favor, ingresa una opción:
        1. Para agregar alumnos ingrese [1]
        2. Para agregar calificaciones ingrese [2]
        S. Para salir y ver resultados ingrese [S]
        """)
        seleccion=input("Ingrese una opción válida: ").strip().upper()
        if seleccion in selecciones:
            return seleccion
        else:
            print("tecla incorrecta")

def cantidad_alu():
    while True:
        try:
            cantidad=int(input("ingrese la cantidad que desea agregar"))
            return cantidad
        except ValueError:
            print("dato incorrecto. Por favor ingresa un dato de numero entero")
while True:
    opcion = menu()

    if opcion == "1":
        alumnos_a_ingresar = cantidad_alu()
        for i in range(alumnos_a_ingresar):
            while True:
                nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
                if nombre == "":
                    print("No se puede dejar el espacio en blanco.")
                else:
                    alumnos.append(nombre)
                    break

    elif opcion == "2":
        if not alumnos:
            print("Primero debes ingresar alumnos antes de agregar calificaciones.")
            continue
        calificaciones_a_ingresar = cantidad_alu()
        for i in range(calificaciones_a_ingresar):
            while True:
                try:
                    nota = float(input(f"Ingrese la calificación para el alumno {i+1}: "))
                    calificaciones.append(nota)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        for alumno, nota in zip(alumnos, calificaciones):
            print(f"el alumno {alumno} tiene una calificacion de {nota}")
        os.system("pause")
    else:
        while True:
            try:

                opcion=="S"
                verificacion=input("seguro desea salir? presione [1] para si o [2] para no ")
                if verificacion=="2":
                    break
                elif verificacion=="1":
                    print("----------RESULTADOS--------------")
                    for alumno, nota in zip(alumnos, calificaciones):
                        print(f"el alumno {alumno} tiene una calificacion de {nota}")
                os.system("pause")
                break
            except ValueError:
                print("valor incorrecto")
            




            


