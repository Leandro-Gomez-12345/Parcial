import pandas as pd

"""Para el parcial, deberán entonces desarrollar un archivo de factura para cada compra realizada en formato txt, 
que incluya la información del comprador, el sistema de créditos, las cuotas a pagar y el vehículo comprado. 
Además de ello, cada compra deberá ser registrada en un archivo de excel utilizando la librería Pandas, 
y se deberá crear otro documento informando la cantidad de dinero que se espera obtener tras cada mes
dadas las cuotas que cada cliente haya pactado pagar. """

def factura(diccionario, interes):
    with open("factura "+ diccionario["Nombre"] +".txt", "w", encoding="utf-8") as archivo:
        archivo.write("     LUXURY CARS     \n")
        archivo.write("-------------------------------\n")
        archivo.write("Nombre: "+ diccionario["Nombre"] +"\n")
        archivo.write("Cedula: "+ diccionario["Cedula"] +"\n")
        archivo.write("Vehiculo: "+ diccionario["Carro"] +"\n")
        if interes:
            archivo.write("Sistemas de credito: "+ diccionario["Entidad"] +'\n')
        archivo.write("Precio: "+ str(diccionario["Precio"]) +'\n')
        if interes:
            archivo.write("Valor de cuota: "+ str(diccionario["Cuota"]) +'\n')
            archivo.write("Cuotas a pagar: "+ str(diccionario["Meses"]) +'\n')
        archivo.write("Total: "+ str(diccionario["Total"]) +'\n')
        archivo.write("¡GRACIAS POR TU COMPRA "+ diccionario["Nombre"] + "!")
        
    excel(diccionario, interes)

def excel(diccionario, interes):
    try:
        datos_nuevos = pd.DataFrame({"Nombre":[diccionario["Nombre"]], "Cedula":[diccionario["Cedula"]], 
        "Vehiculo":[diccionario["Carro"]], "Precio":[diccionario["Precio"]], "Valor de cuota":[diccionario["Cuota"] if interes else 0], 
        "Cuotas a pagar":[diccionario["Meses"] if interes else 0], "Total":[diccionario["Total"]]})
        datos_actuales = pd.read_excel("compras.xlsx")
        datos = pd.concat([datos_actuales, datos_nuevos], ignore_index=True)
        datos.to_excel("compras.xlsx", index=False)
    except:
        datos_nuevos.to_excel("compras.xlsx", index=False)


"""Falta crear una funcion que cree un archivo de las ganancias mensules que gana LUXURY CARS por las cuotas de los usuarios"""