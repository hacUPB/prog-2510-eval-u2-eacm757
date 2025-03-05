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




 