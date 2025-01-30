"""
    Ejemplo de uso del ciclo while

while condicion-lógica:
    // instrucción
    // instrucción
    // instrucción
    // instrucción

"""
# Declaración de variables
numero = 1   # Contador: controla el número hasta donde debe ejecutarse el bucle
suma = 0     # Acumulador: almacena la suma total de los números
promedio = 0 # Variable para calcular el promedio

# Proceso para calcular la suma usando un ciclo While
while numero <= 10:  # El bucle se ejecuta mientras numero sea menor o igual a 10
    suma = suma + numero   # Se acumula el valor actual en la variable suma
    numero = numero + 1    # Se incrementa el contador en 1 para avanzar al siguiente número

# Calcular el promedio
promedio = suma / 10  # Se divide la suma total entre 10

# Presentar los resultados
print("La suma de los números del 1 al 10 es: %d" % suma)
print("El promedio de los números del 1 al 10 es: %.2f" % promedio)
