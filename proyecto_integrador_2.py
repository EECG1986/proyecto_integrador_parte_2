# Importar las funciones readkey y key del módulo readchar

from readchar import readkey, key

# Pedir al usuario que presione una tecla y explicar cómo detener el programa

print(input("Por favor presione una tecla y para detener presione flecha 🡩 ")) 

# Inicia un bucle infinito

while True:
    # Leer la tecla presionada por el usuario
    
    k = readkey()

    # Verificar si la tecla presionada es la flecha hacia arriba
    
    if k == key.UP:
        
        # Si es así, imprimir un mensaje y romper el bucle para terminar el programa
        
        print("Oh!! haz presionado 🡩  para detener ")
        break
    else:
        # Si se presiona cualquier otra tecla, mostrar qué tecla fue
    
        print(f"Presionaste {k}")
