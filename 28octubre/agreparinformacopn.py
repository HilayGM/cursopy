import pandas as pd


datos = "online_retail.csv"
rd = pd.read_csv(datos)

  
rd["Total Venta"] = rd["Quantity"] * rd["UnitPrice"]

NVPais = rd["Country"].value_counts()
print("numero de ventas por pais", NVPais)


grupo_ventas = rd.groupby("Country")["Quantity"].sum()


general_ventas = rd.groupby("Country")["Quantity"].agg(
    ["mean","sum"]
)

inventario_pais = rd.groupby(["Country","StockCode"])["Quantity"].sum()



def total(grupo) : 
    return (grupo["Quantity"] * grupo["UnitPrice"]).sum()

revision_pais = rd.groupby("Country").apply(total)




#busqueda de informacion

ventas_paus = rd[rd["Country"] == "Germany"]


print("ventas de akemania ", ventas_paus)



ventas_pauss = rd[(rd["Country"] == "Germany")|(rd["Country"] == "united kingdom")]
print("ventas paises ", ventas_pauss)


#mVentas = rd[(rd["total_venta"] > 300 )& (rd["Country"] == "united kingdom")]
#omVentas = mVentas.sort_values(by = "total_venta", ascending=False)



#print("mayores ventas de reino unido\n ", mVentas)



rd["InvoiceDate"] = pd.to_datetime(rd["InvoiceDate"])
print(rd.info())



ventas_2011 = rd[rd["InvoiceDate"].dt.year == 2011]

print("total de ventas en el 2011 \n", ventas_2011)



ventas_2011["mes"] = ventas_2011["InvoiceDate"].dt.month
print(ventas_2011.head())

ventas_anuales = ventas_2011.pivot_table(
    values="Total Venta", 
    index= "Country",
    columns= "InvoiceDate",
    aggfunc= "mean"
)

print("ventas anuales 2011\n ", ventas_anuales)



