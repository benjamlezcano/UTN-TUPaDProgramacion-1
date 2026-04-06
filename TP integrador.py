ejercicio = int(input("Ingrese que ejercicio quiere revisar: "))
match ejercicio:
    #ejercicio 1
    case 1:
            nombre = input("Ingrese su nombre: ")
            cantidad = input("Cantidad de productos: ")

            while nombre == "" or not nombre.isalpha():
                nombre = input("La contrasena debe ser solo de letras. ")

            while not cantidad.isdigit() or int(cantidad) <= 0:
                cantidad = input("Error, Debe ser solo numeros. ")
            cantidad = int(cantidad)

            total_sin_desc = 0
            total_con_desc = 0

            precio = input("precio: ")

            while not precio.isdigit():
                precio = input("Error, ingresa numeros: ")

            precio = int(precio)

            total_sin_desc += precio

            descuento = input("Descuento (S/N): ").lower()

            while descuento != "s" and descuento != "n":
                desc = input("Error. Ingresa S o N: ").lower()


            if descuento == "s":
                desc = precio * 0.10
                precio_final = precio - desc
                total_con_desc += precio_final

            ahorro = total_sin_desc - total_con_desc
            promedio = total_con_desc / cantidad

            print(f"Total sin descuentos: ${total_sin_desc}")
            print(f"Total con descuentos: ${total_con_desc:.2f}")
            print(f"ahorro: {ahorro:.2f}")
            print(f"Promedio por producto: ${promedio:.2f}")


    #Ejercicio 2
    case 2:
            usuario = "benjamin"
            clave = "123"
            intentos = 0 

            while intentos < 3:
                usuario1 = input("Ingrese el usuario:")
                clave1 = input("ingrese la clave: ")
                if usuario1 == usuario and clave1 == clave:
                    print("Acceso concedido")
                    break
                else:
                    print("Error")
                    intentos += 1 
            if intentos == 3:
                print("Cuenta bloqueada")

            while usuario1 == usuario and clave1 == clave:
                menu = ["1) Estado", "2) Cambiar clave", "3) Mensaje", "4) Salir"]
                for opcion in menu:
                    print(opcion)
                opcion = input("Opcion: ")
                if not opcion.isdigit():
                    print("Ingrese un numero")
                elif int(opcion) < 1 or int(opcion) > 4:
                    print("Elije una opcion entre 1 y 4")
                match opcion:
                    case "1":
                        print("Inscripto")
                        continue
                    case "2":
                        nuevaclave = input("Ingrese la nueva clave (6 digitos): ")
                        confirmarclave = input("Confirme la nueva clave: ")
                        if len(nuevaclave) < 6:
                            print("Error, la clave es muy corta ")
                        elif nuevaclave != confirmarclave:
                            print("Las claves son diferentes")
                        clave = nuevaclave
                        continue
                    case "3":
                        print("No importa qué tan lento vayas mientras no te detengas")
                        continue
                    case "4":
                        break


    #Ejercicio 3
    case 3:
        nombre = input("Ingrese el nombre del operador: ")
        lunes1 = ""
        lunes2 = ""
        lunes3 = ""
        lunes4 = ""

        martes1 = ""
        martes2 = ""
        martes3 = ""

        while nombre == "" or not nombre.isalpha():
            nombre = input("Ingrese un nombre: ")
        while True:
            menu = ["1. Reservar turno", "2. Cancelar turno(por nombre)", "3. Ver agenda del dia ", "4. Resumen General", "5. Salir"]
            for opcion in menu:
                print(opcion)
            opcion = input("Opcion: ")
            match opcion:
                case "1":
                    dia = int(input("1= Lunes, 2= Martes"))
                    paciente = input("Ingrese el nombre del paciente: ")
                    while paciente == "" or not paciente.isalpha():
                        paciente = input(("Escribir bien el nombre del paciente"))
                    if dia == 1:
                            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                                print("Ya existe")
                            elif lunes1 == "":
                                lunes1 = paciente
                            elif lunes2 == "":
                                lunes2 = paciente
                            elif lunes3 == "":
                                lunes3 = paciente
                            elif lunes4 == "":
                                lunes4 = paciente
                            else:
                                print("No hay turnos disponibles")
                    
                    if dia == 2:
                        if paciente == martes1 or paciente == martes2 or paciente == martes3:
                            print("Ya existe")
                        elif martes1 == "":
                            martes1 = paciente
                        elif martes2 == "":
                            martes2 = paciente
                        elif martes3 == "":
                            martes3 = paciente
                        else:
                            print("No hay turnos disponibles")

                
                case "2":
                    dia = int(input("Ingrese un dia: Lunes(1), Martes(2)"))
                    paciente = input("Ingrese el nombre del paciente: ")
                    while paciente == "" or not paciente.isalpha():
                        print("Escribir bien el nombre del paciente")
                    if dia == 1:
                                if lunes1 == paciente:
                                    lunes1 = ""
                                elif lunes2 == paciente:
                                    lunes2 = ""
                                elif lunes3 == paciente:
                                    lunes3 = ""
                                elif lunes4 == paciente:
                                    lunes4 = ""
                                else:
                                    print("No encontrado. ")
                    if dia == 2:
                        if martes1 == paciente:
                            martes1 = ""
                        elif martes2 == paciente:
                            martes2 = ""
                        elif martes3 == paciente:
                            martes3 = ""
                            
                case "3":
                    dia = int(input("Ingrese un dia: Lunes(1), Martes(2)"))
                    if dia == 1:
                            if lunes1 == "":
                                print("Turno 1: Libre")
                            else:
                                    print("Turno 1: ", lunes1)
                            if lunes2 == "":
                                print("Turno 2: Libre")
                            else:
                                print("Turno 2: ", lunes2)
                            if lunes3 == "":
                                print("Turno 3: Libre")
                            else:
                                print("Turno 3: ", lunes3)
                            if lunes4 == "":
                                print("Turno 4: Libre")
                            else:
                                print("Turno 4: ", lunes4)

                    if dia == 2:
                            if martes1 == "":
                                print("Turno Martes 1: Libre")
                            else:
                                print("Turno Martes 1: ", martes1)
                            if martes2 == "":
                                print("Turno Martes 2: Libre")
                            else:
                                print("Turno Martes 2: ", martes2)
                            if martes3 == "":
                                print("Turno Martes 3: Libre")
                            else:
                                print("Turno Martes 3: ", martes3)

                    
                case "4":
                    total = 7
                    ocupados = 0
                    ocupados_lunes = 0
                    ocupados_martes = 0
                    disponibles = 0
                    ocupados_lunes += 1
                    if lunes1 != "":
                        ocupados_lunes += 1
                    if lunes2 != "":
                        ocupados_lunes += 1
                    if lunes3 != "":
                        ocupados_lunes += 1
                    if lunes4 != "":
                        ocupados_lunes += 1
                    if martes1 != "":
                        ocupados_martes += 1
                    if martes2 != "":
                        ocupados_martes += 1
                    if martes3 != "":
                        ocupados_martes += 1

                    ocupados += ocupados_lunes + ocupados_martes

                    disponibles = total - ocupados
                    print("Lunes: ", ocupados_lunes)
                    print("Martes: ", ocupados_martes)
                    if ocupados_lunes > ocupados_martes:
                        print("Dias mas ocupados")
                    else:
                        print("Dias mas ocupados")

                case "5":
                    break

#Ejercicio 4
    case 4:
        energia = 100
        tiempo = 12
        cerraduras_abiertas = 0
        alarma = False
        codigo_parcial = ""
        forzar_seguidas = 0

        nombre_agente = input("Ingrese el nombre edl agente: ")
        while nombre_agente == "" or not nombre_agente.isalpha():
            nombre_agente = input("Ingrese bien el nombre: ")

        while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
            if alarma and tiempo <= 3:
                print("Sistema bloqueado")
                break
            menu = ["1. Forzar", "2. Hackear", "3. Descansar"]
            for opcion in menu:
                print(opcion)
            opcion = input("Elije una opcion(1, 2, 3): ")
            while not opcion.isdigit():
                opcion = input("Elije un numero(1, 2, 3)")
            if opcion != "1":
                forzar_seguidas = 0

            match opcion:
                case "1":
                    energia -= 20
                    tiempo -= 2
                    forzar_seguidas += 1
                    numero_cerradura = "0"
                    if forzar_seguidas >= 3:
                        print("La cerradura no abre")
                        alarma = True
                        print("La alarma se ha activado")
                    else:
                        if energia < 40:
                            numero_cerradura = input("Elige un numero del 1 al 3: ")
                            while not numero_cerradura.isdigit():
                                numero_cerradura = input("Ingrese un numero (1, 2, 3)")
                        if numero_cerradura == "3":
                            alarma = True
                            print("La alarma se ha activado")
                        if alarma == False:
                            cerraduras_abiertas += 1
                            print("La cerradura se ha abierto")
                
                case "2":
                    energia -= 10
                    tiempo -= 3
                
                    for i in range(1, 5):
                        print(f"Paso {i}/4 - Hackeando...")
                        codigo_parcial += "A"
                    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print("Se ha abierto la cerradura")

                case "3":
                    energia += 15
                    if energia > 100:
                        energia = 100
                    tiempo -= 1
                    if alarma == True:
                        energia -= 10

            if cerraduras_abiertas == 3: 
                print(f"{nombre_agente} ha ganado")
            elif alarma == True and tiempo <= 3:
                print("Ha perdido por bloqueo de sistema")
            else:
                print("Ha perdido por energia o tiempo agotado")

#Ejercicio 5
    case 5:
        print("--- BIENVENIDO A LA ARENA ---")
        nombre_gladiador = input("Ingresa el nombre del gladiador: ")
        while nombre_gladiador == "" or not nombre_gladiador.isalpha():
            nombre_gladiador = input("Error. Utiliza solo letras, intenta de nuevo: ")

        vida_gladiador = 100
        vida_enemigo = 100
        pocion_vida = 3
        ataque_pesado = 15
        golpe_enemigo = 12
        turno_gladiador = True

        print("=== INICIO DEL COMBATE ===")

        while vida_enemigo > 0 and vida_gladiador > 0:
            print(f"Vida de {nombre_gladiador}: {vida_gladiador}\nVida Enemigo: {vida_enemigo}\nPociones de vida: {pocion_vida}")

            menu = ["1. Ataque pesado", "2. Rafaga veloz", "3. Curar"]
            for opcion in menu:
                print(opcion)
            opcion = input("Ingresa una opcion (1, 2, 3): ")
            while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
                opcion = input("Error. Ingrese una opcion [1, 2, 3]")
            
            match opcion:
                case "1":
                    if vida_enemigo < 20:
                        dano = ataque_pesado * 1.5
                        vida_enemigo -= dano
                        print(f"Has hecho dano al enemigo, su vida: {vida_enemigo}")
                    else:
                        vida_enemigo -= ataque_pesado
                        print(f"Has hecho dano al enemigo, su vida: {vida_enemigo}")

                case "2":
                    for i in range(1, 4):
                        vida_enemigo -= 5
                        print("Golpe conectado por 5 de dano")

                case "3":
                    if pocion_vida > 0:
                        vida_gladiador += 30
                        pocion_vida -= 1
                        print(f"Te has curado, tu vida: {vida_gladiador}")
                    else:
                        print("No te quedan pociones")
                
            vida_gladiador -= golpe_enemigo
            print(f"El enemigo golpea y hace 12 de dano, tu vida es {vida_gladiador}")

        if vida_gladiador > 0:
            print(f"Victoria, {nombre_gladiador} ha ganado la batalla.")
        else:
            print("Derrota. Has caido en combate")