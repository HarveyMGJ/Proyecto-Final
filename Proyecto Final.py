# Grupo 3: Insertion Sort y Búsqueda Binaria
# Integrantes:
# - Harvey González
# - Carlos Acuña
# - Elías Flores

def insertion_sort(arr):
    # Ordena la lista usando el algoritmo Insertion Sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def proyecto_insertion_sort():
    print("\n--- Proyecto: Simulación de llegada de datos y ordenamiento en tiempo real ---")
    datos = []
    while True:
        entrada = input("Ingresa un dato numérico (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            datos.append(numero)
            datos = insertion_sort(datos)
            print("Lista ordenada actual:", datos)
        except ValueError:
            print("Por favor, ingresa un número válido o 'fin' para terminar.")
    print("Datos finales ordenados:", datos)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def proyecto_busqueda_binaria():
    print("\n--- Proyecto: Buscador de palabras en un diccionario digital ---")
    entrada = input("Ingresa palabras (separadas por espacio, sin importar el orden): ")
    palabras = entrada.strip().split()
    palabras = insertion_sort(palabras)  # Asegura que estén ordenadas alfabéticamente
    print("Diccionario ordenado:", palabras)
    busqueda = input("Ingresa la palabra a buscar: ")
    pos = binary_search(palabras, busqueda)
    if pos != -1:
        print(f"La palabra '{busqueda}' fue encontrada en la posición {pos} del diccionario.")
    else:
        print(f"La palabra '{busqueda}' no se encuentra en el diccionario.")

def menu():
    while True:
        print("\n=== Menú de proyectos ===")
        print("1. Simulación con Insertion Sort (datos en tiempo real)")
        print("2. Buscador con Búsqueda Binaria (diccionario digital)")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")
        if opcion == '1':
            proyecto_insertion_sort()
        elif opcion == '2':
            proyecto_busqueda_binaria()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    menu()
