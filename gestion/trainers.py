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