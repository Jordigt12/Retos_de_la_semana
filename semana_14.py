# Listas para almacenar los datos de los colaboradores
nombre = []
correo = []
numero = []

# Función que muestra el menú principal y valida la opción ingresada
def menu():
    selecciones = ["1", "2", "3"]  # Opciones válidas como cadenas
    while True:
        print("""
        Hola, ¿cómo te encuentras? Espero que bien.
        Por favor, ingresa una opción:
        1. Para agregar colaboradores ingrese [1]
        2. Para modificar colaboradores ingrese [2]
        3. Para mostrar todos los resultados [3]
        """)
        seleccion = input("Ingrese una opción válida: ").strip()  # Limpia espacios
        if seleccion in selecciones:
            return seleccion  # Devuelve la opción si es válida
        else:
            print("Tecla incorrecta")  # Mensaje de error si no está en la lista

# Bucle principal del programa
while True:
    opcion = menu()  # Llama al menú y guarda la opción seleccionada

    # Opción 1: Agregar colaborador
    if opcion == "1":

        # Función para ingresar nombre
        def nombre_completo():
            while True:
                colaborador = input("Ingrese el nombre del colaborador: ").strip().capitalize()
                if colaborador:
                    with open("texto.txt", "a") as nom:
                        nom.write("\tNombre: " + colaborador)  # Guarda en archivo
                    return colaborador  # Devuelve el nombre
                else:
                    print("El nombre no puede estar vacío. Intenta de nuevo.")
        nombre.append(nombre_completo())  # Agrega el nombre a la lista

        # Función para ingresar correo
        def correo_elec():
            while True:
                correo_email = input("Ingrese el correo del colaborador: ").strip()
                if correo_email:
                    with open("texto.txt", "a") as corre:
                        corre.write("\tCorreo: " + correo_email)  # Guarda en archivo
                    return correo_email
                else:
                    print("El correo no puede estar vacío. Intenta de nuevo.")
        correo.append(correo_elec())  # Agrega el correo a la lista

        # Función para ingresar número de celular
        def numero_celular():
            while True:
                numero_cel = input("Ingrese el número de celular del colaborador: ").strip()
                if numero_cel:
                    with open("texto.txt", "a") as cel:
                        cel.write("\tNúmero de celular: " + numero_cel + "\n")  # Guarda en archivo
                    return numero_cel
                else:
                    print("El número no puede estar vacío. Intenta de nuevo.")
        numero.append(numero_celular())  # Agrega el número a la lista

    # Opción 3: Mostrar todos los colaboradores registrados
    elif opcion == "3":
        for a, b, c in zip(nombre, correo, numero):
            print(f"Nombre: {a}, Correo: {b}, Número de celular: {c}")

    # Opción 2: Modificar datos de un colaborador
    else:

        # Función para reescribir el archivo con los datos actualizados
        def actualizar_archivo():
            with open("texto.txt", "w") as archivo:
                for n, c, num in zip(nombre, correo, numero):
                    archivo.write(f"Nombre: {n}\tCorreo: {c}\tNúmero: {num}\n")

        if not nombre:
            print("No hay colaboradores aún")  # Si no hay datos, se avisa
            continue

        # Muestra los colaboradores con índice
        print("Los colaboradores que tienes registrados son:")
        for i, (n, c, num) in enumerate(zip(nombre, correo, numero), start=1):
            print(f"{i}. Nombre: {n}, Correo: {c}, Número: {num}")

        try:
            # Selección del colaborador a modificar
            modificacion = int(input("Ingrese el número del colaborador a modificar: ")) - 1
            if 0 <= modificacion < len(nombre):
                campo = input("¿Qué deseas modificar? nombre / correo / numero: \n").strip().lower()

                # Modificar nombre
                if campo == "nombre":
                    nuevo = input("Ingrese el nuevo nombre: \n").strip().capitalize()
                    if nuevo:
                        nombre[modificacion] = nuevo
                        actualizar_archivo()
                        print(" Nombre actualizado.")

                # Modificar correo
                elif campo == "correo":
                    nuevo = input("Ingrese el nuevo correo: \n").strip()
                    if nuevo:
                        correo[modificacion] = nuevo
                        actualizar_archivo()
                        print(" Correo actualizado.")

                # Modificar número
                elif campo == "numero":
                    nuevo = input("Ingrese el nuevo número: \n").strip()
                    if nuevo.isdigit():
                        numero[modificacion] = nuevo
                        actualizar_archivo()
                        print(" Número actualizado.")
                    else:
                        print(" Solo se permiten números.")

                # Campo inválido
                else:
                    print(" Campo no válido.")
            else:
                print(" Número fuera de rango.")
        except ValueError:
            print(" Ingresa una opción válida.")
