import data.datos as dataOpciones
import menu.opciones as menuOpciones

def mostrar_campers(estado = None): 
    # Se cargan los datos desde el JSON
    campers = dataOpciones.cargar_datos("data/campers.json")

    if campers: 
        print(f"Lista de campers con estado: {estado if estado else 'Registrado'}:")
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
        campers = dataOpciones.cargar_datos("data/campers.json")

        print("Campers con bajo rendimiento:")
        # Recorrer e imprimir los campers que esten en riesgo alto (bajo rendimiento)
        for doc_camper, datos_camper in campers.items():
            if datos_camper["riesgo"] == "Alto":
                menuOpciones.mini_separador()
                print(f"Documento: {doc_camper}")
                for clave, valor in datos_camper.items():
                    print(f" - {clave.capitalize()}: {valor}")

def camper_crearNotas(doc, ruta):
    
    # Se cargan los datos desde el JSON 
    notas = dataOpciones.cargar_datos("data/notas.json")

    # Se crean los módulos predefinidos 
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
    # Se crea un diccionario con el documento del camper, la ruta a la que pertenece el camper y los módulos predefinidos
    notas[doc] = {
        "ruta": ruta,
        "modulos": modulos
    }

    # Se guardan las notas en el JSON 
    dataOpciones.guardar_datos("data/notas.json", notas)

def crear_camper(): 
    # Se cargan los datos desde el JSON 
    campers = dataOpciones.cargar_datos("data/campers.json")
    # Se crea un diccionario donde se guardara el camper
    camper = {} 
    # Se verifica que el camper no este registrado 
    while True:
        doc = input("Ingrese el documento del nuevo camper: ").strip()
        if doc in campers:
            print("¡El documento ya está registrado!")
        elif doc =="":
            print("Debe ingresar un numero de documento")
        else:
            break
    
    # Se piden los datos del camper. Se verifica que el usuario no entregue los datos vacios
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

    # Se crea el diccionario campers con las variables que obtuvimos del usuario
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
    # Se guarda en campers el camper creado asociado a su documento
    campers[doc] = camper
    # Se guardan los datos en el JSON 
    dataOpciones.guardar_datos("data/campers.json", campers)
    
    print("¡Nuevo camper agregado exitosamente!")

def actualizar_camper(): 
    # Se cargan los datos desde el JSON 
    campers = dataOpciones.cargar_datos("data/campers.json")
    # Se solicita el documento del camper 
    doc = input("Ingrese el documento del camper: ").strip()
    # Verifica que el camper se encuentre registrado
    if doc not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return
    # Si el camper esta registrado, se muestran sus datos 
    print("Datos actuales del camper:")
    for clave, valor in campers[doc].items():
        if clave not in ["pruebaIngreso", "estado", "riesgo"]: 
            print(f"{clave.capitalize()}: {valor}")
    # Se solicita seleccionar el campo que se desea actualizar, no se pueden actualizar los datos en la prueba de ingreso, estado ni riesgo, ya que estos se manejan en otras funciones
    campo_actualizar = input("Ingrese el campo que desea actualizar: ").strip().lower()
    if campo_actualizar not in campers[doc] or campo_actualizar in ["pruebaingreso", "estado", "riesgo"]:
        print("El campo ingresado no existe.")
        return
    # Se le solicita el nuevo valor que tendra el campo seleccionado
    nuevo_valor = input(f"Ingrese el nuevo valor para '{campo_actualizar.capitalize()}': ").strip()
    campers[doc][campo_actualizar] = nuevo_valor
    # Se guardan los cambios en el JSON 
    dataOpciones.guardar_datos("data/campers.json", campers)

def cambiar_estado():
    # Se cargan los datos desde el JSON 
    campers = dataOpciones.cargar_datos("data/campers.json")
    # Se solicita el documento del camper y se verifica que exista
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return
    # Si el camper esta registrado se muestra el estado actual, y las opciones a las que se puede cambiar el estado, las opciones de estado 'Inscrito', 'Cursando' y 'Aprobado', se asignan automaticamente en otras funciones
    print(f"Estado actual del camper: {campers[doc]['estado']}")
    print("Opciones de estado: Graduado, Expulsado, Retirado")
    # Se verifica que el estado seleccionado sea de los que estan disponibles en las opciones
    while True:
        nuevo_estado = input("Ingrese el nuevo estado del camper: ").strip().capitalize()
        if nuevo_estado not in ["Graduado", "Expulsado", "Retirado"]:
            print("El estado ingresado no es válido. Por favor, ingrese un estado válido (Graduado, Expulsado, Retirado).")
        else:
            break
    # Se le asigna el nuevo estado al camper
    campers[doc]["estado"] = nuevo_estado
    # Se guardan los datos en el JSON
    dataOpciones.guardar_datos("data/campers.json", campers)
    print("Estado del camper actualizado correctamente.")

def notas_prueba_ingreso():
    # Se cargan los datos desde el JSON 
    campers = dataOpciones.cargar_datos("data/campers.json")
    # Se solicita el documento del camper y se verifica que exista
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return
    # Por medio de la llave 'promedio' verifica si ya se han ingresado las notas de la prueba de ingreso
    if campers[doc]["pruebaIngreso"]["promedio"] != 0:
        print("Las notas de la prueba de ingreso ya han sido ingresadas.")
        return
    # En caso de no haber sido ingresadas las solicita, verificando que se ingrese un numero y que este este entre 0 y 100
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
    # Se calculo el promedio con las notas y se le asigna al camper
    promedio = (nota_practica + nota_teorica) / 2
    campers[doc]["pruebaIngreso"]["nota_practica"] = nota_practica
    campers[doc]["pruebaIngreso"]["nota_teorica"] = nota_teorica
    campers[doc]["pruebaIngreso"]["promedio"] = promedio
    # Si el promedio de las notas es mayor o igual a 60 automaticamente el estado del camper pasa a 'Aprobado'
    if promedio >= 60:
        campers[doc]["estado"] = "Aprobado"
    # Se guardan los datos en el JSON 
    dataOpciones.guardar_datos("data/campers.json", campers)
    print("Notas de la prueba de ingreso ingresadas correctamente.")

def crear_advertencias(): 
    # Se cargan los datos desde el JSON 
    notas = dataOpciones.cargar_datos("data/notas.json")
    # Solicita el documento del camper y se verifica que este registrado
    doc_camper = input("Ingrese el documento del camper: ").strip()
    
    if doc_camper not in notas:
        print("¡El documento del camper no se encuentra registrado!")
        return
    # En caso de estar registrado, se muestra los modulos disponibles, para que eliga en donde poner la advertencia
    modulos_disponibles = list(notas[doc_camper]['modulos'].keys()) # Lista con las llaves de 'modulos'
    print("Módulos disponibles:")
    for idx, modulo in enumerate(modulos_disponibles, start=1): # Recorre la lista de modulos_disponibles
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