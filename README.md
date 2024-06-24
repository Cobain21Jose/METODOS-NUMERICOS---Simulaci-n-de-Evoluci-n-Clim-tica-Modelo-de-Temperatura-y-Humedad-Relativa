<p align="center">
  <a href="https://tesjo.edomex.gob.mx">
    <img src="tesjo.png" alt="Logo de Ing en Sistemas Computacionales - Tesjo">
  </a>
</p>

# Ing en Sistemas Computacionales - Tesjo

Este programa simula la evolución de la temperatura y la humedad relativa en un entorno específico a lo largo de un período de 24 horas utilizando el método de Euler para resolver un sistema de ecuaciones diferenciales ordinarias.

[![Logo1](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/isc.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)
[![Logo2](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)](https://www.python.org/downloads/)

# Simulación de Evolución Climática

Este proyecto simula la evolución de la temperatura y la humedad relativa en un entorno específico a lo largo de un período de 24 horas utilizando el método de Euler para resolver un sistema de ecuaciones diferenciales ordinarias.


## Descripción del Proyecto

Este proyecto tiene como objetivo simular la evolución de la temperatura y la humedad relativa en un entorno específico a lo largo de un período de 24 horas. Para lograrlo, se utiliza el método de Euler para resolver un sistema de ecuaciones diferenciales ordinarias (EDO). Este tipo de simulación es útil para entender cómo cambian estas variables climáticas a lo largo del tiempo y puede ser aplicada en diversos campos como la meteorología, la ingeniería ambiental y la agricultura.

### Introducción

La simulación del clima es una herramienta poderosa para predecir condiciones futuras y para el análisis de diferentes escenarios. En este proyecto, se considera una temperatura ambiente constante y se estudia cómo varían la temperatura y la humedad relativa en un entorno cerrado a lo largo de un día completo.

### Metodología

Para resolver el sistema de ecuaciones diferenciales que modelan la evolución de la temperatura y la humedad relativa, se emplea el método de Euler, un método numérico sencillo pero eficaz para la integración de EDOs. 

Las ecuaciones diferenciales utilizadas en este proyecto son:

[![Logo8](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/imagen_2024-06-23_151310460.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)

Donde:
- \(T\) es la temperatura en grados Celsius.
- \(H\) es la humedad relativa en porcentaje.
- \(T_{amb}\) es la temperatura ambiente constante (20°C en este caso).


## Requisitos

- Python (probado en Python 3.7+)
- Bibliotecas: numpy, matplotlib

## Sistema Utilizado para la creacion de este proyecto

Mac os Sonoma 14.5

[![Logo3](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/macossonoma.png)](https://www.apple.com/mx/macos/sonoma/)

## Hadware del Equipo
<p align="center">
  <img src="hadware.png" alt="Hadware del equipo">
</p>

# Plantamiento Matematico
1. ## Sistema de Ecuaciones Diferenciales
[![Logo5](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/imagen_2024-06-23_145828261.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)

2. ## Condiciones Iniciales
[![Logo6](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/imagen_2024-06-23_150248608.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)

2. ## Paso por el Tiempo
[![Logo7](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/imagen_2024-06-23_150510834.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)

3. ## Formulas de Euler
[![Logo8](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/imagen_2024-06-23_151310460.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)

## Estado de Resultados de Hora de Temperatura x Humedad Relativa 

| Hora | Temperatura (°C) | Humedad Relativa (%) |
|------|-------------------|----------------------|
| 0    | 25.0000           | 60.0000              |
| 1    | 30.6500           | 57.9500              |
| 2    | 35.6995           | 55.6790              |
| 3    | 40.1684           | 53.2237              |
| 4    | 44.0790           | 50.6185              |
| 5    | 47.4553           | 47.8960              |
| 6    | 50.3231           | 45.0864              |
| 7    | 52.7091           | 42.2176              |
| 8    | 54.6412           | 39.3156              |
| 9    | 56.1479           | 36.4041              |
| 10   | 57.2579           | 33.5046              |
| 11   | 58.0004           | 30.6366              |
| 12   | 58.4040           | 27.8174              |
| 13   | 58.4974           | 25.0627              |
| 14   | 58.3089           | 22.3860              |
| 15   | 57.8659           | 19.7989              |
| 16   | 57.1952           | 17.3117              |
| 17   | 56.3227           | 14.9326              |
| 18   | 55.2733           | 12.6685              |
| 19   | 54.0710           | 10.5247              |
| 20   | 52.7385           | 8.5054               |
| 21   | 51.2974           | 6.6134               |
| 22   | 49.7679           | 4.8501               |
| 23   | 48.1692           | 3.2162               |
| 24   | 46.5189           | 1.7112               |

## Grafica de Python
[![Logo9](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/imagen_2024-06-23_153257729.png)](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa)

## Museos y Archivos
Descripción: Museos y archivos necesitan controlar estrictamente la temperatura y la humedad para preservar obras de arte y documentos históricos. Temperaturas alrededor de los 23 grados Celsius son comunes en estos entornos.
Aplicación: Simulaciones ayudan a prever y mantener las condiciones necesarias para la conservación de piezas valiosas.

## Conclusión
En este ejercicio, podemos observar cómo evolucionan la temperatura y la humedad relativa en un entorno específico a lo largo de un día. Utilizando el método de Euler, podemos resolver el sistema de ecuaciones diferenciales y predecir los cambios en el clima. Los resultados muestran una disminución inicial de la humedad relativa, seguida de un aumento gradual. La temperatura aumenta rápidamente al inicio y luego se estabiliza alrededor de los 23°C. Este tipo de análisis es crucial para entender y prever condiciones climáticas en distintos entornos.

# Explicacion en YouTube
[![Logo9](https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa/blob/main/youtube.png)](https://www.youtube.com/watch?v=_QXeYHNZCws)

# Video: Metodos Numéricos - Simulación de Evolución Climática (Metodo de Euler)
[![Watch the video](https://img.youtube.com/vi/_QXeYHNZCws/0.jpg)](https://www.youtube.com/watch?v=_QXeYHNZCws)


## Instalación en Terminal

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Cobain21Jose/METODOS-NUMERICOS---Simulaci-n-de-Evoluci-n-Clim-tica-Modelo-de-Temperatura-y-Humedad-Relativa.git

2. Ejecuta en Visual Studio Code (Python)
    ```bash
       code .
3. Se Abrira el Proyecto "Simulación de Evolución Climática"

4. Corre el codigo

5. Visualizacion de Temperaturas Graficamente tanto, en la salida de terminal


