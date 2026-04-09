# listas-python
En este repositorio veremos como funcionan las listas en Python de distintas formas

## Primer ejercicio

### Análisis

#### Variabes

- mejores_amigos = [] lista de amigos que tu quieras colocar (son ssolo 3)

#### Procesamiento

mejores_amigos = ["Javier", "Anthony", "Sosa"]
mejores_amigos.append("Omar")
mejores_amigos.pop(0)

print('Mis amigos actuales son:', mejores_amigos)
print('Total de amigos:', len(mejores_amigos))

### Diseño

![alt text](image.png)

### Construción

esten el archivo ejercicio 1.py la construcción del programa


## Segundo ejercicio

### Análisis

#### Variabes

- nombres = [] los nombres de tus compañeros que quieras colocar (son 5)

- edades = [] las edades de tus compañeros

- musica = [] los generos de musica que les gusta mas a tus compañeros


#### Procesamiento

nombres = ['Rolando', 'Juan Diego', 'Andres', 'Ivdejel', 'Robinson']
edades = [15, 15, 15, 15, 17]
musica = ['Reggaeton', 'Cumbia', 'Vallenato', 'Salsa', 'Vocaloid']

promedio = sum(edades) / len(edades)
print('Promedio de edad:', promedio)

mayores = [edad for edad in edades if edad > 15]
print('Edades > 15:', mayores)

fans_rock = [gen for gen in musica if gen == 'Rock']
print('Total fans rock:', len(fans_rock))

### Diseño

![alt text](image.png)

### Construción

esten el archivo ejercicio 2.py la construcción del programa