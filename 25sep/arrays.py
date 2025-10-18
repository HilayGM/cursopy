import numpy as np

escalar = np.array(55)
#esto es de un solo valor
print(escalar)
print(type(escalar))

vector = np.array([1, 2, 3, 4, 5])
print(vector)
print(type(vector))


#matris
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
print(type(matriz))


#es un cubo porque trae profundidad
tendsor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tendsor)
print(type(tendsor))

eye_matrix = np.eye(4)
print(eye_matrix)


aleatorio= np.random.random((3,3))
print(aleatorio)

aleatorio2= np.random.randint(1,10, size=(3,3))
print(aleatorio2)
print(aleatorio2[2,2])
print(aleatorio2[:,0:2]) #todas las filas de la columna 2
