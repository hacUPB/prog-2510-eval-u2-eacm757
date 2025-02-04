## 1.¿Qué es un computador?
Un computador es una máquina capaz de procesar información de manera automática. Está diseñado para realizar operaciones lógicas, almacenar datos y ejecutar programas o instrucciones para llevar a cabo tareas específicas. Un computador consta de componentes de hardware y software, trabajando de manera conjunta.

Referencia Bibliográfica:
["Computación, Arquitectura de Computadores", de William Stallings. Pearson Educación](http://biblioteca.univalle.edu.ni/files/original/c1b1f5d1c12abc60a246e2a0d784f7c9d163ee81.pdf)

## 2.Arquitecturas de un computador 
La arquitectura de un computador es la estructura y diseño de sus componentes principales, que incluyen tanto el hardware como los circuitos necesarios para su funcionamiento. Determina cómo los componentes interactúan entre sí y cómo los programas pueden aprovechar estos recursos para ejecutar instrucciones.

###  2.1 Arquitectura CISC (Complex Instruction Set Computer)
En esta arquitectura, la CPU tiene un conjunto amplio y complejo de instrucciones. Esto permite que la CPU ejecute operaciones complejas en una sola instrucción, lo que puede simplificar el diseño del software, pero al mismo tiempo aumenta la complejidad del hardware.

__Ejemplos de equipos modernos:__

Procesadores Intel x86
AMD Ryzen
2.2 Arquitectura RISC (Reduced Instruction Set Computer)
En esta arquitectura, la CPU tiene un conjunto reducido de instrucciones, lo que simplifica el diseño de la CPU. Las instrucciones son más simples y se ejecutan en menos ciclos de reloj, lo que mejora la eficiencia y velocidad en algunos casos.

__Ejemplos de equipos modernos:__

Procesadores ARM (utilizados en dispositivos móviles y sistemas embebidos)
Apple M1 
3. ## ¿Qué es el hardware?
El hardware es la parte física de un computador, que incluye todos los componentes y dispositivos que realizan el procesamiento de datos y permiten la interacción con el usuario.

### 3.1 CPU (Unidad Central de Procesamiento)
La CPU es el cerebro del computador, encargada de ejecutar las instrucciones de los programas. Está formada por varias partes esenciales:

ALU (Unidad Aritmético Lógica): Realiza operaciones matemáticas y lógicas.
Unidad de Control: Dirige la ejecución de las instrucciones y coordina las demás unidades del computador.
Registros: Memoria pequeña y rápida que guarda datos temporales y resultados intermedios de operaciones.
Buses: Canales de comunicación que permiten el traslado de datos entre los distintos componentes del sistema.

### 3.2 GPU (Unidad de Procesamiento Gráfico)
La GPU es un procesador especializado en la manipulación y la creación de imágenes, gráficos y vídeos. Se utiliza principalmente en tareas de renderizado gráfico, pero también se usa para procesamiento paralelo en aplicaciones científicas y de inteligencia artificial.

Comparación con la CPU:

CPU: Optimizada para ejecutar una serie de instrucciones de manera secuencial. Su arquitectura es adecuada para tareas generales.
GPU: Optimizada para ejecutar tareas paralelas masivas y repetitivas, como la generación de gráficos. Su arquitectura se basa en múltiples núcleos más pequeños que permiten realizar muchos cálculos simultáneamente.
3.3 Memoria
Registros: Memoria extremadamente rápida en la CPU, utilizada para almacenar valores intermedios.
Caché: Memoria más rápida que la RAM, situada cerca de la CPU, que guarda datos de acceso frecuente para acelerar la ejecución de programas.
Memoria Principal (RAM): Memoria volátil de acceso rápido que almacena datos temporales mientras el computador está encendido.
Memoria Secundaria (Disco Duro y Unidades Externas de Almacenamiento): Almacena datos permanentemente, incluso cuando el computador está apagado.
3.4 Dispositivos de Entrada/Salida
Estos son los periféricos que permiten al usuario interactuar con el computador:

Entrada: Teclado, ratón, micrófono, cámara.
Salida: Monitor, impresora, altavoces.
3.5 Buses de Datos
Son sistemas de comunicación dentro del computador que transportan información entre diferentes componentes, como la CPU, la memoria y los dispositivos de entrada/salida.

## 4. ¿Qué es el software?
El software es el conjunto de instrucciones y programas que le indican al hardware qué hacer. Se clasifica en diferentes tipos:

### 4.1 Software de Sistema
Es el conjunto de programas que gestionan el hardware y permiten la ejecución de otros programas. Ejemplo: el sistema operativo (Windows, Linux, macOS).

### 4.2 Software de Aplicación
Son programas diseñados para realizar tareas específicas, como procesadores de texto, hojas de cálculo, navegadores web, etc.

### 4.3 Software de Desarrollo
Son herramientas que permiten a los desarrolladores escribir, probar y mantener otros programas. Ejemplo: compiladores, editores de código, entornos de desarrollo integrados (IDE).

## 5. Funcionamiento del computador

### 5.1 ¿Qué procesos se llevan a cabo cuando se enciende una computadora?
Al encender el computador, el proceso de arranque es llamado POST (Power-On Self Test), que verifica el hardware básico. Luego, el BIOS/UEFI busca un sistema operativo en la memoria secundaria y lo carga en la memoria RAM.

### 5.2 ¿Qué sucede desde que ingreso un dato a través del teclado, hasta que veo el resultado de la operación en la pantalla?
Cuando ingresas un dato a través del teclado, el proceso es el siguiente:

El teclado envía señales eléctricas a la CPU.
La CPU procesa los datos e interpreta las instrucciones del sistema operativo.
El resultado se almacena en la memoria RAM o se muestra en la pantalla a través de la GPU.
### 5.3 ¿Cómo se codifican los datos internamente en el computador?
Los datos se codifican en forma de bits (0s y 1s) dentro de la memoria. Todo tipo de datos (texto, imágenes, audio) se convierten a secuencias de bits mediante un sistema de codificación, como ASCII o Unicode para texto.

### 5.4 ¿Cuáles son las unidades de medida de datos en un computador?
Las unidades más comunes de medida de datos son:

Bit (b): Unidad más pequeña de información (0 o 1).
Byte (B): 8 bits.
Kilobyte (KB): 1,024 bytes.
Megabyte (MB): 1,024 KB.
Gigabyte (GB): 1,024 MB.
Terabyte (TB): 1,024 GB.
