import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # 1. Cargar el dataset climático
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Configuración de lienzo y diagrama de dispersión
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6)

    # 3. Primer ajuste lineal: Tendencia global (1880 proyectado hasta 2050)
    res_global = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended_global = np.arange(df['Year'].min(), 2051)
    line_global = res_global.intercept + res_global.slope * years_extended_global
    ax.plot(years_extended_global, line_global, color='red')

    # 4. Segundo ajuste lineal: Tendencia reciente (2000 proyectado hasta 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended_recent = np.arange(2000, 2051)
    line_recent = res_recent.intercept + res_recent.slope * years_extended_recent
    ax.plot(years_extended_recent, line_recent, color='green')

    # 5. Etiquetas normativas exactas y título
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Guardar imagen y retornar objeto de ejes para test_module.py
    fig.savefig('sea_level_plot.png')
    return ax