import pandas as pd 

"""Para el parcial, deberán entonces desarrollar un archivo de factura para cada compra realizada en formato txt, 
que incluya la información del comprador, el sistema de créditos, las cuotas a pagar y el vehículo comprado. 
Además de ello, cada compra deberá ser registrada en un archivo de excel utilizando la librería Pandas, 
y se deberá crear otro documento informando la cantidad de dinero que se espera obtener tras cada mes
dadas las cuotas que cada cliente haya pactado pagar. """

def factura(diccionario, interes):
    with open("factura "+diccionario["Nombre"]+".txt", "w") as archivo:
        archivo.write("     LUXURY CARS     \n")
        archivo.write("-------------------------------\n")
        archivo.write("Nombre: "+ diccionario["Nombre"] +"\n")
        archivo.write("Cedula: "+ diccionario["Cedula"] +"\n")
        archivo.write("Vehiculo: "+ diccionario["Carro"] +"\n")
        if interes:
            archivo.write("Sistemas de credito: "+ diccionario["Entidad"] +'\n')
        archivo.write("Precio:"+ str(diccionario["Precio"]) +'\n')
        if interes:
            archivo.write("Cuota:"+ str(diccionario["Cuota"]) +'\n')
        archivo.write("Total:"+ str(diccionario["Total"]) +'\n')
        archivo.write("|GRACIAS POR TU COMPRA "+ diccionario["Nombre"] + "!")
        """tabla=pd.DataFrame({"Nombre":[nombre], "Cedula":[cedula], "Vehiculo":[ marca[contador]["Modelo"]], "Precio":[str(precio_)], "Cuota":[str(round(precio / meses))], "Total":[str(precio)]})
        tabla.to_excel("datos.xlsx", index=False)"""

#def excel():
