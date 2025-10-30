import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- PARÁMETROS DE LA SIMULACIÓN ---
G = 9.81  # Aceleración de la gravedad (m/s^2)
V0 = 30.0 # Velocidad inicial (m/s)
ANGLE_DEG = 65 # Ángulo de lanzamiento (grados)
ANGLE_RAD = np.deg2rad(ANGLE_DEG) # Conversión a radianes, requerida por numpy
MAX_TIME = (2 * V0 * np.sin(ANGLE_RAD)) / G # Tiempo total de vuelo

# --- FUNCIONES VECTORIALES (Posición y Velocidad) ---

def x_position(t):
    """Componente x de la posición (Ecuación Paramétrica)"""
    return V0 * np.cos(ANGLE_RAD) * t

def y_position(t):
    """Componente y de la posición (Ecuación Paramétrica)"""
    return V0 * np.sin(ANGLE_RAD) * t - 0.5 * G * t**2

def x_velocity(t):
    """Componente x de la velocidad (Derivada de x(t))"""
    # La velocidad horizontal es constante
    return V0 * np.cos(ANGLE_RAD)

def y_velocity(t):
    """Componente y de la velocidad (Derivada de y(t))"""
    return V0 * np.sin(ANGLE_RAD) - G * t

# --- CÁLCULO DE LA TRAYECTORIA ---
# Generamos 100 puntos de tiempo entre t=0 y el tiempo de vuelo máximo
times = np.linspace(0, MAX_TIME, 100)
x_data = x_position(times)
y_data = y_position(times)

# Encontramos el tiempo en el que la altura es máxima (donde Vy = 0)
time_peak = V0 * np.sin(ANGLE_RAD) / G
peak_height = y_position(time_peak)
peak_distance = x_position(time_peak)


# --- CONFIGURACIÓN DE LA GRÁFICA ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title(f'Animación de Movimiento Parabólico - $\\theta = {ANGLE_DEG}°$, $V_0 = {V0}m/s$')
ax.set_xlabel('Distancia Horizontal (x) [m]')
ax.set_ylabel('Altura Vertical (y) [m]')
ax.grid(True)
ax.set_aspect('equal', adjustable='box')

# Ajuste dinámico de límites para un buen encuadre
ax.set_xlim(0, x_data[-1] * 1.1)
ax.set_ylim(-1, peak_height * 1.2)

# La línea completa de la trayectoria (gris tenue)
full_trajectory, = ax.plot(x_data, y_data, ':', color='gray', alpha=0.5, label='Trayectoria Completa')

# El punto que se moverá (el proyectil)
projectile, = ax.plot([], [], 'o', color='red', markersize=8, label='Proyectil')

# Texto para mostrar la velocidad en tiempo real
velocity_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=10, verticalalignment='top')
time_text = ax.text(0.02, 0.90, '', transform=ax.transAxes, fontsize=10, verticalalignment='top')

ax.legend(loc='upper right')


# --- FUNCIÓN DE INICIALIZACIÓN DE LA ANIMACIÓN ---
def init():
    projectile.set_data([], [])
    velocity_text.set_text('')
    time_text.set_text('')
    return projectile, velocity_text, time_text

# --- FUNCIÓN DE ANIMACIÓN (Actualizada en cada fotograma) ---
def update(frame):
    # Obtiene la posición actual (x(t), y(t)) del proyectil
    current_x = x_data[frame]
    current_y = y_data[frame]
    current_t = times[frame]

    # Actualiza la posición del proyectil en la gráfica
    # CORRECCIÓN: Se envuelve current_x y current_y en una lista [] para que sean una "secuencia"
    projectile.set_data([current_x], [current_y])

    # Cálculo y presentación de la velocidad (Derivada)
    vx_val = x_velocity(current_t)
    vy_val = y_velocity(current_t)
    v_magnitude = np.sqrt(vx_val**2 + vy_val**2)

    # Actualiza el texto de velocidad
    velocity_info = (
        f"Velocidad (Derivada):\n"
        f"  $v_x$ = {vx_val:.2f} m/s\n"
        f"  $v_y$ = {vy_val:.2f} m/s\n"
        f"  $|v|$ = {v_magnitude:.2f} m/s"
    )
    velocity_text.set_text(velocity_info)
    time_text.set_text(f"Tiempo (t): {current_t:.2f} s")

    # Si se detiene la animación, se imprime un resumen
    if frame == len(times) - 1:
        print("\n--- RESUMEN DEL MOVIMIENTO ---")
        print(f"Distancia horizontal máxima: {x_data[-1]:.2f} m")
        print(f"Altura máxima: {peak_height:.2f} m (en t={time_peak:.2f} s)")
        print(f"Velocidad horizontal (constante): {x_velocity(0):.2f} m/s")
        print("-----------------------------\n")

    return projectile, velocity_text, time_text

# --- EJECUCIÓN DE LA ANIMACIÓN ---
# Crea la animación. interval es el retardo entre fotogramas en ms.
# frames=len(times) asegura que se usen todos los puntos calculados
anim = FuncAnimation(
    fig,
    update,
    frames=len(times),
    init_func=init,
    blit=True,
    repeat=False,
    interval=50
)

# Muestra el plot
plt.show()

