## Ejercicio 1
En el caso de 1 bit, hay 2 estados posibles (0 y 1). 

Con 2 bits, hay 4 combinaciones posibles (00, 01, 10, 11). 

Con 3 bits, se pueden representar 8 estados diferentes: 000, 001, 010, 011, 100, 101, 110 y 111

Siguiendo con esta secuencia, usando $n$ bits de información se pueden representar $2^{n}$ estados totales.

### Representación de datos en una computadora
Los datos en una computadora se representan mediante el sistema binario, compuesto por ceros y unos. Cada número, letra, imagen o sonido se traduce en combinaciones de estos valores. Por ejemplo las imágenes se almacenan en píxeles con códigos de color específicos. 

### ¿Cuáles son las unidades de almacenamiento de datos que se utilizan en computación? 
| Unidad        | Abreviatura | Equivalencia en bytes |
|--------------|------------|-------------------------|
| Byte         | B          | 1 byte      |
| KiloByte     | KB         | 1,024 bytes |
| MegaByte     | MB         | 1,024 KB    |
| GigaByte     | GB         | 1,024 MB    |
| TeraByte     | TB         | 1,024 GB    |
| PetaByte     | PB         | 1,024 TB    |
| ExaByte      | EB         | 1,024 PB    |
| ZettaByte    | ZB         | 1,024 EB    |
| YottaByte    | YB         | 1,024 ZB    |

### Importancia del trabajo de George Boole
El trabajo de George Boole fue fundamental en la informática, ya que desarrolló el álgebra booleana, que es la base de los sistemas de cómputo modernos. Su lógica binaria permite que los circuitos electrónicos realicen operaciones mediante puertas lógicas (AND, OR, NOT), facilitando el procesamiento de datos en computadoras y otros dispositivos digitales.
[Lea más sobre George Boole aquí](https://linguistica.gea.lat/la-importancia-del-algebra-booleana-en-la-era-digital/?utm_source=chatgpt.com)


## Actividad 2 - Convertir de Binario a Decimal 
| Binario       | Potencias de 2             | Decimal |
|--------------|---------------------------------------|---------|
| 1010101010₂  | 2¹ + 2³ + 2⁵ + 2⁷ + 2⁹ = 2 + 8 + 32 + 128 + 512  | 682₁₀  |
| 11111₂       | 2⁰ + 2¹ + 2² + 2³ + 2⁴ = 1 + 2 + 4 + 8 + 16  | 31₁₀  |
| 10000000₂    | 2⁷ = 128  | 128₁₀  |
| 100100100₂   | 2² + 2⁵ + 2⁸ = 4 + 32 + 256  | 292₁₀  |
| 111000₂      | 2³ + 2⁴ + 2⁵ = 8 + 16 + 32  | 56₁₀  |



  ## Actividad 3 - Concertir de Decimal a Binario

1. **127₁₀**  
   - 127 ÷ 2 = **63**, residuo **1**  
   - 63 ÷ 2 = **31**, residuo **1**  
   - 31 ÷ 2 = **15**, residuo **1**  
   - 15 ÷ 2 = **7**, residuo **1**  
   - 7 ÷ 2 = **3**, residuo **1**  
   - 3 ÷ 2 = **1**, residuo **1**  
   - 1 ÷ 2 = **0**, residuo **1**  
   - **127₁₀ = 1111111₂** 

2. **246₁₀**  
   - 246 ÷ 2 = **123**, residuo **0**  
   - 123 ÷ 2 = **61**, residuo **1**  
   - 61 ÷ 2 = **30**, residuo **1**  
   - 30 ÷ 2 = **15**, residuo **0**  
   - 15 ÷ 2 = **7**, residuo **1**  
   - 7 ÷ 2 = **3**, residuo **1**  
   - 3 ÷ 2 = **1**, residuo **1**  
   - 1 ÷ 2 = **0**, residuo **1**  
   - **246₁₀ = 11110110₂**  

3. **1025₁₀**  
   - 1025 ÷ 2 = **512**, residuo **1**  
   - 512 ÷ 2 = **256**, residuo **0**  
   - 256 ÷ 2 = **128**, residuo **0**  
   - 128 ÷ 2 = **64**, residuo **0**  
   - 64 ÷ 2 = **32**, residuo **0**  
   - 32 ÷ 2 = **16**, residuo **0**  
   - 16 ÷ 2 = **8**, residuo **0**  
   - 8 ÷ 2 = **4**, residuo **0**  
   - 4 ÷ 2 = **2**, residuo **0**  
   - 2 ÷ 2 = **1**, residuo **0**  
   - 1 ÷ 2 = **0**, residuo **1**  
   - **1025₁₀ = 10000000001₂**  

4. **354₁₀**  
   - 354 ÷ 2 = **177**, residuo **0**  
   - 177 ÷ 2 = **88**, residuo **1**  
   - 88 ÷ 2 = **44**, residuo **0**  
   - 44 ÷ 2 = **22**, residuo **0**  
   - 22 ÷ 2 = **11**, residuo **0**  
   - 11 ÷ 2 = **5**, residuo **1**  
   - 5 ÷ 2 = **2**, residuo **1**  
   - 2 ÷ 2 = **1**, residuo **0**  
   - 1 ÷ 2 = **0**, residuo **1**  
   - **354₁₀ = 101100010₂**  

5. **187₁₀**  
   - 187 ÷ 2 = **93**, residuo **1**  
   - 93 ÷ 2 = **46**, residuo **1**  
   - 46 ÷ 2 = **23**, residuo **0**  
   - 23 ÷ 2 = **11**, residuo **1**  
   - 11 ÷ 2 = **5**, residuo **1**  
   - 5 ÷ 2 = **2**, residuo **1**  
   - 2 ÷ 2 = **1**, residuo **0**  
   - 1 ÷ 2 = **0**, residuo **1**  
   - **187₁₀ = 10111011₂**  

## Diferentes tipos de datos que se utilizan en varios lenguajes de programación



| Características Principales | Enteros  | Punto Flotante | String   | Booleano  | Char |
|----------------------------|----------|---------------|----------|-----------|------|
| **Descripción**            | Son números sin parte decimal | Representa números reales con parte decimal | Representa secuencias de caracteres o texto | Almacena uno de dos valores: `true` o `false` | Representa un solo carácter alfanumérico |
| **C y C++**                | `int`, `short`  | `float`, `double`  | `char[]`  | `bool`  | `char`  |
| **Java**                   | `int`, `long`   | `float`, `double`  | `String`  | `boolean`  | `char`  |
| **Python**                 | `int`           | `float`            | `str`     | `bool`  | No tiene |
| **JavaScript**             | No tiene        | `Number`           | `String`  | `boolean`  | No tiene |
| **C#**                     | `int`, `short`, `long` | `float`, `double` | `string`  | `bool`  | `char`  |

## Calculo de espacio en memoria


### Datos y tamaños en memoria  
**Número entero (int)** → 4 bytes  
**Número de punto flotante (float)** → 4 bytes  
**Valor booleano (bool)** → 1 byte  
**Texto de 10 caracteres (string de 10 caracteres)** → 10 bytes  


### Cálculo de memoria por registro  
4 + 4 + 1 + 10 = 19 bytes por registro

### Cálculo total  
$$
0.1\text{ datos}/s \cdot 60\text{ s}/\text{min} = 6\text{ datos}/\text{min} \cdot 60\text{ min}/\text{h} = 360\text{ datos}/\text{h} \cdot 24\text{ h}/\text{día} = 8640\text{ datos}/\text{día}
$$

$$
8640\text{ datos}/\text{día} \cdot 19\text{ B}/\text{dato} = 164160\text{ B}/\text{día}
$$

8,640 /19 = 164,160 bytes = 160.3125KB = 0.156MB

### Resultado final  
Se necesitan aproximadamente **160.3 KB (0.156 MB)** 



