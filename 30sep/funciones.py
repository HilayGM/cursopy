#funciones son fracmentos de codigo que realizan una tarea especifica
#se definen con la palabra reservada def
#una regla que al aplicarse se genera un unico numero real 
#se puedes utilizar diferntes variables 
#

#funciones basicas 
def f1 (x, y) :
    z = x + y
    return z 

resultado = f1 (3, 5)
print (resultado)

#funciones polinomiales 
def f2 (x, y) : return x**2+y**2
print(f2(3,4))

#funciones cuadradas o de raiz cuadrada 
def f3 (x, y):
    return (x**2+y**2)**0.5
print(f3(3,4))


#funciones racionales 
def f4(x,y):
    return (x**2+1)/(y+1)
print(f4(1,2))

#funciones exponensiales
#para este caso ya se importa numpy
import numpy as np
def f5 (x,y):
    return np.exp(x*y)

print(f5(1,2))

#funciones logaritmicvas 
def f6(x,y):
    return np.log(x*y)
print(f6(1,2))

#funciones trigonometricas 
def f7(x,y):
    return np.sin(x) + np.cos(y)
print(f7(np.pi/2,0))

#funciones absolutas
def f8 (x,y):
    return abs(x-y)
print(f8(7,10))
#______________________________________________________________________________

def costo_casa(b, h):
    return b*50000 + h*80000 

#nb = int(input("Ingrese el numero de habitaciones: "))
#nh = int(input("Ingrese el numero de baños: "))
#rint("El costo de la casa es: ", costo_casa(nb, nh))



#------------------------------------------------------------------------------
#vamos por tacos 

def cuenta_individual (t,b):
    return 15*t+b*25
print("El costo de la cuenta individual es: ", cuenta_individual(2,3))

#funcion para evalularr la optimizacion

def optimizacion (nl ,t):
    return nl*1+ t*100
print()

#crear una funcion pasra evaluar 2 metricas de las paginas web, al cargar por primera vez   