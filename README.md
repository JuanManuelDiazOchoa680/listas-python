# listas-python
En este repositorio veremos como funcionan las listas en Python de distintas formas

## 1. Concepto y Sintaxis
Las listas permiten agrupar múltiples elementos en una sola estructura, optimizando la gestión de memoria y el orden de los datos
y se definen mediante corchetes []

## 2. Indexación y Acceso
El acceso a los elementos se realiza mediante índices numéricos

- Índice 0: Primer elemento de la lista

- Índice -1: Acceso directo al último elemento

## 3. Manipulación de Colecciones
Acciones principales para la gestión del "inventario" de datos

- append(elemento): Agrega un objeto al final de la lista

- pop(índice): Elimina el elemento en la posición especificada

- len(lista): Retorna la cantidad total de elementos

- sort() / reverse(): Ordenamiento y        reversión de la secuencia

## 4. List Comprehensions
Técnica avanzada para la creación y filtrado eficiente de listas en una sola línea de código

Estructura: [ expresión for elemento in iterable if condición ]
Casos de uso:
Transformación: [x * 12 for x in lista]

Filtrado: [x for x in lista if x > 15]

## 5. Análisis de Datos Proyectado
La implementación de estas herramientas permite el procesamiento de datos estadísticos, como el cálculo de promedios combinando sum() y len(), así como la segmentación de bases de datos mediante filtros condicionales

### Primer ejercicio

#### Análisis

##### Variabes

- mejores_amigos = [] lista de amigos que tu quieras colocar (son ssolo 3)

##### Procesamiento

mejores_amigos = ["Javier", "Anthony", "Sosa"]
mejores_amigos.append("Omar")
mejores_amigos.pop(0)

print('Mis amigos actuales son:', mejores_amigos)
print('Total de amigos:', len(mejores_amigos))

#### Diseño

![alt text](image.png)

#### Construción

esten el archivo ejercicio 1.py la construcción del programa


### Segundo ejercicio

#### Análisis

##### Variabes

- nombres = [] los nombres de tus compañeros que quieras colocar (son 5)

- edades = [] las edades de tus compañeros

- musica = [] los generos de musica que les gusta mas a tus compañeros


##### Procesamiento

nombres = ['Rolando', 'Juan Diego', 'Andres', 'Ivdejel', 'Robinson']
edades = [15, 15, 15, 15, 17]
musica = ['Reggaeton', 'Cumbia', 'Vallenato', 'Salsa', 'Vocaloid']

promedio = sum(edades) / len(edades)
print('Promedio de edad:', promedio)

mayores = [edad for edad in edades if edad > 15]
print('Edades > 15:', mayores)

fans_rock = [gen for gen in musica if gen == 'Rock']
print('Total fans rock:', len(fans_rock))

#### Diseño

![alt text](image.png)

#### Construción

esten el archivo ejercicio 2.py la construcción del programa

### Tercer ejercicio

#### Análisis

##### Variabes

- lista =[]
- lista_1= [1, 2, 3, 4, 5]
- resultado = obtener_primero_ultimo(lista_1)


##### Procesamiento

def obtener_primero_ultimo(lista):

    if lista:
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return "faltan elementos bro"
    else:
        return "la lista esta vacia bro"

lista_1= [1, 2, 3, 4, 5]

resultado = obtener_primero_ultimo(lista_1)
print(resultado)

#### Diseño

![alt text](image.png)

#### Construción

esten el archivo ejercicio 3.py la construcción del programa

