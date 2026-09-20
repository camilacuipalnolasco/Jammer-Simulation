#SIMULADOR DE GRAFICAS S11 Y S21
#Importar librerias

import numpy as np
import matplotlib.pyplot as plt


#Fondo oscuro
plt.style.use('dark_background')

#Solicitar datos de entrada
ValidarDato= False

while ValidarDato == False:
    Canal =int(input("Ingrese el canal a interferir (1, 6 u 11): "))
    if Canal ==1 or Canal ==6 or Canal ==11:
        ValidarDato= True
    else:
        print("Ingrese un canal valido")
        ValidarDato= False

AnchoBanda = 22 # En MHz

if Canal == 1 :
    FrecuenciaCentral =2412.0
elif Canal == 6 :
    FrecuenciaCentral =2437.0
else :
    FrecuenciaCentral =2462.0

#LÍMITES DE ANCHO DE BANDA
FrecInferior= FrecuenciaCentral - AnchoBanda/2
FrecSuperior = FrecuenciaCentral + AnchoBanda/2


#DEFINIR GRÁFICAS
#Definir dominio

frecuenciaEjeX = np.linspace(2300, 2600, 2000)

#Función de reflexión S11

S11 = -15 * np.exp(-((frecuenciaEjeX - FrecuenciaCentral) ** 2) / (2 * (AnchoBanda / 2) ** 2))

S11 = np.minimum(S11, -1.0)

#Función de Ganancia S21

S21_max = 25.0   # Ganancia del datasheet
S21_min = -20.0   # Piso en el gráfico(para que no vaya al -infinito
RangoGanancia = S21_max - S21_min

S21 = S21_min + RangoGanancia/ (1 + ((frecuenciaEjeX - FrecuenciaCentral) / AnchoBanda) ** 8)

#Ploteo de las gráficas
#Crear una ventana

fig, (axS11, axS21) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
#Gráfica S11

axS11.plot(frecuenciaEjeX, S11, color="cyan", linewidth=2, label ="S11")
axS11.axhline(-10, color="red", linestyle="--", alpha=0.7, label="(-10 dB)")
axS11.set_xlabel("Frecuencia (MHz)", fontsize=11)
axS11.set_ylabel("S11 (dB)", color="cyan", fontsize=11)
axS11.set_title("Parámetros S ", fontsize=12)
axS11.set_ylim(-20, 5)
axS11.grid(True, color="#333333", linestyle="--") #Fondo con cuadricula
axS11.legend(loc='lower right')

# Gráfica S21
axS21.plot(frecuenciaEjeX, S21, color="#FF00FF", linewidth=2, label="S21 ")
axS21.axhline(25, color='yellow', linestyle='--', alpha=0.7, label="(+25 dB)")
axS21.set_xlabel("Frecuencia (MHz)")
axS21.set_ylabel("S21 (dB)")
axS21.set_ylim(-25, 30)
axS21.grid(True, color="#333333", linestyle="--") #Fondo con cuadricula
axS21.legend(loc='lower right')

plt.tight_layout()
plt.show()
