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