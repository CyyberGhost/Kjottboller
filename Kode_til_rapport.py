import numpy as np
import math as m
import matplotlib.pyplot as plt

t = np.array([i for i in range(21)])  # Tid i minutter
temp_mal = np.array([80,73,67,63,59,55,53,50,48,47,44,44,42,41,40,39,39,38,37,36,36]) # Oppgitt i celsius

Tk = 26 # Rom temperatur: Celsius
T0 = temp_mal[0] # Celsius

c = T0-Tk # Celcius
alf_list = [] # Ingenting hittil

for i in range(1,len(t)):
  alf_temp = (1/i) * m.log(c/(temp_mal[i]-Tk))
  alf_list.append(alf_temp)

alf = sum(alf_list)/len(alf_list) # Alfa oppgitt i: (60s)**-1
ualf = (max(alf_list)-min(alf_list))/2 #Usikkerheten til alfa

x = np.linspace(0,t[-1],10000)

print(f"Alfa er: ({alf:.2f} ± {ualf:.2f})/min")
print(f"T(t) = {c}*e^(-{alf:.2f}*t)+{Tk}")
def T(t):
  return c*m.e**(-alf*t)+Tk
  
plt.plot(t, temp_mal, "-", label="Målinger", color="gold") # Hadde lyst på en gul farge, og gull så best ut
plt.plot(x, T(x), "-", label="Modell", color="r")
plt.xlabel("Tid (minutter)")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur av kjøttboller")
plt.legend()
plt.grid(True)
plt.show()