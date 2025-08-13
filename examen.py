"""
Calculadora básica en consola que permite al usuario realizar operaciones matemáticas
simples (suma, resta, multiplicación y división) entre dos números. El usuario puede 
elegir la operación deseada a través de un menú, y el programa continúa ejecutándose 
hasta que se elige la opción de salir. Incluye una función para limpiar la consola y 
otra para solicitar datos numéricos al usuario.

Realizado por: Brandon Chan 13/08/2025
"""

import os  #Importa el módulo 'os' para poder ejecutar comandos del sistema 

def limpiar_consola(): #Función para limpiar la consola
    if os.name == 'nt': #Verifica si el sistema operativo es Windows 
        os.system('cls') #Ejecuta el comando 'cls' para limpiar la consola


def DATOS(): #Función que solicita dos números al usuario y los devuelve como floats
    num1 = float(input("Ingrese un numero:")) #Solicita al usuario el primer número y lo convierte a float
    num2 = float(input("Ingrese otro numero:")) #Solicita al usuario el segundo número y lo convierte a float
    return num1, num2 #Devuelve ambos números como una tupla

def SUMA(): #Función que realiza una suma
    print("SUMA") #Muestra un encabezado indicando la operación
    num1, num2 = DATOS() #Llama a la función DATOS para obtener los dos números
    resultado = num1 + num2 #Realiza la suma

    print(f"\nRESULTADO: {num1} + {num2} = {resultado}") #Muestra el resultado de la operación
    input("Presione Enter para continuar...") #Pausa para que el usuario vea el resultado

def RESTA(): #Función que realiza una resta
    print("RESTA") #Muestra un encabezado indicando la operación.
    num1, num2 = DATOS() #Llama a la función DATOS para obtener los dos números
    resultado = num1 - num2 #Realiza la resta

    print(f"\nRESULTADO: {num1} - {num2} = {resultado}") #Muestra el resultado de la operación
    input("Presione Enter para continuar...") #Pausa para que el usuario vea el resultado

def MULTIPLICACION(): #Función que realiza una multiplicación
    print("MULTIPLICACION") #Muestra un encabezado indicando la operación
    num1, num2 = DATOS() #Llama a la función DATOS para obtener los dos números
    resultado = num1 * num2 #Realiza la multiplicación

    print(f"\nRESULTADO: {num1} * {num2} = {resultado}") #Muestra el resultado de la operación
    input("Presione Enter para continuar...") #Pausa para que el usuario vea el resultado

def DIVISION(): #Función que realiza una división
    print("DIVISION") #Muestra un encabezado indicando la operación
    num1, num2 = DATOS() #Llama a la función DATOS para obtener los dos números.
    resultado = num1 / num2 #Realiza la división.

    print(f"\nRESULTADO: {num1} / {num2} = {resultado}") #Muestra el resultado de la operación
    input("Presione Enter para continuar...") #Pausa para que el usuario vea el resultado

while True: #Bucle principal del programa que muestra el menú
    limpiar_consola() #Limpia la consola antes de mostrar el menú
    print("Seleccione una opcion:") #Muestra un mensaje al usuario
    print("1. SUMA") #Opción 1 del menú
    print("2. RESTA") #Opción 2 del menú.
    print("3. MULTIPLICACION") #Opción 3 del menú
    print("4. DIVISION") #Opción 4 del menú
    print("5. SALIR") #Opción para salir del programa
    opcion = input("Ingrese el numero de opcion deseada:") #Solicita la opción al usuario

    if opcion == '1': #Si elige 1
        SUMA() #Llama a la función de suma

    elif opcion == '2': #Si elige 2 
        RESTA() #Llama a la función de resta
    
    elif opcion == '3': #Si elige 3
        MULTIPLICACION() #Llama a la función de multiplicación

    elif opcion == '4': #Si elige 4 
        DIVISION() #Llama a la función de división

    elif opcion == '5': #Si elige 5
        print("\nSaliendo del sistema... ¡Hasta pronto!") #Muestra mensaje de salida
        break #Finaliza el bucle

    else: #Si se introduce una opción no válida 
        print("Opcion no valida.") #Muestra un mensaje de error