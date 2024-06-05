import data.datos as dataOpciones
def mostrar_campers(estado = None): 
    campers = datos.cargar_datos("data\campers.json")
    if campers: 
        print(f"Lista de campers con estado: {estado if estado else "Registrado"}:")
        for doc_camper, datos_camper in campers.items(): 
            if not estado or datos_camper.get("estado") == estado:
                opciones_menu.mini_separador()
                print(f"Documento: {doc_camper}")
                for clave, valor in datos_camper.items():
                    print(f" - {clave.capitalize()}: {valor}")
    else: 
        print("No hay campers registrados")