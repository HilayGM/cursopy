
import statistics

LEjercicio = [10,20,30,40,50,60,70,80,90,None,100,200,300,400,500,600,700,800,900,
              1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10,None,-1,-2,-3,-4,-5,-6,-7]

# limpiar None
valores = [x for x in LEjercicio if x is not None]

total = len(valores)
promedio = sum(valores) / total
mediana = statistics.median(valores)
suma = sum(valores)
maximo = max(valores)
minimo = min(valores)

print(f"Total de registros: {total}")
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana}")
print(f"Suma total: {suma}")
print(f"Valor más alto: {maximo}")
print(f"Valor más bajo: {minimo}")
