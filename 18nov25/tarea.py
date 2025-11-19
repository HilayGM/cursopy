import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definición del nombre para los títulos de las gráficas
my_name = "Martin Moreno Libreros"


try:
    df = pd.read_csv("software_dev_data.csv")
    

    df.columns = ['Fecha', 'Proyecto', 'Desarrollador', 'TipoTarea', 'Lenguaje', 'Estado', 
                  'Horas', 'BugsEncontrados', 'Commits', 'CoberturaCodigo', 
                  'ComplejidadCiclomatica', 'LineasCodigo']


    for col in ['Horas', 'BugsEncontrados', 'Commits', 'CoberturaCodigo', 'ComplejidadCiclomatica', 'LineasCodigo']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(inplace=True)
    
except FileNotFoundError:
    print("Error: El archivo 'software_dev_data.csv' no se encontró. Asegúrate de que esté en el directorio correcto.")
    exit()



print("Generando Gráfica 1...")
horas_por_tarea = df.groupby('TipoTarea')['Horas'].agg(['mean', 'median']).sort_values(by='mean', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
horas_por_tarea.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e'], alpha=0.8)

ax.set_title(f'Análisis de Horas Trabajadas por Tipo de Tarea (por {my_name})', fontsize=14, fontweight='bold')
ax.set_xlabel('Tipo de Tarea', fontsize=12)
ax.set_ylabel('Horas Trabajadas', fontsize=12)
ax.legend(['Media (Horas)', 'Mediana (Horas)'])
ax.tick_params(axis='x', rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()




plt.savefig('horas_por_tarea.png')
plt.close(fig)


print("Generando Gráfica 2...")

df['Productividad'] = df['LineasCodigo'] / df['Horas']


df['Productividad'] = df['Productividad'].replace([np.inf, -np.inf], 0)


productividad_desarrollador = df.groupby('Desarrollador')['Productividad'].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
productividad_desarrollador.plot(kind='bar', ax=ax, color='#8A2BE2', alpha=0.8)

ax.set_title(f'Productividad Promedio por Desarrollador (por {my_name})', fontsize=14, fontweight='bold')
ax.set_xlabel('Desarrollador', fontsize=12)
ax.set_ylabel('Líneas de Código por Hora (Productividad)', fontsize=12)
ax.tick_params(axis='x', rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# plt.show()
plt.savefig('productividad_desarrollador.png')
plt.close(fig)


print("Generando Gráfica 3...")
metricas_por_estado = df.groupby('Estado')[['Horas', 'LineasCodigo', 'BugsEncontrados']].mean()

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=False) 

metricas_por_estado['Horas'].sort_values(ascending=False).plot(
    kind='bar', ax=axes[0], color='#2ecc71', alpha=0.8
)
axes[0].set_title('Horas Promedio', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Horas')
axes[0].tick_params(axis='x', rotation=45)
axes[0].set_xlabel('Estado de la Tarea')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)







metricas_por_estado['LineasCodigo'].sort_values(ascending=False).plot(
    kind='bar', ax=axes[1], color='#3498db', alpha=0.8
)
axes[1].set_title('Líneas de Código Promedio', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Líneas de Código')
axes[1].tick_params(axis='x', rotation=45)
axes[1].set_xlabel('Estado de la Tarea')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)


metricas_por_estado['BugsEncontrados'].sort_values(ascending=False).plot(
    kind='bar', ax=axes[2], color='#e74c3c', alpha=0.8
)
axes[2].set_title('Bugs Encontrados Promedio', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Bugs Encontrados')
axes[2].tick_params(axis='x', rotation=45)
axes[2].set_xlabel('Estado de la Tarea')
axes[2].grid(axis='y', linestyle='--', alpha=0.7)





fig.suptitle(f'Comparación de Métricas Clave por Estado de Tarea (por {my_name})', fontsize=16, fontweight='heavy')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
plt.savefig('metricas_por_estado.png')
plt.close(fig)

print("¡Proceso de generación de gráficas completado!")