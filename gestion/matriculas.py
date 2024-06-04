import data.datos as dataOpciones

def asignarCamper_ruta():
    campers = dataOpciones.cargar_datos("data/campers.json")
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    
    doc_camper = input("Ingrese el documento del camper: ").strip()
    
    if doc_camper not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return

    if campers[doc_camper]['estado'] != 'Aprobado':
        print("El camper debe tener en su estado aprobado, para ser asignado a una ruta.")
        return
    
    print("Rutas disponibles:")
    for idx, ruta in enumerate(rutas.keys(), 1):
        print(f"{idx}. {ruta}")
    
    while True:
        try:
            ruta_idx = int(input("Seleccione una ruta (número): ")) - 1
            if ruta_idx < 0 or ruta_idx >= len(rutas):
                raise IndexError("El número seleccionado no corresponde a ninguna ruta.")
            ruta_seleccionada = list(rutas.keys())[ruta_idx]
            break
        except ValueError:
            print("Debe ingresar un número válido.")
        except IndexError as ie:
            print(f"Error: {ie}")
    
    grupos_disponibles = {grupo: datos for grupo, datos in rutas[ruta_seleccionada]['grupos'].items() if datos['cantidad_campers'] < 33}
    
    if not grupos_disponibles:
        print(f"Todos los cursos de la {ruta_seleccionada} están llenos.")
        return
    
    print(f"Grupos disponibles en {ruta_seleccionada}:")
    for grupo, datos in grupos_disponibles.items():
        print(f"{grupo} - {datos['cantidad_campers']} inscritos")
    
    while True:
        grupo_seleccionado = input("Ingrese el grupo en el que desea inscribir al camper: ").strip().capitalize()
        if grupo_seleccionado in grupos_disponibles:
            break
        else:
            print("El grupo seleccionado no es válido. Ingrese nuevamente el grupo.")

    rutas[ruta_seleccionada]['grupos'][grupo_seleccionado]['campers_ids'].append(doc_camper)
    rutas[ruta_seleccionada]['grupos'][grupo_seleccionado]['cantidad_campers'] += 1
    campers[doc_camper]['estado'] = 'Cursando'
    
    dataOpciones.guardar_datos("data/rutas.json", rutas)
    dataOpciones.guardar_datos("data/campers.json", campers)
    
    print(f"El camper {doc_camper} ha sido asignado correctamente a {ruta_seleccionada}, grupo {grupo_seleccionado}.")