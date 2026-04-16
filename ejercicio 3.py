# Ejercicio 3: Escribe una función que tome una lista como argumento y devuelva una tupla con el primer y el último elemento de la lista. Si la lista está vacía, devuelve un mensaje indicando que la lista está vacía. Si la lista tiene solo un elemento, devuelve un mensaje indicando que faltan elementos.

def obtener_primero_ultimo(lista):
    if lista:
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return "faltan elementos bro"
    else:
        return "la lista esta vacia bro"

# Output

lista_1= [1, 2, 3, 4, 5]
resultado = obtener_primero_ultimo(lista_1)
print(resultado)
