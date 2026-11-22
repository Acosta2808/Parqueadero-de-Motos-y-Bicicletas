from datetime import datetime


def buscar_usuario(usuarios, nombre):
    for i in range(len(usuarios)):
        if usuarios[i][0] == nombre:
            return i
    return -1


def buscar_vehiculo(vehiculos, identificador):
    for i in range(len(vehiculos)):
        if vehiculos[i][0] == identificador:
            return i
    return -1


def buscar_tarifa(tarifas, tipo):
    for i in range(len(tarifas)):
        if tarifas[i][0] == tipo:
            return i
    return -1


def iniciar_sesion(usuarios):
    print("\n=== INICIO DE SESIÓN ===")
    nombre = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    i = buscar_usuario(usuarios, nombre)

    if i == -1:
        print("ERROR: Usuario inexistente.")
        return ""
    if usuarios[i][3] == 0:
        print("ERROR: La cuenta está desactivada.")
        return ""
    if usuarios[i][1] != contraseña:
        print("ERROR: Contraseña incorrecta.")
        return ""

    print("Bienvenido,", nombre, "- Rol:", usuarios[i][2])
    return nombre


def mostrar_menu_admin():
    print("\n--- MENÚ ADMINISTRADOR ---")
    print("1. Gestionar usuarios")
    print("2. Configurar tarifas")
    print("3. Configurar capacidad")
    print("4. Consultar auditoría y caja")
    print("5. Consultar disponibilidad")
    print("6. Cerrar sesión")


def gestionar_usuarios(usuarios):
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Crear vigilante")
        print("2. Editar vigilante")
        print("3. Activar/desactivar vigilante")
        print("4. Restablecer contraseña")
        print("5. Ver usuarios")
        print("6. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre de usuario: ").strip()
            if buscar_usuario(usuarios, nombre) != -1:
                print("ERROR: El usuario ya existe.")
            elif nombre == "":
                print("ERROR: El usuario no puede estar vacío.")
            else:
                contraseña = input("Contraseña inicial: ").strip()
                usuarios.append([nombre, contraseña, "OPERARIO", 1])
                print("Vigilante creado correctamente.")

        elif opcion == "2":
            nombre = input("Usuario a editar: ").strip()
            i = buscar_usuario(usuarios, nombre)
            if i == -1 or usuarios[i][2] != "OPERARIO":
                print("ERROR: Vigilante no encontrado.")
            else:
                nuevo = input("Nuevo nombre (Enter para conservar): ").strip()
                if nuevo != "":
                    usuarios[i][0] = nuevo
                    print("Nombre actualizado.")

        elif opcion == "3":
            nombre = input("Usuario vigilante: ").strip()
            i = buscar_usuario(usuarios, nombre)
            if i == -1 or usuarios[i][2] != "OPERARIO":
                print("ERROR: Vigilante no encontrado.")
            else:
                usuarios[i][3] = 0 if usuarios[i][3] == 1 else 1
                estado = "activa" if usuarios[i][3] == 1 else "desactivada"
                print("Cuenta", estado)

        elif opcion == "4":
            nombre = input("Usuario vigilante: ").strip()
            i = buscar_usuario(usuarios, nombre)
            if i == -1 or usuarios[i][2] != "OPERARIO":
                print("ERROR: Vigilante no encontrado.")
            else:
                usuarios[i][1] = input("Nueva contraseña: ").strip()
                print("Contraseña restablecida.")

        elif opcion == "5":
            print("\n--- USUARIOS ---")
            for usuario in usuarios:
                estado = "Activo" if usuario[3] == 1 else "Inactivo"
                print(usuario[0], "|", usuario[2], "|", estado)

        elif opcion == "6":
            break
        else:
            print("ERROR: Opción no válida.")


def configurar_tarifas(tarifas):
    print("\n--- CONFIGURACIÓN DE TARIFAS ---")
    for tarifa in tarifas:
        print("\n", tarifa[0])
        print("Fracción:", tarifa[1])
        print("Hora:", tarifa[2])
        print("Día:", tarifa[3])
        print("Mes:", tarifa[4])

        if input("¿Modificar esta tarifa? (s/n): ").strip().lower() == "s":
            periodos = ["Fracción", "Hora", "Día", "Mes"]
            for j in range(4):
                try:
                    nuevo = float(input(periodos[j] + ": ").strip())
                    if nuevo < 0:
                        print("ERROR: El valor no puede ser negativo.")
                    else:
                        tarifa[j + 1] = nuevo
                except ValueError:
                    print("ERROR: Precio no válido.")


def configurar_capacidad(capacidad):
    print("\n--- CONFIGURACIÓN DE CAPACIDAD ---")
    try:
        nueva_motos = int(input("Nueva capacidad de motos: ").strip())
        nueva_bicis = int(input("Nueva capacidad de bicicletas: ").strip())
        if nueva_motos < 0 or nueva_bicis < 0:
            print("ERROR: La capacidad no puede ser negativa.")
        else:
            capacidad[0][1] = nueva_motos
            capacidad[1][1] = nueva_bicis
            print("Capacidad actualizada.")
    except ValueError:
        print("ERROR: Use números enteros.")


def contar_vehiculos(vehiculos, tipo):
    total = 0
    for vehiculo in vehiculos:
        if vehiculo[1] == tipo:
            total = total + 1
    return total


def consultar_disponibilidad(vehiculos, capacidad):
    print("\n--- DISPONIBILIDAD ---")
    for i in range(len(capacidad)):
        tipo = capacidad[i][0]
        cupos = capacidad[i][1]
        ocupados = contar_vehiculos(vehiculos, tipo)
        libres = cupos - ocupados
        if cupos > 0:
            porcentaje = ocupados * 100 / cupos
        else:
            porcentaje = 0
        print(tipo, "ocupadas:", ocupados, "de", cupos,
              "- libres:", libres,
              "- ocupación:", round(porcentaje, 1), "%")

        if porcentaje >= 90:
            print("ALERTA: La zona superó el 90% de ocupación.")


def registrar_ingreso(vehiculos, capacidad, operario):
    print("\n--- REGISTRO DE INGRESO ---")
    opcion = input("Tipo (1 Moto, 2 Bicicleta): ").strip()

    if opcion == "1":
        tipo = "Moto"
        identificador = input("Placa: ").strip().upper()
    elif opcion == "2":
        tipo = "Bicicleta"
        identificador = input("Cédula/código del tiquete: ").strip()
    else:
        print("ERROR: Tipo no válido.")
        return

    if identificador == "":
        print("ERROR: La identificación no puede estar vacía.")
        return
    if buscar_vehiculo(vehiculos, identificador) != -1:
        print("ERROR: El vehículo ya está dentro.")
        return

    i = 0 if tipo == "Moto" else 1
    ocupados = contar_vehiculos(vehiculos, tipo)
    if ocupados >= capacidad[i][1]:
        print("ALERTA: No hay cupos disponibles.")
        return

    marca = input("Marca: ").strip()
    color = input("Color: ").strip()
    novedades = input("Novedades iniciales (Enter si ninguna): ").strip()
    vehiculos.append([
        identificador,
        tipo,
        marca,
        color,
        novedades,
        operario,
        datetime.now(),
    ])
    print("Ingreso registrado:", tipo, "-", identificador)


def calcular_tiempo(hora_ingreso):
    hora_actual = datetime.now()
    minutos = int((hora_actual - hora_ingreso).total_seconds() // 60)
    if minutos < 1:
        minutos = 1
    return minutos


def registrar_salida(vehiculos, tarifas, caja_operario,
                     caja_global, transacciones, operario):
    print("\n--- REGISTRO DE SALIDA Y COBRO ---")
    identificador = input("Placa o código: ").strip().upper()
    i = buscar_vehiculo(vehiculos, identificador)
    if i == -1:
        print("AVISO: No se encontró el vehículo.")
        return caja_global, caja_operario

    minutos = calcular_tiempo(vehiculos[i][6])
    print("Tiempo transcurrido:", minutos, "minutos")

    tipo = vehiculos[i][1]
    tarifa_por_minuto = 3000
    monto = minutos * tarifa_por_minuto

    print("Tarifa de prueba: $3.000 por minuto")
    print("Monto a cobrar por", tipo + ":", monto)
    if input("¿Confirmar pago? (s/n): ").strip().lower() != "s":
        print("Salida cancelada.")
        return caja_global, caja_operario

    caja_operario = caja_operario + monto
    caja_global = caja_global + monto
    transacciones.append([identificador, tipo, operario, monto, "PAGADO"])
    vehiculos.pop(i)
    print("Pago confirmado y salida registrada.")
    print("Caja actual del operario:", caja_operario)
    return caja_global, caja_operario


def registrar_novedad(vehiculos):
    print("\n--- NOVEDAD DE SEGURIDAD ---")
    identificador = input("Placa o código: ").strip().upper()
    i = buscar_vehiculo(vehiculos, identificador)
    if i == -1:
        print("AVISO: No se encontró el vehículo.")
        return

    novedad = input("Describa el incidente o daño: ").strip()
    if novedad == "":
        print("ERROR: La novedad no puede estar vacía.")
    else:
        if vehiculos[i][4] != "":
            vehiculos[i][4] = vehiculos[i][4] + "; "
        vehiculos[i][4] = vehiculos[i][4] + novedad
        print("Novedad registrada.")


def cerrar_turno(operario, caja_operario, turnos_cerrados):
    turnos_cerrados.append([operario, caja_operario])
    print("Cierre de turno realizado.")
    print("Total recaudado:", caja_operario)
    return 0


def mostrar_auditoria(caja_global, transacciones, turnos_cerrados,
                      tiquetes_anulados):
    print("\n--- AUDITORÍA Y CAJA ---")
    print("Ingresos globales:", caja_global)
    print("Tiquetes anulados:", len(tiquetes_anulados))

    print("\nHistorial de pagos:")
    if len(transacciones) == 0:
        print("No hay pagos registrados.")
    for pago in transacciones:
        print(pago)

    print("\nHistorial de turnos cerrados:")
    if len(turnos_cerrados) == 0:
        print("No hay turnos cerrados.")
    for turno in turnos_cerrados:
        print(turno)


def exportar_reporte(caja_global, transacciones, turnos_cerrados,
                     tiquetes_anulados):
    archivo = open("reporte_parqueadero.txt", "w", encoding="utf-8")
    archivo.write("REPORTE PARQUEADERO CAMPUS SEGURO\n")
    archivo.write("Ingresos globales: " + str(caja_global) + "\n\n")
    archivo.write("Pagos:\n")
    for pago in transacciones:
        archivo.write(str(pago) + "\n")
    archivo.write("\nTurnos cerrados:\n")
    for turno in turnos_cerrados:
        archivo.write(str(turno) + "\n")
    archivo.write("\nTiquetes anulados:\n")
    for tiquete in tiquetes_anulados:
        archivo.write(str(tiquete) + "\n")
    archivo.close()
    print("Reporte exportado como reporte_parqueadero.txt")


def menu_admin(usuarios, tarifas, capacidad, vehiculos, caja_global,
               transacciones, turnos_cerrados, tiquetes_anulados):
    while True:
        mostrar_menu_admin()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            gestionar_usuarios(usuarios)
        elif opcion == "2":
            configurar_tarifas(tarifas)
        elif opcion == "3":
            configurar_capacidad(capacidad)
        elif opcion == "4":
            while True:
                print("\n1. Ver auditoría")
                print("2. Registrar tiquete anulado")
                print("3. Exportar reporte")
                print("4. Volver")
                subopcion = input("Seleccione una opción: ").strip()

                if subopcion == "1":
                    mostrar_auditoria(
                        caja_global,
                        transacciones,
                        turnos_cerrados,
                        tiquetes_anulados,
                    )
                elif subopcion == "2":
                    motivo = input("Motivo de la anulación: ").strip()
                    if motivo == "":
                        print("ERROR: El motivo no puede estar vacío.")
                    else:
                        tiquetes_anulados.append([motivo])
                        print("Tiquete anulado registrado.")
                elif subopcion == "3":
                    exportar_reporte(
                        caja_global,
                        transacciones,
                        turnos_cerrados,
                        tiquetes_anulados,
                    )
                elif subopcion == "4":
                    break
        elif opcion == "5":
            consultar_disponibilidad(vehiculos, capacidad)
        elif opcion == "6":
            print("Sesión de administrador cerrada.")
            break
        else:
            print("ERROR: Opción no válida.")


def mostrar_menu_operario():
    print("\n--- MENÚ OPERARIO ---")
    print("1. Registrar ingreso")
    print("2. Registrar salida y cobrar")
    print("3. Registrar novedad de seguridad")
    print("4. Cerrar turno")
    print("5. Consultar disponibilidad")
    print("6. Cerrar sesión")


def menu_operario(nombre, tarifas, capacidad, vehiculos, caja_global,
                  transacciones, turnos_cerrados):
    caja_operario = 0

    while True:
        mostrar_menu_operario()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_ingreso(vehiculos, capacidad, nombre)
        elif opcion == "2":
            caja_global, caja_operario = registrar_salida(
                vehiculos,
                tarifas,
                caja_operario,
                caja_global,
                transacciones,
                nombre,
            )
        elif opcion == "3":
            registrar_novedad(vehiculos)
        elif opcion == "4":
            caja_operario = cerrar_turno(
                nombre,
                caja_operario,
                turnos_cerrados,
            )
        elif opcion == "5":
            consultar_disponibilidad(vehiculos, capacidad)
        elif opcion == "6":
            print("Sesión de operario cerrada.")
            break
        else:
            print("ERROR: Opción no válida.")

    return caja_global


def main():
    usuarios = [
        ["admin", "admin123", "ADMIN", 1],
        ["operario", "operario123", "OPERARIO", 1],
    ]
    tarifas = [
        ["Moto", 2000, 3000, 30000, 150000],
        ["Bicicleta", 1000, 2000, 15000, 75000],
    ]
    capacidad = [
        ["Moto", 50],
        ["Bicicleta", 30],
    ]
    vehiculos = []
    transacciones = []
    turnos_cerrados = []
    tiquetes_anulados = []
    caja_global = 0

    print("=== PARQUEADERO CAMPUS SEGURO ===")
    while True:
        nombre = iniciar_sesion(usuarios)
        if nombre == "":
            if input("¿Intentar nuevamente? (s/n): ").strip().lower() != "s":
                break
            continue

        i = buscar_usuario(usuarios, nombre)
        if usuarios[i][2] == "ADMIN":
            menu_admin(
                usuarios,
                tarifas,
                capacidad,
                vehiculos,
                caja_global,
                transacciones,
                turnos_cerrados,
                tiquetes_anulados,
            )
        else:
            caja_global = menu_operario(
                nombre,
                tarifas,
                capacidad,
                vehiculos,
                caja_global,
                transacciones,
                turnos_cerrados,
            )


if __name__ == "__main__":
    main()
