print("Este programa cuenta con 4 funciones para calcular al ingresar 5 numeros")
print("Opcion 1 - Sumar \nOpcion 2 - Sacar promedio\nOpcion 3 - Sacar el Maximo de un numero \nOpcion 4 - Sacar el minimo de un numero")
opcion = int(input("Ingrese la opcion que desea utilizar (1,2,3 o 4): "))
if opcion == 1:
    print("Usted eligio la Opcion 1 - Sumar")
    list = []
    result = 0
    suma = 0
    for i in range(5):
        num = int(input("Ingrese un numero"))
        list.append(num)
    for number in list:
        result += number
    print(f"El resultado de la suma es: {result}")
if opcion == 2:
    print("Usted eligio la Opcion 2 - Sacar promedio")
    list = []
    result = 0
    for i in range(5):
        num = int(input("Ingrese un numero: "))
        list.append(num)
    for number in list:
        suma += number
        promedio = suma / len(list)
    print(f"El promedio de los numeros ingresados es: {promedio}")
if opcion == 3:
    print("Usted eligio la Opcion 3 - Sacar el Maximo de un numero")
    list = []
    result = 0
    for i in range(5):
        num = int(input("Ingrese un numero: "))
        list.append(num)
    for number in list:
        result = max(list)
    print(f"El valor maximo de los numeros ingresados es: {result}")
if opcion == 4:
    print("Usted eligio la Opcion 4 - Sacar el minimo de un numero")
    list = []
    result = 0
    for i in range(5):
        num = int(input("Ingrese un numero: "))
        list.append(num)
    for number in list:
        result = min(list)
    print(f"El valor minimo de los numeros ingresados es: {result}")

print("Gracias por utilizar el programa!")
print("Participantes:\n-Alejandro Antonio Leyton Segovia(Aula 5)\n-William Bernardo Leyton Segovia(Aula 4) ")




