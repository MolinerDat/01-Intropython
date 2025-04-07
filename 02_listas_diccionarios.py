# Listas y diccionarios en Python

# ---------- LISTAS ----------
# Una lista es una colección ordenada y modificable
frutas = ["manzana", "banana", "naranja"]

# Acceder a elementos
print("Primera fruta:", frutas[0])

# Modificar un elemento
frutas[1] = "kiwi"
print("Lista modificada:", frutas)

# Añadir elementos
frutas.append("pera")
print("Lista con nueva fruta:", frutas)

# Recorrer la lista
print("Frutas en la lista:")
for fruta in frutas:
    print("-", fruta)

# ---------- DICCIONARIOS ----------
# Un diccionario almacena pares clave:valor
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Madrid"
}

# Acceder a valores por clave
print("Nombre:", persona["nombre"])

# Modificar un valor
persona["edad"] = 29

# Añadir una nueva clave
persona["profesion"] = "Analista de datos"

# Recorrer el diccionario
print("Datos de la persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
