import pandas as pd
import numpy as np 



data = {
    'Juego': [
        'Cyberpunk 2077', 'The Witcher 3', 'Grand Theft Auto V', 'Red Dead Redemption 2', 'Minecraft',
        'Terraria', 'Stardew Valley', 'Rocket League', 'Among Us', 'Hades'
    ],
    'Genero': [
        'RPG', 'RPG', 'Action', 'Action', 'Sandbox',
        'Sandbox', 'RPG', 'Sports', 'Party', 'Action'
    ],
    'Plataforma': [
        'PC/Consola', 'PC/Consola', 'PC/Consola', 'PC/Consola', 'Multi',
        'Multi', 'Multi', 'Multi', 'Multi', 'PC/Consola'
    ],
    'Anio_Lanzamiento': [2020, 2015, 2013, 2018, 2011, 2011, 2016, 2015, 2018, 2020],
    'Ventas_Globales_M': [18.0, 50.0, 190.0, 60.0, 300.0, 44.0, 20.0, 25.0, 15.0, 2.0], # Millones
    'Puntuacion_Critica': [86, 92, 97, 96, 93, 88, 89, 86, 79, 93], # Puntuación de 100
    'Desarrollador': [
        'CD Projekt', 'CD Projekt', 'Rockstar Games', 'Rockstar Games', 'Mojang',
        'Re-Logic', 'ConcernedApe', 'Psyonix', 'Innersloth', 'Supergiant Games'
    ],
    'Precio_Lanzamiento_USD': [59.99, 49.99, 59.99, 59.99, 26.95, 9.99, 14.99, 19.99, 4.99, 24.99],
    'Multijugador': [
        'No', 'No', 'Sí', 'Sí', 'Sí',
        'Sí', 'Sí', 'Sí', 'Sí', 'No'
    ],
    'Region_Principal_Venta': [
        'Europa', 'Global', 'Norteamérica', 'Norteamérica', 'Global',
        'Global', 'Global', 'Norteamérica', 'Global', 'Global'
    ]
}

df_juegos = pd.DataFrame(data)

print("="*60)
print("DataFrame Creado: Análisis de Ventas de Videojuegos")
print("="*60)



print("\n--- 3.1 Todos los Registros del DataFrame (df_juegos) ---")
print(df_juegos)


print("\n--- 3.2 Primeros 5 Registros (df_juegos.head()) ---")
print(df_juegos.head(5))


print("\n--- 3.3 Información General del DataFrame (df_juegos.info()) ---")
df_juegos.info()

print("\n--- 3.4 Descripción Estadística del DataFrame (df_juegos.describe()) ---")
print(df_juegos.describe())



print("\n--- 5. Acceso a Datos Específicos ---")


precio = df_juegos['Precio_Lanzamiento_USD']
print("\nAccediendo a la Columna 'Precio_Lanzamiento_USD':")
print(precio)


fila_gta = df_juegos.iloc[2]
print("\nAccediendo a la Fila del índice 2 (iloc[2] - GTA V):")
print(fila_gta)


juegos_best_sellers = df_juegos[df_juegos['Ventas_Globales_M'] > 50.0]
print("\nAccediendo a juegos 'Best Sellers' (> 50 Millones de Ventas Globales):")
print(juegos_best_sellers)

68
juegos_rpg_multi = df_juegos[
    (df_juegos['Genero'] == 'RPG') & 
    (df_juegos['Multijugador'] == 'Sí')
]
print("\nAccediendo a juegos de Género 'RPG' Y 'Multijugador' ('Sí'):")
print(juegos_rpg_multi)
