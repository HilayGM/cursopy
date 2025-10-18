import numpy as np
import matplotlib.pyplot as plt


lenguajes = np.array([
    'Python', 'Java', 'C/C++', 'Objective-C', 'JavaScript', 
    'R', 'C#', 'PHP', 'Swift', 'Rust'
])
cuotas = np.array([
    28.97, 13.94, 10.54, 7.05, 6.33, 
    5.27, 3.96, 3.19, 2.93, 2.59
])


plt.figure(figsize=(12, 7))


bars = plt.bar(
    lenguajes,
    cuotas,
    color='darkgreen'
)


for bar in bars:
    yval = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2, 
        yval + 0.2, 
        f'{yval:.2f}%', 
        ha='center', 
        va='bottom', 
        fontsize=9
    )



plt.xlabel("Lenguaje de Programación", fontsize=12)
plt.ylabel("Cuota de Popularidad (%) (Índice PYPL)", fontsize=12)
plt.title("Los 10 Lenguajes de Programación Más Populares (Índice PYPL, Octubre 2025) - Con NumPy", fontsize=14)


plt.xticks(rotation=45, ha='right')


plt.grid(axis='y', linestyle='--', alpha=0.6)


plt.tight_layout()


plt.show()