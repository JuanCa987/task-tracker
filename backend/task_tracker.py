import json # Para leer y escribir archivos JSON
import os # Para crear y borrar archivos

TASKS_FILE = 'tasks.json'  # Archivo donde se almacenarán las tareas

# Función para cargar las tareas desde el archivo JSON
def load_tasks():
    if os.path.exists(TASKS_FILE):  # Si el archivo existe
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)  # Intenta cargar las tareas
        except (json.JSONDecodeError, ValueError):  # Si el archivo tiene datos corruptos
            print("El archivo de tareas está corrupto o vacío, se creará un nuevo archivo.")
            return []  # Retorna una lista vacía si hay un error
    return []  # Si no existe el archivo, retorna una lista vacía


# Función para guardar las tareas en el archivo JSON
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)  # Guarda las tareas en formato JSON

# Función para agregar una tarea
def add_task(description):
    if not description.strip():  # Verifica que la descripción no esté vacía
        print("La descripción de la tarea no puede estar vacía.")
        return

    tasks = load_tasks()  # Carga las tareas
    task = {'description': description, 'completed': False}  # Nueva tarea
    tasks.append(task)  # Agrega la tarea a la lista
    save_tasks(tasks)  # Guarda la lista de tareas actualizada
    print(f"Tarea '{description}' agregada.")


# Función para listar todas las tareas
def list_tasks():
    tasks = load_tasks()  # Carga las tareas
    if tasks:
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task['completed'] else "✘"
            print(f"{idx}. {task['description']} [{status}]")
    else:
        print("No tasks found. congrats!")

# Función para marcar una tarea como completada
def complete_task(task_number):
    tasks = load_tasks()  # Carga las tareas
    if 0 < task_number <= len(tasks):  # Verifica si el número de tarea es válido
        tasks[task_number - 1]['completed'] = True  # Marca la tarea como completada
        save_tasks(tasks)  # Guarda las tareas actualizadas
        print(f"Tarea {task_number} marcada como completada.")
    else:
        print("Número de tarea no válido. Asegúrate de que el número de tarea exista.")

# Función para eliminar una tarea
def delete_task(task_number):
    tasks = load_tasks()  # Carga las tareas
    if 0 < task_number <= len(tasks):  # Verifica si el número de tarea es válido
        removed_task = tasks.pop(task_number - 1)  # Elimina la tarea
        save_tasks(tasks)  # Guarda las tareas actualizadas
        print(f"Tarea '{removed_task['description']}' eliminada.")
    else:
        print("Número de tarea no válido. Asegúrate de que el número de tarea exista.")

#-------------------------------------------------------------------------------

"""Hacerlo iterativo con la terminal"""

def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        try:
            choice = int(input("Elige una opción (1/2/3/4/5): "))
        except ValueError:  # Si la entrada no es un número válido
            print("Por favor ingresa un número válido.")
            continue

        if choice == 1:
            description = input("Escribe la descripción de la tarea: ")
            add_task(description)
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            try:
                task_number = int(input("¿Qué tarea deseas marcar como completada? (Número de tarea): "))
                complete_task(task_number)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif choice == 4:
            try:
                task_number = int(input("¿Qué tarea deseas eliminar? (Número de tarea): "))
                delete_task(task_number)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif choice == 5:
            print("Adiós!")
            break
        else:
            print("Opción no válida, por favor elige 1, 2, 3, 4 o 5.")


if __name__ == "__main__": # Ejecutar la función main si el archivo se ejecuta directamente
    main()
