
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
T_amb = 20  # Temperatura ambiente constante en °C
T0 = 25    # Temperatura inicial en °C
H0 = 60    # Humedad relativa inicial en %
delta_t = 1  # Paso de tiempo en horas
total_time = 24  # Tiempo total en horas

# Inicializar arrays para almacenar los valores de T y H
time_points = np.arange(0, total_time + delta_t, delta_t)
T = np.zeros(len(time_points))
H = np.zeros(len(time_points))

# Condiciones iniciales
T[0] = T0
H[0] = H0

# Método de Euler
for n in range(len(time_points) - 1):
    T[n+1] = T[n] + delta_t * (-0.07 * (T[n] - T_amb) + 0.1 * H[n])
    H[n+1] = H[n] + delta_t * (-0.03 * H[n] + 0.05 * (T_amb - T[n]))

# Imprimir los resultados de cada hora
print("Hora\tTemperatura (°C)\tHumedad Relativa (%)")
for n in range(len(time_points)):
    print(f"{time_points[n]:.0f}\t{T[n]:.4f}\t\t\t{H[n]:.4f}")

# Gráficas de los resultados
plt.figure(figsize=(14, 6))

# Gráfica de la temperatura
plt.subplot(1, 2, 1)
plt.plot(time_points, T, marker='o', label='Temperatura (T)')
for n in range(len(time_points)):
    plt.annotate(f"{T[n]:.2f}", (time_points[n], T[n]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Temperatura (°C)')
plt.title('Evolución de la Temperatura')
plt.legend()
plt.grid(True)

# Gráfica de la humedad relativa
plt.subplot(1, 2, 2)
plt.plot(time_points, H, marker='o', label='Humedad Relativa (H)', color='orange')
for n in range(len(time_points)):
    plt.annotate(f"{H[n]:.2f}", (time_points[n], H[n]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Humedad Relativa (%)')
plt.title('Evolución de la Humedad Relativa')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()



