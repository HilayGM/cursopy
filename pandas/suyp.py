import pandas as pd

# Crear el DataFrame con información de canciones de Twenty One Pilots
datos_canciones = {
    'ID_Cancion': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Titulo': ['Stressed Out', 'Heathens', 'Ride', 'Chlorine', 'Heavydirtysoul',
               'Car Radio', 'Lane Boy', 'Jumpsuit', 'Shy Away', 'Saturday'],
    'Album': ['Blurryface', 'Suicide Squad OST', 'Blurryface', 'Trench', 'Blurryface',
              'Vessel', 'Blurryface', 'Trench', 'Scaled and Icy', 'Scaled and Icy'],
    'Año_Lanzamiento': [2015, 2016, 2015, 2018, 2015, 2013, 2015, 2018, 2021, 2021],
    'Duracion_Segundos': [202, 195, 214, 325, 234, 268, 265, 298, 163, 154],
    'Reproducciones_Millones': [2800, 2100, 980, 450, 380, 520, 190, 340, 210, 180],
    'Genero': ['Alternative Hip Hop', 'Alternative Rock', 'Reggae Fusion', 'Electropop',
               'Rap Rock', 'Alternative Rock', 'Rap Rock', 'Alternative Rock', 
               'Indie Pop', 'Indie Pop'],
    'Popularidad': [98, 95, 88, 82, 85, 87, 75, 83, 79, 74],
    'Tempo_BPM': [170, 90, 120, 110, 176, 96, 136, 120, 157, 108],
    'Calificacion': [4.9, 4.8, 4.7, 4.6, 4.8, 4.9, 4.5, 4.7, 4.4, 4.3]
}

# Crear el DataFrame
df_canciones = pd.DataFrame(datos_canciones)

print("="*80)
print("DATAFRAME CREADO - CANCIONES DE TWENTY ONE PILOTS")
print("="*80)

# Mostrar todos los registros
print("\n--- Todos los Registros del DataFrame ---")
print(df_canciones)

# Mostrar primeros registros (head)
print("\n--- Primeros 5 Registros (df_canciones.head()) ---")
print(df_canciones.head(5))

# Información general del DataFrame (info)
print("\n--- Información General del DataFrame (df_canciones.info()) ---")
df_canciones.info()

# Descripción estadística (describe)
print("\n--- Descripción Estadística del DataFrame (df_canciones.describe()) ---")
print(df_canciones.describe())

# Búsquedas avanzadas
print("\n" + "="*80)
print("BÚSQUEDAS AVANZADAS")
print("="*80)

# Búsqueda 1: Canciones con más de 500 millones de reproducciones
print("\n--- Canciones con más de 500 Millones de Reproducciones ---")
canciones_populares = df_canciones[df_canciones['Reproducciones_Millones'] > 500]
print(canciones_populares)

# Búsqueda 2: Canciones del álbum Blurryface
print("\n--- Canciones del Álbum 'Blurryface' ---")
canciones_blurryface = df_canciones[df_canciones['Album'] == 'Blurryface']
print(canciones_blurryface)

# Búsqueda 3: Canciones con calificación mayor a 4.7 y popularidad mayor a 85
print("\n--- Canciones con Calificación > 4.7 Y Popularidad > 85 ---")
canciones_top = df_canciones[
    (df_canciones['Calificacion'] > 4.7) & 
    (df_canciones['Popularidad'] > 85)
]
print(canciones_top)

# Búsqueda 4: Canciones lanzadas después de 2015
print("\n--- Canciones Lanzadas Después de 2015 ---")
canciones_recientes = df_canciones[df_canciones['Año_Lanzamiento'] > 2015]
print(canciones_recientes)

# Búsqueda 5: Canciones de género Alternative Rock o Rap Rock
print("\n--- Canciones de Género 'Alternative Rock' o 'Rap Rock' ---")
canciones_rock = df_canciones[
    (df_canciones['Genero'] == 'Alternative Rock') | 
    (df_canciones['Genero'] == 'Rap Rock')
]
print(canciones_rock)