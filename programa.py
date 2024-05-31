from collections import Counter

# Valores de la muestra
muestra = [
    102, 98, 93, 100, 98, 105, 115, 110, 99, 120,
    115, 130, 100, 86, 95, 103, 105, 92, 99, 134,
    116, 118, 89, 102, 128, 99, 119, 128, 110, 130,
    112, 114, 106, 114, 100, 116, 108, 113, 106, 105,
    120, 106, 110, 100, 106, 117, 109, 108, 105, 106
]

# Contar las frecuencias de cada valor en la muestra
frecuencias = Counter(muestra)

# Ordenar la tabla de frecuencias por valor
tabla_frecuencias = sorted(frecuencias.items())

# Imprimir la tabla de frecuencias
print("Valor\tFrecuencia")
for valor, frecuencia in tabla_frecuencias:
    print(f"{valor}\t{frecuencia}")
