import pandas as pd


datos = "online_retail.csv"
rd = pd.read_csv(datos)

print(rd)


print("las columnas son :\n", rd.columns)

Nfilas,Ncolumnas = rd.shape
print("las filas son:", Nfilas, "\n Las columnas son:", Ncolumnas)

print("informacion general : \n", rd.describe())

print("ventas diarias: \n" , rd["Quantly"])

print("promedio de ventas: \n", rd["Quantly"].mean())

print ("total de ventas: \n", rd["Quantly"].sum())


#tarea 
#a partir de la siguiente lista muestra la informacion mas relevante
#total de registros
#promedio
#mediana
#suma 
#valor mas alto 
#valor mas bajo 
#resumen