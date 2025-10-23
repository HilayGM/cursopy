import pandas as pd

# Lista original
LEjercicio = [10,20,30,40,50,60,70,80,90,None,100,200,300,400,500,600,700,800,900,
              1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10,None,-1,-2,-3,-4,-5,-6,-7]

# Crear un DataFrame
df = pd.DataFrame(LEjercicio, columns=["Valores"])

# Eliminar los valores nulos (None)
df = df.dropna()

# Calcular las estadísticas básicas
total = df["Valores"].count()
suma = df["Valores"].sum()
promedio = df["Valores"].mean()
mediana = df["Valores"].median()
maximo = df["Valores"].max()
minimo = df["Valores"].min()

# Mostrar resultados
print("📊 RESUMEN DE DATOS 📊")
print(f"Total de registros: {total}")
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana}")
print(f"Suma total: {suma}")
print(f"Valor más alto: {maximo}")
print(f"Valor más bajo: {minimo}")

# También puedes usar describe() para un resumen completo
print("\n📈 Resumen con describe():")
print(df.describe())
