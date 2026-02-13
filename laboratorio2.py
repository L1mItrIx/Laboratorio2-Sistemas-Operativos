"""
Laboratorio #2 - Sistemas Operativos
Universidad Internacional de las Américas


Eugene Li Liang
"""

import threading


contador = 0  # Variable compartida entre hilos
#Parte a: Crear una sección crítica que incremente un contador global 100,000 veces por cada hilo
def seccion_critica():
    global contador
    for _ in range(100000):
        contador += 1

#Parte b: Crear al menos 2 hilos que ejecuten la sección crítica y esperar a que terminen
def ejecutar_una_vez():
    global contador
    contador = 0  # Reiniciar contador para cada ejecucion
    hilo1 = threading.Thread(target=seccion_critica)
    hilo2 = threading.Thread(target=seccion_critica)
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()
    return contador

# Parte c: Ejecutar al menos 5 veces y revisar si el valor final del contador varía
valor_esperado = 200000  # 2 hilos × 100000 incrementos
print("Valor esperado:", valor_esperado)
for i in range(5):
    resultado = ejecutar_una_vez()
    print(f"Ejecución {i+1}: {resultado} (diferencia: {valor_esperado - resultado})")
