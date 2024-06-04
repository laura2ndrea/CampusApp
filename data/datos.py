import json 

def cargar_datos(nombre_archivo): 
    try: 
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            print ("Datos cargados exitosamente")
            return json.load(file)
    except Exception as e: 
        print(f"Error al cargar los datos {e}")


def guardar_datos(nombre_archivo, data): 
    try: 
        with open (nombre_archivo, "w", encoding="utf-8") as file: 
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e: 
        print(f"Error al guardar los datos: {e}")