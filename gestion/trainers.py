import data.datos as dataOpciones
import menu.opciones as menuOpciones

def mostrar_trainers(): 
    # Se cargan los datos desde el JSON
    trainers = dataOpciones.cargar_datos("data/trainers.json")

    print("Trainers disponibles:")

    # Recorrer trainers e ir mostrandolos
    for doc, info_trainer in trainers.items():
        print(f"Documento: {doc}")
        print(f"Nombre: {info_trainer['nombres']} {info_trainer['apellidos']}")
        print("Horarios disponibles:")
        for horario, disponibilidad in info_trainer['horario_disponible'].items():
            print(f"- {horario}: {disponibilidad}")
        menuOpciones.mini_separador()

def mostrarInformacion_trainer(doc): 
    trainers = dataOpciones.cargar_datos("data/trainers.json")

    if doc in trainers:
        trainer_info = trainers[doc]
        print("Información del trainer:")
        print(f"Documento: {doc}")
        print(f"Nombre: {trainer_info['nombres']} {trainer_info['apellidos']}")
        print("Horarios: ")
        for horario, disponibilidad in trainer_info['horario_disponible'].items():
            print(f"- {horario}: {disponibilidad}")

def verRutas_trainers(doc): 
    rutas = dataOpciones.cargar_datos("data/rutas.json")

    print("Grupos asignados al trainer:")
    for ruta, info_ruta in rutas.items():
        grupos = info_ruta.get('grupos', {})
        for grupo, info_grupo in grupos.items():
            if info_grupo['trainer_id'] == doc:
                print(f"Ruta: {ruta}, Grupo: {grupo}")
                print(f"  Horario: {info_grupo.get('horario', 'No asignado')}")
                print(f"  Salón: {info_grupo.get('salon', 'No asignado')}")
                menuOpciones.mini_separador()

def verificar_pertenencia_camper(doc_trainer, doc_camper):
    rutas = dataOpciones.cargar_datos("data/rutas.json")

    for ruta, info_ruta in rutas.items():
        grupos = info_ruta.get("grupos", {})
        for grupo, info_grupo in grupos.items():
            if info_grupo.get("trainer_id") == doc_trainer and doc_camper in info_grupo.get("campers_ids", []):
                return True
    return False

def ingresarNotas_camper(doc): 
    # Cargar los datos desde el JSON 
    notas = dataOpciones.cargar_datos("data/notas.json")
    campers = dataOpciones.cargar_datos("data/campers.json")

    # Pedir el documento del camper al que se le quieren poner notas
    doc_camper = input("Ingrese el documento del camper: ").strip()

    # Verificación de si el camper pertenece a un grupo del trainer
    verificacion = verificar_pertenencia_camper(doc, doc_camper)
    if verificacion == True: 
        # Obtener las notas del camper
        camper_notas = notas[doc_camper]

    # Mostrar los módulos disponibles para ingresar notas
        modulos_disponibles = list(camper_notas['modulos'].keys())
        print("Módulos disponibles para ingresar notas:")
        for num, modulo in enumerate(modulos_disponibles, 1):
            print(f"{num}. {modulo}")

        while True:
            try:
                opcion = int(input("Seleccione el número del módulo para ingresar notas: "))
                if 1 <= opcion <= len(modulos_disponibles):
                    break
                else:
                    print("Número de módulo fuera de rango. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        modulo_seleccionado = modulos_disponibles[opcion - 1]

        # Se piden las notas al trainer
        while True:
            try:
                quices_trabajos = float(input("Ingrese la nota de quices y trabajos (0-100): ").strip())
                if 0 <= quices_trabajos <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        while True:
            try:
                prueba_teorica = float(input("Ingrese la nota de la prueba teórica (0-100): ").strip())
                if 0 <= prueba_teorica <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        while True:
            try:
                prueba_practica = float(input("Ingrese la nota de la prueba práctica (0-100): ").strip())
                if 0 <= prueba_practica <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")

        # Se calcula el promedio y se cambia el estado
        promedio = (quices_trabajos * 0.1) + (prueba_teorica * 0.3) + (prueba_practica * 0.6)
        if promedio >= 60:
            estado = "Aprobado"
        else: 
            estado = "No aprobado"
            campers[doc_camper]["riesgo"] = "Alto"
            
            

        # Actualizar las notas del camper
        camper_notas['modulos'][modulo_seleccionado] = {
            "quices_trabajos": quices_trabajos,
            "prueba_teorica": prueba_teorica,
            "prueba_practica": prueba_practica,
            "promedio": promedio,
            "estado": estado,
            "advertencias": []
        }

        # Guardar los cambios en el archivo JSON
        dataOpciones.guardar_datos("data/notas.json", notas)
        dataOpciones.guardar_datos("data/campers.json", campers)

        print("Notas ingresadas exitosamente.")
    else: 
        print("El camper no pertenece a ninguno de tus grupos.")

   