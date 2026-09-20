#SIMULACIÓN DE JAMMER
""
"""
import os
print(os.path.abspath(__file__))
"""
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
#INGRESO DE DATOS
print("====== INGRESO DE DATOS DE ENTRADA =======")

ValidarDato = False
while ValidarDato == False:
    Canal =int(input("Ingrese el canal a interferir (1, 6 u 11): "))
    if Canal ==1 or Canal ==6 or Canal ==11:
        ValidarDato= True
    else:
        print("Ingrese un canal valido")
        ValidarDato= False
PotenciaEntrada = float(input("Introducir la Potencia de Entrada en dBm: "))
Perdidas = float(input("Pérdidas de cable/conectores en dB : "))

#DATOS FIJOS

AnchoBanda = 22 # En MHz
GananciaAntena = 2.15 # en dBi
if Canal == 1 :
    FrecuenciaCentral =2412.0
elif Canal == 6 :
    FrecuenciaCentral =2437.0
else :
    FrecuenciaCentral =2462.0

#PRESUPUESTO DE ENLACE
PotenciaRadiada = PotenciaEntrada  + GananciaAntena -  Perdidas
PotenciaRadiadamW = round(10**(PotenciaRadiada/10),2)
VoltajePico = round(sqrt(2*50*(PotenciaRadiadamW/1000)),2)

#LÍMITES DE ANCHO DE BANDA
FrecInferior= FrecuenciaCentral - AnchoBanda/2
FrecSuperior = FrecuenciaCentral + AnchoBanda/2

print("La frecuencia de corte inferior es ",FrecInferior)
print("La frecuencia de corte superior es ",FrecSuperior)

#############################################
### Cálculo de las gráfcas ####

#Definición de la forma de la curva

FrecEjeX = np.linspace(2100,3000,2000)
RadioCanal = AnchoBanda / 2
espectro_dBm = PotenciaRadiada - 3 * (((FrecEjeX - FrecuenciaCentral) / RadioCanal) ** 2)
espectro_dBm = np.maximum(espectro_dBm, -80)
#Creación del ruido

RuidoAleatorio = np.random.normal(0.0, 3,2000) # Mismo "ancho" que el eje x, si cambia el argumento en Frecx, cambiar aqui
RuidoGeneral = -85 + RuidoAleatorio # El ruido rtotal es la suma del ruido base más la distribución normal dle ruido


# Creación de la ventana
plt.style.use('dark_background') #Fondo oscuro
plt.figure(figsize=(10, 5))



#Creacion de la función
EspectroConRuido = np.maximum(espectro_dBm + RuidoAleatorio*0.2,RuidoGeneral) # Elige la mayor funcion entre el ruido y el espectro
plt.plot(FrecEjeX, EspectroConRuido, color='red', label=f'Canal {Canal}')
plt.axvline(FrecInferior, color='skyblue', linestyle='--', label=f'Límite Inf: {FrecInferior} MHz')
plt.axvline(FrecSuperior, color='skyblue', linestyle='--', label=f'Límite Sup: {FrecSuperior} MHz')
plt.axhline(PotenciaRadiada - 3, color='pink', linestyle=':', label='Corte -3 dB')
plt.grid(True, color='#333333', linestyle='--') #Fondo con cuadricula
plt.xlabel("Frecuencia (MHz)")
plt.ylabel("Potencia (dBm)")
plt.ylim(-90,30)

plt.show()




