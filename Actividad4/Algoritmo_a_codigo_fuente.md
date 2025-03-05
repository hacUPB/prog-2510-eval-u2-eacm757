## Ejercicio 1
    Pseudocodigo:
    Inicio 
    Escribir "Punto en X1:"
    Escribir "Punto en X2:"
    Leer X1, X2
    Escribir "Punto en Y1:"
    Escribir "Punto en Y2:"
    Leer Y1, Y2
    Distancia = ((X2 - X1)^2 + (Y2 - Y1)^2)^1/2
    Imprimir Distacia 
    Fin 

    Codigo py:
    X1 = float(input("Ingrese coordenada X de P1: "))
    Y1 = float(input("Ingrese coordenada Y de P1: "))
    X2 = float(input("Ingrese coordenada X de P2: "))
    Y2 = float(input("Ingrese coordenada Y de P2: "))
    D = (((X2 - X1)**2 + (Y2 - Y1)**2)**0.5)
    print (f"La distancia es: {D}")

## Ejercicio 2
    Pseudocodigo:
    Inicio
    Escribir "Metros" 
    Leer metros 
    Pulgadas = Metros/0.0254m
    Imprimir Pulgadas 
    Fin 

    Codigo py:
    Metros = float(input("Ingrese los metros: "))
    Pulgadas = Metros/0.0254
    print (f"Los metros en pulgadas son: {Pulgadas:.2f}")

## Ejercicio 3
    Pseudocodigo:
    Inicio
    Escribir "A"
    Escribir "B" 
    Leer A, B
    C = (A^2 + B^2)^1/2
    Imprimir C
    Fin 


    Codigo py:
    A = float(input("Lado del cateto 1: "))
    B = float(input("Lado del cateto 2: "))
    Hipotenusa = (A**2 + B**2)**0.5
    print (f"La hipotenusa es: {Hipotenusa:.2f}")

## Ejercicio 4 
    Pseudocodigo:
    Inicio 
    Escribir "Ingrese la fecha de nacimiento: (Dia/Mes/Año)"
    Escribir "Fecha actual:(Dia/Mes/Año)"

    Leer DAC, MAC, AAC, DCU, MCU, ACU

    Edad = AAC - ACU 
    Si MAC < MCU
        Edad =Edad - 1
    Sino Si MAC = MCU
        Si DAC < DCU
        Edad = Edad - 1
        Sino Si DAC = DCU 
        Imprimir "Feliz cumpleaños"
        Sino
            Imprimir "Ya has cumplido años este año"
        Fin si
    Sino
        Imprimir "Ya has cumplido años este año"
    Fin si
    Imprimir "Tu edad es:", Edad 
    Fin 
    

    Codigo py:
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

## Ejercicio 5
    Pseudocodigo:
    Inicio 
    Escribir "Numero de horas trabajadas"
    Escribir "Pago Por Hora"
    Leer NoHoras, PagoxHora
    Si NoHoras > 50
        Escribir "No está permitido"
        Aumento = PagoxHora * 3
    Sino Si Nohoras >= 46
        Aumento = PagoxHora * 3
        Sino Si NoHoras >= 41
            Aumento = PagoxHora * 2
            Sino 
            Aumento = PagoxHora 
        Fin si   
    Fin si
    Si NoHoras <= 50
        Imprimir  Sueldo = Nohoras * Aumento 
        Escribir "Su sueldo semanal es:"
    Fin si
    Fin 



    Codigo py:
    NoHoras = float(input("Ingrese el numero de horas trabajadas: "))
    PagoxHora = float(input("Ingrese el pago por hora: "))

    if NoHoras > 50: 
    print ("No esta permitido trabajar mas de 50 horas")
    elif NoHoras >= 46: 
        Aumento = PagoxHora * 3 
    elif NoHoras >= 41: 
        Aumento = PagoxHora * 2 
    else :
        Aumento = PagoxHora 

    if NoHoras < 50:   
        Sueldo = (NoHoras * Aumento)
    print (f"Su sueldo semanal: {Sueldo}")
    print ("Esta mal pq se calcula todo como horas dobles y triples")









