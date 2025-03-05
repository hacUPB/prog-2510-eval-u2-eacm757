DAC = int(input("Ingrese el dia actual: "))
MAC = int(input("Ingrese el mes actual: "))
AAC = int(input("Ingrese el año actual: "))
print (f"La fecha actual es (Dia/Mes/Año): {DAC}/{MAC}/{AAC}")


DCU = int(input("Ingrese el dia de cumpleaños: "))
MCU = int(input("Ingrese el mes de cumpleaños: "))
ACU = int(input("Ingrese el año de cumpleaños: "))
print (f"La fecha de su cumpleaños (Dia/Mes/Año): {DCU}/{MCU}/{ACU}")

Edad = AAC - ACU
if MAC < MCU:
    Edad = Edad - 1
elif MAC == MCU:
    if DAC < DCU:
        Edad = Edad - 1 
    elif DAC == DCU:
        print ("Feliz Cumpleaños")
    else:
        print("ya has cumplido años este año")
else: 
    print ("Ya has cumplido años este año")
print (f"Su edad es: {Edad}")
