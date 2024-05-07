def calcular(opcion):
    if opcion in ("1", "2", "3", "4", "5", "7", "8", "9", "10"):
        val1 = float(input("Ingrese el primer valor: "))
    if opcion in ("1", "2", "3", "4", "5", "7", "8", "9", "10"):
        val2 = float(input("Ingrese el segundo valor: "))

    if opcion == "1":
        velocidad(val1, val2)
    elif opcion == "2":
        distancia(val1, val2)
    elif opcion == "3":
        tiempo(val1, val2)
    elif opcion == "4":
        vol_cubo(val1)
    elif opcion == "5":
        fuerza(val1, val2)
    elif opcion == "6":
        val2 = float(input("Ingrese el segundo lado: "))
        area(val1, val2)
    elif opcion == "7":
        trabajo(val1, val2)
    elif opcion == "8":
        val3 = float(input("Ingrese el tercer valor: "))
        velf(val1, val2, val3)
    elif opcion == "9":
        val3 = float(input("Ingrese el tercer valor: "))
        velin(val1, val2, val3)
    elif opcion == "10":
        val3 = float(input("Ingrese el tercer valor: "))
        aceleracion(val1, val2, val3)
    elif opcion == "fin":
        print("!Hasta luego¡")
    else:
        print("ERROR")

def velocidad(x, t):
    result = x / t
    print("La velocidad es", str(result))

def distancia(v, t):
    result = v * t
    print("La distancia es", str(result))

def tiempo(x, v):
    result = x / v
    print("El tiempo es", str(result))

def vol_cubo(lado):
    result = lado ** 3
    print("El volumen es", str(result))

def fuerza(m, a):
    result = m * a
    print("La fuerza es", str(result))

def area(lado1, lado2):
    result = lado1 * lado2
    print("El area es", str(result))

def trabajo(f, desplazamiento):
    result = f * desplazamiento
    print("El trabajo es", str(result))

def velf(vo, a, t):
    result = vo + a * t
    print("La velocidad final es", str(result))

def velin(vf, a, t):
    result = vf - a * t
    print("La velocidad inicial es", str(result))

def aceleracion(vf, vo, t):
    result = (vf - vo) / t
    print("La aceleración es", str(result))

while True:
    print("Seleccione el tipo de conversión:")
    print("1 = Velocidad")
    print("2 = Distancia")
    print("3 = Tiempo")
    print("4 = Volumen del cubo")
    print("5 = Fuerza")
    print("6 = Área")
    print("7 = Trabajo")
    print("8 = Velocidad final")
    print("9 = Velocidad inicial")
    print("10 = Aceleración")
    print("fin = Salir")

    opcion = input("Ingrese la opción que desea llevar a cabo: ")

    if opcion == "fin":
        calcular(opcion)
        break
    elif opcion in ("1", "2", "3", "4", "5", "7", "8", "9", "10"):
        calcular(opcion)
    else:
        print("ERROR")