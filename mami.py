import numpy as np
import scipy.stats as stats

# Valores de la muestra
muestra_1 = [
    102, 98, 93, 100, 98, 105, 115, 110, 99, 120,
    115, 130, 100, 86, 95, 103, 105, 92, 99, 134,
    116, 118, 89, 102, 128, 99, 119, 128, 110, 130,
    112, 114, 106, 114, 100, 116, 108, 113, 106, 105,
    120, 106, 110, 100, 106, 117, 109, 108, 105, 106
]

muestra = [6.80, 6.78,6.77,6.80,6.78,6.80, 6.82,6.81,6.80,6.79]

# Calcular la media y desviación estándar muestral
media_muestral = np.mean(muestra)
desviacion_estandar_muestral = np.std(muestra, ddof=1)  # ddof=1 para muestra
n = len(muestra)

# Calcular el intervalo de confianza al 95%
intervalo_95 = stats.t.interval(0.95, n-1, loc=media_muestral, scale=stats.sem(muestra))

# Calcular el intervalo de confianza al 90%
intervalo_90 = stats.t.interval(0.90, n-1, loc=media_muestral, scale=stats.sem(muestra))

# Prueba de hipótesis: H0: μ = 100
t_stat, p_value = stats.ttest_1samp(muestra, 100)
rechazar_H0_5 = p_value < 0.05
rechazar_H0_10 = p_value < 0.10

# Calcular la moda
moda = stats.mode(muestra)[0][0]

# Calcular la mediana
mediana = np.median(muestra)

# Imprimir resultados
print("Media muestral:", media_muestral)
print("Desviación estándar muestral:", desviacion_estandar_muestral)
print("Intervalo de confianza al 95%:", intervalo_95)
print("Intervalo de confianza al 90%:", intervalo_90)
print("Rechazar H0 al 5%:", rechazar_H0_5)
print("Rechazar H0 al 10%:", rechazar_H0_10)
print("Longitud más frecuente (moda):", moda)
print("Mediana:", mediana)
