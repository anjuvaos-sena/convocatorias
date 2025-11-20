# =====================================================
# CONFIGURADOR DIDÁCTICO DE SWITCH CISCO 2960
# FASE 1: Recolección de datos (sin conexión real)
# Autor: José Fernando Murillo Arango
# =====================================================

def menu():
    configuracion = {
        "ip_vlan1": [],
        "hostname": [],
        "vlans": [],
        "puertos_vlan": [],
        "clave_consola": [],
        "clave_privilegiado": [],
        "cifrado": []
    }

    while True:
        print("\n===============================")
        print("   CONFIGURADOR SWITCH CISCO")
        print("===============================")
        print("1. Asignar dirección IP al switch")
        print("2. Asignar nombre al switch")
        print("3. Configurar VLANs")
        print("4. Asignar puertos a VLANs")
        print("5. Asignar clave para ingresar al switch (consola)")
        print("6. Asignar clave para modo privilegiado")
        print("7. Activar cifrado de contraseñas")
        print("8. Ver configuración almacenada")
        print("9. Configurar dispositivo")
        print("10. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                asignar_direccion_ip(configuracion)
            case "2":
                asignar_nombre_switch(configuracion)
            case "3":
                configurar_vlans(configuracion)
            case "4":
                asignar_puertos_vlan(configuracion)
            case "5":
                asignar_clave_consola(configuracion)
            case "6":
                asignar_clave_privilegiado(configuracion)
            case "7":
                activar_cifrado_contraseñas(configuracion)
            case "8":
                ver_configuracion(configuracion)
            case "9":
                aplicar_configuraciones(configuracion)
            case "10":
                print("\n Saliendo del configurador. Hasta pronto.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

        '''if opcion == "1":
            asignar_direccion_ip(configuracion)
        elif opcion == "2":
            asignar_nombre_switch(configuracion)
        elif opcion == "3":
            configurar_vlans(configuracion)
        elif opcion == "4":
            asignar_puertos_vlan(configuracion)
        elif opcion == "5":
            asignar_clave_consola(configuracion)
        elif opcion == "6":
            asignar_clave_privilegiado(configuracion)
        elif opcion == "7":
            activar_cifrado_contraseñas(configuracion)
        elif opcion == "8":
            ver_configuracion(configuracion)
        elif opcion == "9":
            aplicar_configuraciones(configuracion)
        elif opcion == "10":
            print("\n Saliendo del configurador. Hasta pronto.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")'''


def asignar_direccion_ip(config):
    print("\n--- ASIGNAR DIRECCIÓN IP AL SWITCH ---")
    ip = input("Ingrese la dirección IP del switch: ")
    mascara = input("Ingrese la máscara de subred: ")

    comandos = [
        "enable",
        "configure terminal",
        "interface vlan 1",
        f"ip address {ip} {mascara}",
        "no shutdown",
        "end",
        "copy running-config startup-config"
    ]

    config["ip_vlan1"] = comandos
    print("\n Dirección IP configurada y guardada en memoria temporal.")


def asignar_nombre_switch(config):
    print("\n--- ASIGNAR NOMBRE AL SWITCH ---")
    nombre = input("Ingrese el nombre del switch: ")

    comandos = [
        "enable",
        "configure terminal",
        f"hostname {nombre}",
        "end",
        "copy running-config startup-config"
    ]

    config["hostname"] = comandos
    print(f"\n Nombre '{nombre}' configurado y guardado en memoria temporal.")


def configurar_vlans(config):
    print("\n--- CONFIGURAR VLANS ---")
    num_vlans = int(input("¿Cuántas VLANs desea crear?: "))
    comandos = ["enable", "configure terminal"]

    for i in range(num_vlans):
        vlan_id = input(f"Ingrese el número de la VLAN {i+1}: ")
        vlan_name = input(f"Ingrese el nombre de la VLAN {vlan_id}: ")
        comandos.append(f"vlan {vlan_id}")
        comandos.append(f"name {vlan_name}")
        comandos.append("exit")

    comandos.append("end")
    comandos.append("copy running-config startup-config")

    config["vlans"] = comandos
    print("\n VLANs configuradas y guardadas en memoria temporal.")


def asignar_puertos_vlan(config):
    print("\n--- ASIGNAR PUERTOS A VLAN ---")
    comandos = ["enable", "configure terminal"]
    num_grupos = int(input("¿Cuántos grupos de puertos desea configurar?: "))

    for i in range(num_grupos):
        rango = input(f"Ingrese el rango de puertos (ejemplo: fa0/1-8) del grupo {i+1}: ")
        vlan = input(f"Ingrese el número de VLAN para el rango {rango}: ")

        comandos.append(f"interface range {rango}")
        comandos.append("switchport mode access")
        comandos.append(f"switchport access vlan {vlan}")
        comandos.append("exit")

    comandos.append("end")
    comandos.append("copy running-config startup-config")

    config["puertos_vlan"] = comandos
    print("\n Puertos asignados a VLAN y guardados en memoria temporal.")


def asignar_clave_consola(config):
    print("\n--- ASIGNAR CLAVE PARA INGRESAR AL SWITCH (CONSOLa) ---")
    clave = input("Ingrese la contraseña para acceso por consola: ")

    comandos = [
        "enable",
        "configure terminal",
        "line console 0",
        f"password {clave}",
        "login",
        "end",
        "copy running-config startup-config"
    ]

    config["clave_consola"] = comandos
    print("\n Clave de consola configurada y guardada en memoria temporal.")


def asignar_clave_privilegiado(config):
    print("\n--- ASIGNAR CLAVE PARA MODO PRIVILEGIADO ---")
    clave = input("Ingrese la contraseña para modo privilegiado (enable): ")

    comandos = [
        "enable",
        "configure terminal",
        f"enable password {clave}",
        "end",
        "copy running-config startup-config"
    ]

    config["clave_privilegiado"] = comandos
    print("\n Clave del modo privilegiado configurada y guardada en memoria temporal.")


def activar_cifrado_contraseñas(config):
    print("\n--- ACTIVAR CIFRADO DE CONTRASEÑAS ---")

    comandos = [
        "enable",
        "configure terminal",
        "service password-encryption",
        "end",
        "copy running-config startup-config"
    ]

    config["cifrado"] = comandos
    print("\n Cifrado de contraseñas activado y guardado en memoria temporal.")


def ver_configuracion(config):
    print("\n--- CONFIGURACIÓN ACUMULADA ---")
    if not any(config.values()):
        print(" No hay configuraciones almacenadas aún.")
        return

    for seccion, comandos in config.items():
        if comandos:
            print(f"\n[{seccion.upper()}]")
            for cmd in comandos:
                print(f"  {cmd}")




def aplicar_configuraciones(config):
    """
    Aplica al switch todas las configuraciones almacenadas en el diccionario recibido.
    Requiere conexión SSH válida.    
    """

    from netmiko import ConnectHandler
    import getpass

    if not config:
        print(" No se recibió ninguna configuración para aplicar.\n")
        return

    print("\n=== APLICAR CONFIGURACIONES AL SWITCH ===")
    host = input("IP del switch: ")
    usuario = input("Usuario SSH: ")
    password = getpass.getpass("Contraseña: ")

    dispositivo = {
        "device_type": "cisco_ios",
        "host": host,
        "username": usuario,
        "password": password
    }

    try:
        print("\nConectando al switch...")
        conexion = ConnectHandler(**dispositivo)
        conexion.enable()

        print("\n Conexión establecida correctamente.\n")
        print("Aplicando configuraciones...\n")

        for clave, comandos in config.items():
            print(f"  Aplicando sección: {clave}")
            salida = conexion.send_config_set(comandos)
            print(salida)
            print("-" * 50)

        conexion.disconnect()
        print("\n Todas las configuraciones se aplicaron correctamente.\n")

    except Exception as e:
        print(f"\n Error al conectar o aplicar configuraciones: {e}\n")



# Punto de entrada principal
if __name__ == "__main__":
    menu()
