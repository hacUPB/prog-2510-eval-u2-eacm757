## Problemas 

1. Se requiere obtener la distancia entre dos puntos en el plano cartesiano,
tal y como se muestra en la figura 1. Realice un diagrama de flujo y pseudocódigo
que representen el algoritmo para obtener la distancia entre
esos puntos.

![alt text](Images/SS1.png)

__Analisís:__ 

    Variables de entrada: X1, X2, Y1, Y2
    Variables de salida: Distancia
    Constantes: N/A 
    Operaciones: Distancia = ((X2 - X1)^2 + (Y2 - Y1)^2)^1/2

![alt text](Images/Diagrama1.png)

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


2. Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero.
Para cada pedido, tiene que proporcionar las medidas de la tela
en pulgadas, pero ella generalmente las tiene en metros. Realice un algoritmo
para ayudar a resolver el problema, determinando cuántas pulgadas
debe pedir con base en los metros que requiere. Represéntelo mediante un
diagrama de flujo y pseudocódigo (1 pulgada = 0.0254 m).

__Analisís:__ 

    Variables de entrada: Metros 
    Variables de salida: Pulgadas
    Constantes: 0.0254m
    Operaciones: Pulgadas = Metros/0.0254m

![alt text](Images/Diagrama2.png)

    Inicio
    Escribir "Metros" 
    Leer metros 
    Pulgadas = Metros/0.0254m
    Imprimir Pulgadas 
    Fin 


3. Se requiere determinar la hipotenusa de un triángulo rectángulo. ¿Cómo sería el diagrama de flujo y el pseudocódigo que representen el algoritmo para obtenerla? 
Recuerde que por Pitágoras se tiene que: $C^2 = A^2 + B^2$.

__Analisís:__ 

    Variables de entrada: A, B
    Variables de salida: C
    Constantes: N/A 
    Operaciones: C^2 = A^2 + B^2 

![alt text](Images/Diagrama3.png)

    Inicio
    Escribir "A"
    Escribir "B" 
    Leer A, B
    C = (A^2 + B^2)^1/2
    Imprimir C
    Fin 

4. __Se requiere determinar la edad actual de una persona basándose en su fecha de nacimiento. Además, es necesario establecer si la persona ya ha cumplido años en el año en curso, si aún no lo ha hecho, o si hoy es su cumpleaños, para celebrarlo. La fecha de nacimiento y la fecha actual estarán representadas mediante tres variables: día, mes y año.__
    
    **Instrucciones:**
    
    - Diseñe un algoritmo que permita calcular la edad de la persona.
    - Dentro de la solución, determine si la persona ya celebró su cumpleaños este año o si aún no lo ha hecho.
    - Verifique si la fecha actual corresponde al día de su cumpleaños. De ser así, imprima el mensaje “Feliz Cumpleaños”.
    - Represente la solución utilizando **pseudocódigo** claro y estructurado.


5. Realice un algoritmo que permita determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora, considerando que a partir de la hora número 41 y hasta la 45, cada hora se le paga el doble, de la hora 46 a la 50, el triple, y que trabajar
más de 50 horas no está permitido. Represente el algoritmo mediante pseudocódigo.

__Analisís:__ 

    Variables de entrada: Horas
    Variables de salida: Sueldo, Pago por hora
    Constantes: N/A 
    Operaciones: 

![alt text](Images/Diagrama4.png)       

    Inicio 
    Escribir "Numero de horas"
    Leer NoHoras 
    PagoxHora = PagoxHora
    Si NoHoras > 50
        Escribir "No está permitido"
        Sueldo_Semanal = NoHoras * Aumento 

    Sino 
    Fin 


6. __Se requiere un algoritmo para determinar, de N cantidades, cuántas son cero, cuántas son menores a cero, y cuántas son mayores a cero. Realice el pseudocódigo para representarlo, utilizando el ciclo apropiado.__


7. __Se requiere un algoritmo para determinar cuánto ahorrará en pesos una persona diariamente, y en un año, si ahorra 3¢ el primero de enero, 9¢ el dos de enero, 27¢ el 3 de enero y así sucesivamente todo el año. Represente la solución mediante pseudocódigo.__


8. Realice el algoritmo para determinar cuánto pagará una persona que adquiere N artículos, los cuales están de promoción. Considere que si su precio es mayor o igual a $200 se le aplica un descuento de 15%, y si su precio es mayor a $100, pero menor a $200, el descuento es de
12%; de lo contrario, solo se le aplica 10%. Se debe saber cuál es el costo y el descuento que tendrá cada uno de los artículos y finalmente cuánto se pagará por todos los artículos obtenidos. Represente la solución mediante pseudocódigo.





