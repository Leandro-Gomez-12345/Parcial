from tkinter import messagebox

#-----Listas con diccionarios de las marcas de carros-----
inventario_BMW=[
            {"Precio": 172000000 ,
            "Año": "2024",
            "Modelo":"BMW218i",
            "Descripción": "El BMW 218i Gran Coupé tiene un motor de gasolina de 6 cilindros en línea BMW M TwinPower Turbo.",
            "Imagen" : "218i.jpg"},

            {"Precio": 800000000 ,
            "Año": "2025",
            "Modelo":"BMW I7 M70",
            "Descripción": "Aceleración de 0 a 100 km/h en 3,7 segundos Emisiones de CO2: 0 g/km Consumo de energía combinado: 20.8-23.7 kWh/100km (WLTP)",
            "Imagen" : "i7 M70.jpg"},

            {"Precio": 700000000,
            "Año": "2025",
            "Modelo":"BMW M340i",
            "Descripción": "BMW M3 Competition Sedán y BMW M340i xDrive Sedán. La gama BMW Serie 3 Sedán M combina poderosas proporciones y un llamativo diseño de tres volúmenes y cuatro puertas con la deportividad característica de M.",
            "Imagen" : "M340i.jpg"},

            {"Precio": 750000000 ,
            "Año": "2019",
            "Modelo":" BMW I8",
            "Descripción": "Motor tricilíndrico turboalimentado de 1,5 litros Motor eléctrico síncrono BMW eDrive Potencia total de 369 CV",
            "Imagen" : "I8.jpg"},
            ]

inventario_mercedes=[
            {"Precio": 185000000 ,
            "Año": "2014",
            "Modelo": "Clase A 250",
            "Descripción": "Motor de gasolina de 1.991 cc Potencia de 221 hp Torque de 350 Nm Aceleración de 0 a 100 km/h en 6,3 segundos Velocidad máxima de 250 km/",
            "Imagen" : "Mercedez clase A 250.jpg"},

            {"Precio": 377900000,
            "Año": "2025",
            "Modelo":"Clase C AMG",
            "Descripción": "El modelo más reciente, el Mercedes-AMG C 63 S E Performance, cuenta con un innovador sistema híbrido enchufable que combina un motor de 4 cilindros turbo de 2.0 litros con un motor eléctrico. Esta configuración produce una potencia impresionante de 680 CV y un par motor de 1.020 Nm.",
            "Imagen" : "Mercedez clase C AMG.jpg"},

            {"Precio": 234000000,
            "Año": "2024",
            "Modelo":"Clase C Coupé",
            "Descripción": "Motor de gasolina de 1.991 cc Potencia de 258 hp Torque de 400 Nm Aceleración de 0 a 100 km/h en 6,0 segundos Velocidad máxima de 250 km/h",
            "Imagen" : "Mercedez clase C coupe.jpg"},

            {"Precio": 1150000000 ,
            "Año": "2025",
            "Modelo":"Clase S",
            "Descripción": "Motor de gasolina V8 biturbo de 3.982 cc Potencia de 503 hp Torque de 700 Nm Aceleración de 0 a 100 km/h en 4,4 segundos Velocidad máxima de 250 km/h",
            "Imagen" : "Mercedez clase S.jpg"},
            ]

inventario_ferrari=[
            {"Precio": 1200000000 ,
            "Año": "2020",
            "Modelo":"Roma",
            "Descripción": "Motor V8 turbo de 3.855 cc Potencia de 620 CV a 7.500 rpm Torque de 760 Nm entre 3.000 y 5.750 rpm Aceleración de 0 a 100 km/h en 3,4 segundos Velocidad máxima de 320 km/h",
            "Imagen" : "Ferrari Roma.jpg"},

            {"Precio": 1500000000,
            "Año": "2019",
            "Modelo":"F8 Tributo",
            "Descripción": "Motor V8 biturbo de 3.902 cc Potencia de 720 CV a 8.000 rpm Torque de 770 Nm a 3.250 rpm Aceleración de 0 a 100 km/h en 2,9 segundos Velocidad máxima de 340 km/h",
            "Imagen" : "Ferrari F8 Tributo.jpg"},

            {"Precio": 2500000000,
            "Año": "2020",
            "Modelo":"SF90 Stradale",
            "Descripción": "Motor V8 biturbo de 3.990 cc + 3 motores eléctricos Potencia total de 1000 CV (780 CV del motor de combustión + 220 CV de los motores eléctricos) Torque de 800 Nm a 6.000 rpm (motor de combustión) Aceleración de 0 a 100 km/h en 2,5 segundos Velocidad máxima de 340 km/h",
            "Imagen" : "Ferrari SF90 Stradale.jpg"},

            {"Precio": 10000000000 ,
            "Año": "2013",
            "Modelo":"LaFerrari",
            "Descripción": "Motor V12 de 6.262 cc + sistema híbrido HY-KERS Potencia total de 963 CV (800 CV del motor de combustión + 163 CV del motor eléctrico) Torque de 900 Nm (total combinado) Aceleración de 0 a 100 km/h en menos de 3 segundos Velocidad máxima superior a 350 km/h",
            "Imagen" : "Ferrari LaFerrari.jpg"},
            ]

inventario_lamborghini=[
            {"Precio": 1200000000 ,
            "Año": "2014",
            "Modelo":"Huracan",
            "Descripción": "Motor V10 atmosférico de 5.204 cc Potencia de 640 CV a 8.000 rpm Torque de 600 Nm a 6.500 rpm Aceleración de 0 a 100 km/h en 2,9 segundos Velocidad máxima superior a 325 km/h",
            "Imagen" : "Huracan.jpg"},

            {"Precio": 1500000000,
            "Año": "2018",
            "Modelo":"Urus",
            "Descripción": "Motor V8 biturbo de 3.996 cc Potencia de 670 CV a 6.000 rpm Torque de 850 Nm a 2.300-4.500 rpm Aceleración de 0 a 100 km/h en 3,5 segundos Velocidad máxima de 305 km/h",
            "Imagen" : "Urus.jpg"},

            {"Precio": 2000000000,
            "Año": "2011",
            "Modelo":"Aventador",
            "Descripción": "Motor V12 atmosférico de 6.498 cc Potencia de 780 CV a 8.500 rpm Torque de 720 Nm a 6.750 rpm Aceleración de 0 a 100 km/h en 2,8 segundos Velocidad máxima de 355 km/h",
            "Imagen" : "Aventador.jpg"},

            {"Precio": 5000000000 ,
            "Año": "2020",
            "Modelo":"Sian",
            "Descripción": "Motor V12 de 6.498 cc + sistema híbrido ligero de 48 V Potencia total de 819 CV (785 CV del motor de combustión + 34 CV del motor eléctrico) Torque de 720 Nm a 6.750 rpm Aceleración de 0 a 100 km/h en 2,8 segundos Velocidad máxima superior a 350 km/h",
            "Imagen" : "Sian.jpg"},
            ]

#------Recibe la marca del vehiculo y retorna la lista de la marca
def verificador_marca(marca):
    if marca == 'Bmw':
        return inventario_BMW
    elif marca == 'Mercedes':
        return inventario_mercedes
    elif marca == 'Ferrari':
        return inventario_ferrari
    else:
        return inventario_lamborghini
    
def total_pagar(precio_carro):
    return round(precio_carro + 5000000 + (precio_carro * 0.019))

def calculadora_credito(precio_carro, meses, sistema):
    #Verifica que el usuario coloco datos validos
    if meses and (sistema != "Seleccione el sistema"):
        precio_carro = total_pagar(precio_carro)
        meses = int(meses)

        if meses <= 0:
            messagebox.showwarning("Meses no validos", "No puedes ingresar menos de un mes. ")
            return []
        
        if sistema == "sistecredito":
            if meses > 6:
                messagebox.showwarning("Tiempo limite superado", "Cambia los meses a pagar, el tiempo maximo de Sistecredito es de 6 meses. ")
                return []
            else:
                tasa_interes = 0.0266
                return [(precio_carro * (1 + (tasa_interes/12)) ** meses), meses]
            
        elif sistema == "addi":
            if meses > 12:
                messagebox.showwarning("Tiempo limite superado", "Cambia los meses a pagar, el tiempo maximo de Addi es de 12 meses. ")
                return []
            elif meses > 3:
                tasa_interes = 0.04
                return [(precio_carro * (1 + (tasa_interes/12)) ** meses - 3), meses]
            else:
                return [precio_carro, meses]
            
        else:
            if meses > 36:
                messagebox.showwarning("Tiempo limite superado", "Cambia los meses a pagar, el tiempo maximo de Su es de 36 meses. ")
                return []
            elif meses > 6:
                tasa_interes = 0.05
                return [(precio_carro * (1 + (tasa_interes/12)) ** meses - 6), meses]
            else:
                return [precio_carro, meses]
    
    else:
        messagebox.showwarning("Informacion insuficiente", "Termina de completar los datos para poder calcular el interes. ")
        return []

def separador_comas(numero):
    numero = str(numero)
    digitos = len(numero)
    separados = ''
    
    while digitos > 3:
        separados = '.' + numero[digitos-3 : digitos] + separados
        digitos -= 3
    separados = numero[:digitos] + separados
    return separados + "   COP"
