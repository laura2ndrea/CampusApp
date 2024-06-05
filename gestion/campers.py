import data.datos as dataOpciones
import menu.opciones as menuOpciones

def mostrar_campers(estado = None): 
    # Se cargan los datos desde el JSON
    campers = dataOpciones.cargar_datos("data\campers.json")

    if campers: 
        print(f"Lista de campers con estado: {estado if estado else "Registrado"}:")
        # Se muestran los campers segun el estado
        for doc_camper, datos_camper in campers.items(): 
            if not estado or datos_camper.get("estado") == estado:
                menuOpciones.mini_separador()
                print(f"Documento: {doc_camper}")
                for clave, valor in datos_camper.items():
                    print(f" - {clave.capitalize()}: {valor}")
    else: 
        print("No hay campers registrados")

def campers_bajoRendimiento():
        # Se cargan los datos 
        campers = dataOpciones.cargar_datos("data\campers.json")

        print("Campers con bajo rendimiento:")
        # Recorrer e imprimir los campers que esten en riesgo alto (bajo rendimiento)
        for doc_camper, datos_camper in campers.items():
            if datos_camper["riesgo"] == "Alto":
                menuOpciones.mini_separador()
                print(f"Documento: {doc_camper}")
                for clave, valor in datos_camper.items():
                    print(f" - {clave.capitalize()}: {valor}")

def camper_crearNotas(doc, ruta):
    
    notas = dataOpciones.cargar_datos("data/notas.json")

    modulos = {
        "Fundamentos de programación": {
            "quices_trabajos": 0,
            "prueba_teorica": 0,
            "prueba_practica": 0,
            "promedio": 0,
            "estado": "",
            "advertencias": []
        },
        "Programación Web": {
            "quices_trabajos": 0,
            "prueba_teorica": 0,
            "prueba_practica": 0,
            "promedio": 0,
            "estado": "",
            "advertencias": []
        },
        "Programación formal": {
            "quices_trabajos": 0,
            "prueba_teorica": 0,
            "prueba_practica": 0,
            "promedio": 0,
            "estado": "",
            "advertencias": []
        },
        "Bases de datos": {
            "quices_trabajos": 0,
            "prueba_teorica": 0,
            "prueba_practica": 0,
            "promedio": 0,
            "estado": "",
            "advertencias": []
        },
        "Backend": {
            "quices_trabajos": 0,
            "prueba_teorica": 0,
            "prueba_practica": 0,
            "promedio": 0,
            "estado": "",
            "advertencias": []
        }
    }

    notas[doc] = {
        "ruta": ruta,
        "modulos": modulos
    }

    dataOpciones.guardar_datos("data/notas.json", notas)

def crear_camper(): 
    
    campers = dataOpciones.cargar_datos("data/campers.json")
    camper = {}

    while True:
        doc = input("Ingrese el documento del nuevo camper: ").strip()
        if doc in campers:
            print("¡El documento ya está registrado!")
        elif doc =="":
            print("Debe ingresar un numero de documento")
        else:
            break
    

    while True:
        nombres = input("Ingrese nombres: ").strip()
        if nombres:
            break
        else:
            print("Error: Debe ingresar nombres.")
    
    while True:
        apellidos = input("Ingrese apellidos: ").strip()
        if apellidos:
            break
        else:
            print("Error: Debe ingresar apellidos.")
    
    while True:
        direccion = input("Ingrese la dirección: ").strip()
        if direccion:
            break
        else:
            print("Error: Debe ingresar la dirección.")
    
    while True:
        acudiente = input("Ingrese el nombre del acudiente: ").strip()
        if acudiente:
            break
        else:
            print("Error: Debe ingresar el nombre del acudiente.")
    
    while True:
        telefono_celular = input("Ingrese teléfono celular: ").strip()
        if telefono_celular:
            break
        else:
            print("Error: Debe ingresar el teléfono celular.")
    
    while True:
        telefono_fijo = input("Ingrese teléfono fijo: ").strip()
        if telefono_fijo:
            break
        else:
            print("Error: Debe ingresar el teléfono fijo.")

    camper["nombres"] = nombres
    camper["apellidos"] = apellidos
    camper["direccion"] = direccion
    camper["acudiente"] = acudiente
    camper["telefono_celular"] = telefono_celular
    camper["telefono_fijo"] = telefono_fijo
    camper["estado"] = "Inscrito"
    camper["riesgo"] = ""
    camper["pruebaIngreso"] = {
        "nota_practica": 0,
        "nota_teorica": 0,
        "promedio": 0
    }
    
    campers[doc] = camper
    
    dataOpciones.guardar_datos("data/campers.json", campers)
    
    print("¡Nuevo camper agregado exitosamente!")

def actualizar_camper(): 
    campers = dataOpciones.cargar_datos("data\campers.json")
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return

    print("Datos actuales del camper:")
    for clave, valor in campers[doc].items():
        if clave not in ["pruebaIngreso", "estado", "riesgo"]: 
            print(f"{clave.capitalize()}: {valor}")

    campo_actualizar = input("Ingrese el campo que desea actualizar: ").strip().lower()
    if campo_actualizar not in campers[doc] or campo_actualizar in ["pruebaingreso", "estado", "riesgo"]:
        print("El campo ingresado no existe.")
        return

    nuevo_valor = input(f"Ingrese el nuevo valor para '{campo_actualizar.capitalize()}': ").strip()
    campers[doc][campo_actualizar] = nuevo_valor

    dataOpciones.guardar_datos("data\campers.json", campers)

def cambiar_estado():
    campers = dataOpciones.cargar_datos("data/campers.json")
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return

    print(f"Estado actual del camper: {campers[doc]['estado']}")
    print("Opciones de estado: Graduado, Expulsado, Retirado")

    while True:
        nuevo_estado = input("Ingrese el nuevo estado del camper: ").strip().capitalize()
        if nuevo_estado not in ["Graduado", "Expulsado", "Retirado"]:
            print("El estado ingresado no es válido. Por favor, ingrese un estado válido (Graduado, Expulsado, Retirado).")
        else:
            break

    campers[doc]["estado"] = nuevo_estado
    dataOpciones.guardar_datos("data/campers.json", campers)
    print("Estado del camper actualizado correctamente.")

def notas_prueba_ingreso():
    campers = dataOpciones.cargar_datos("data/campers.json")
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return

    if campers[doc]["pruebaIngreso"]["promedio"] != 0:
        print("Las notas de la prueba de ingreso ya han sido ingresadas.")
        return

    while True:
        try:
            nota_practica = float(input("Ingrese la nota de la prueba práctica (0-100): "))
            if nota_practica < 0 or nota_practica > 100:
                print("La nota de la prueba práctica debe ser entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entre 0 y 100.")

    while True:
        try:
            nota_teorica = float(input("Ingrese la nota de la prueba teórica (0-100): "))
            if nota_teorica < 0 or nota_teorica > 100:
                print("La nota de la prueba teórica debe ser entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entre 0 y 100.")

    promedio = (nota_practica + nota_teorica) / 2
    campers[doc]["pruebaIngreso"]["nota_practica"] = nota_practica
    campers[doc]["pruebaIngreso"]["nota_teorica"] = nota_teorica
    campers[doc]["pruebaIngreso"]["promedio"] = promedio

    if promedio >= 60:
        campers[doc]["estado"] = "Aprobado"

    dataOpciones.guardar_datos("data/campers.json", campers)
    print("Notas de la prueba de ingreso ingresadas correctamente.")

def crear_advertencias(): 
    notas = dataOpciones.cargar_datos("data/notas.json")
    
    doc_camper = input("Ingrese el documento del camper: ").strip()
    
    if doc_camper not in notas:
        print("¡El documento del camper no se encuentra registrado!")
        return
    
    modulos_disponibles = list(notas[doc_camper]['modulos'].keys())
    print("Módulos disponibles:")
    for idx, modulo in enumerate(modulos_disponibles, start=1):
        print(f"{idx}. {modulo}")
    
    while True:
        try:
            opcion_modulo = int(input("Seleccione un módulo (número): "))
            if 1 <= opcion_modulo <= len(modulos_disponibles):
                break
            else:
                print("Número de módulo fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")
    
    modulo_elegido = modulos_disponibles[opcion_modulo - 1]
    
    advertencia = input("Escriba la advertencia para este módulo: ").strip()
    
    notas[doc_camper]['modulos'][modulo_elegido]['advertencias'].append(advertencia)
    
    dataOpciones.guardar_datos("data/notas.json", notas)
    
    print("¡Advertencia agregada exitosamente!")

def monstrarInformacion_camper(doc): 
    campers = dataOpciones.cargar_datos("data/campers.json")

    if doc in campers:
        camper = campers[doc]
        print("Información del Camper:")
        print(f"Documento: {doc}")
        print(f"Nombres: {camper['nombres']}")
        print(f"Apellidos: {camper['apellidos']}")
        print(f"Dirección: {camper['direccion']}")
        print(f"Nombre del Acudiente: {camper['acudiente']}")
        print(f"Télefono Celular: {camper['telefono_celular']}")
        print(f"Télefono Fijo: {camper['telefono_fijo']}")
        print(f"Estado: {camper['estado']}")
        print(f"Riesgo: {camper['riesgo']}")

def mostrarRuta_camper(doc): 
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    for ruta, info_ruta in rutas.items():
        grupos = info_ruta.get("grupos", {})
        for grupo, info_grupo in grupos.items():
            if doc in info_grupo.get("campers_ids", []):
                horario = info_grupo.get("horario", "No definido")
                salon = info_grupo.get("salon", "No definido")
                print(f"El camper con documento {doc} pertenece a la ruta: {ruta}")
                print(f"Grupo: {grupo}")
                print(f"Horario del grupo: {horario}")
                print(f"Salón del grupo: {salon}")
                return
    print(f"No se encontró al camper con documento {doc} en ninguna ruta.")

def mostrarNotas_camper(doc): 
    notas = dataOpciones.cargar_datos("data/notas.json")
    if doc in notas:
        notas_camper = notas[doc]
        print(f"Notas del Camper con documento {doc}:")
        for modulo, info_modulo in notas_camper['modulos'].items():
            print(f"\nMódulo: {modulo}")
            print(f" - Quices y trabajos: {info_modulo['quices_trabajos']}")
            print(f" - Prueba teórica: {info_modulo['prueba_teorica']}")
            print(f" - Prueba práctica: {info_modulo['prueba_practica']}")
            print(f" - Promedio: {info_modulo['promedio']}")
            print(f" - Estado: {info_modulo['estado']}")
            if info_modulo['advertencias']:
                print(f" - Advertencias: {', '.join(info_modulo['advertencias'])}")
            else:
                print(" - Advertencias: Ninguna")
    else:
        print(f"No se encontraron notas para el Camper con documento {doc}.")