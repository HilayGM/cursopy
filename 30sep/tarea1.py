import requests
import time

def comparar_tiempo_carga():
    url1 = input("Introduce la primera página web (con https://): ")
    url2 = input("Introduce la segunda página web (con https://): ")

    def medir_tiempo(url):
        try:
            inicio = time.time()
            respuesta = requests.get(url, timeout=10)
            fin = time.time()
            if respuesta.status_code == 200:
                return fin - inicio
            else:
                print(f" La página {url} devolvió código {respuesta.status_code}")
                return float("inf")
        except Exception as e:
            print(f" Error al acceder a {url}: {e}")
            return float("inf")

    tiempo1 = medir_tiempo(url1)
    tiempo2 = medir_tiempo(url2)

    print(f"\nTiempo de carga de {url1}: {tiempo1:.3f} segundos")
    print(f"Tiempo de carga de {url2}: {tiempo2:.3f} segundos")

    if tiempo1 < tiempo2:
        print(f" {url1} carga más rápido.")
    elif tiempo2 < tiempo1:
        print(f" {url2} carga más rápido.")
    else:
        print(" Ambas cargaron en el mismo tiempo.")

# Ejecutar la función
comparar_tiempo_carga()
