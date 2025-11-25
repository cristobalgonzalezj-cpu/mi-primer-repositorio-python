MAYOR_EDAD = 18

edad = input("ingrese su edad:,")

if int(edad) > MAYOR_EDAD:
    print("eres mayor de edad")

elif int(edad) == MAYOR_EDAD:
    print("eres mayor de edad, tienes exactamente 18 años18")

if int(edad) < MAYOR_EDAD:
    print("eres menor de edad")