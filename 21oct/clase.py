import pandas as pd


dato = [1,2,3,4,5]

datalist = pd.DataFrame(dato)

print(datalist)



datos2=[[1,"samuel",32],[2,"jaime",25],[3,"ana",28]]
datalist2 = pd.DataFrame(datos2, columns=["id","nombre","edad"])
print(datalist2)



datos3 = [{
    "id":1,
    "Nombre":"samuel",
    "edad":30
}]

diccionario = pd.DataFrame(datos3)
print(diccionario)










