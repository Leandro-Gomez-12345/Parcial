import tkinter as tk
import imagenes as img
import calculos as cl

#--------------------Interfaz----------------------#
interfaz=tk.Tk()
interfaz.title("LUXURY CARS")
interfaz.geometry("1250x630")
interfaz.resizable(0,0)
interfaz.config(bg="gold", bd=10, relief= "ridge")

#------Funciones de movimiento--------
contador = 0
#------Regresar carro-----#
def regresar():
    Boton1=tk.Button(interfaz, text="<", bg="black", fg="white", font=("georgia", 20) ,command=resta_avanzar ) 
    Boton1.place(x= 75, y=350, width= 40, height=40)
    
#------Avanzar carro-----#
def avanzar():
    Boton1=tk.Button(interfaz, text=">", bg="black", fg="white", font=("georgia", 20) ,command=suma_avanzar ) 
    Boton1.place(x= 475, y=350, width= 40, height=40)

#----IMAGEN DERECHA
def suma_avanzar():
    global contador, imagen_siguiente
    contador += 1
    if contador > 3:
        contador = 0
        
    imagen_siguiente = img.conversor(marca[contador]["Imagen"], x=340, y=196)
    carro.config(image=imagen_siguiente)
    precio_.config(text=marca[contador]["Precio"])
    año_.config(text=marca[contador]["Año"])
    modelo_.config(text=marca[contador]["Modelo"])
    descripcion_.config(text=marca[contador]["Descripción"])
    
#----------------------------IMAGEN IZQUIERDA------------------------------#
def resta_avanzar():
    global contador, imagen_siguiente
    contador -= 1
    if contador < 0:
        contador = 3
        
    imagen_siguiente = img.conversor(marca[contador]["Imagen"], x=340, y=196)
    carro.config(image=imagen_siguiente)
    precio_.config(text=marca[contador]["Precio"])
    año_.config(text=marca[contador]["Año"])
    modelo_.config(text=marca[contador]["Modelo"])
    descripcion_.config(text=marca[contador]["Descripción"])

#----------------------Función para limpiar la pantalla----------------------#
def clean(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def informacion_comprador(con_interes):
    clean(interfaz)
    frame_blanco = tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    
    titulo1 = tk.Label(frame_blanco, text="- INFORMACION -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2 = tk.Label(frame_blanco, text="DEL COMPRADOR", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.29, anchor="center")
    
    nombre_label = tk.Label(frame_blanco, text="Ingrese su nombre completo:", font=("Georgia", 30), bg="white", fg="black")
    nombre_label.place(relx=0.05, rely=0.5)
    nombre_entry = tk.Entry(frame_blanco, font=("Georgia", 30))
    nombre_entry.place(relx=0.55, rely=0.5)
    
    cedula_label = tk.Label(frame_blanco, text="Ingrese su cedula:", font=("Georgia", 30), bg="white", fg="black")
    cedula_label.place(relx=0.05, rely=0.6)
    cedula_entry = tk.Entry(frame_blanco, font=("Georgia", 30))
    cedula_entry.place(relx=0.55, rely=0.6)
    
    aceptar_boton = tk.Button(frame_blanco, text="Guardar", font=("Georgia", 20), bg="black", fg="white", 
                              activebackground="white", activeforeground="black", cursor="hand2",
                              command=pag_compra_exitosa2 if con_interes else pag_compra_exitosa)
    aceptar_boton.place(relx=0.45, rely=0.8)
    regresar_boton = tk.Button(frame_blanco, text=" < ", bg="black", fg="white", font=("georgia", 20), command=pag_compra)
    regresar_boton.place(x=70, y=520)
    #Crear las funciones para que guarde la informacion
    
#----------------------Página de info----------------------#
def pag_info():
    global sistecredito_logo, addi_logo, su_logo

    micro_window = tk.Toplevel(interfaz)
    micro_window.title("Información")
    micro_window.geometry("600x600")
    micro_window.resizable(0, 0)
    micro_window.config(bg="black", bd=10, relief="ridge")
    
    # Creamos un frame dentro de la micro ventana para contener los widgets
    frame_interfaz = tk.Frame(micro_window, bg="white", width=580, height=580)
    frame_interfaz.place(relx=0.5, rely=0.5, anchor="center")
    
    info_addi=tk.Label(frame_interfaz, text="ADDI es un sistema de credito que te permite pagar tu carro en 12 meses, los primeros 3 meses no se pagan intereses. La tasa de interes: 4%", font=("Georgia", 15), bg="white", fg="black", wraplength=250)
    info_addi.place(relx=0.25, rely=0.3, anchor="center")

    info_sistecredito=tk.Label(frame_interfaz, text="SISTECREDITO es un sistema de credito que te permite pagar tu carro en 6 meses. La tasa de interes: 2.66%", font=("Georgia", 15), bg="white", fg="black", wraplength=250)
    info_sistecredito.place(relx=0.75, rely=0.3, anchor="center")

    info_su=tk.Label(frame_interfaz, text="SU es un sistema de credito que te permite pagar tu carro en 36 meses, los primeros 6 meses no se pagan intereses. La tasa de interes: 5%", font=("Georgia", 15), bg="white", fg="black", wraplength=250)
    info_su.place(relx=0.5, rely=0.75, anchor="center")

    # Cargamos las imágenes usando la función conversor y guardamos las referencias en la micro ventana
    micro_window.sistecredito_logo = img.conversor("siste.jpg", 150, 100)
    micro_window.addi_logo = img.conversor("addi.jpg", 150, 100)
    micro_window.su_logo = img.conversor("su+pay.png", 150, 100)
    
    # Creamos labels para mostrar las imágenes y los posicionamos en el frame
    label_siste = tk.Label(frame_interfaz, image=micro_window.sistecredito_logo)
    label_siste.place(relx=0.75, rely=0.08, anchor="center")
    
    label_addi = tk.Label(frame_interfaz, image=micro_window.addi_logo)
    label_addi.place(relx=0.25, rely=0.08, anchor="center")
    
    label_su = tk.Label(frame_interfaz, image=micro_window.su_logo)
    label_su.place(relx=0.5, rely=0.52, anchor="center")

#-------------Interfaz calculadora de credito-----------------
def calculadora_interfaz():
    global meses_entry, sistema_entry
    clean(interfaz)
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    
    titulo1 = tk.Label(frame_blanco, text="CALCULADORA", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="DE CREDITO", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.29, anchor="center")
    
    valor_label = tk.Label(frame_blanco, text="Valor total:", bg="white", font=("georgia", 20))
    valor_label.place(relx=0.1, rely=0.4)
    meses_label = tk.Label(frame_blanco, text="Meses a pagar:", bg="white", font=("georgia", 20))
    meses_label.place(relx=0.1, rely=0.5)
    sistema_label = tk.Label(frame_blanco, text="Sistema de credito:", bg="white", font=("georgia", 20))
    sistema_label.place(relx=0.1, rely=0.6)
    
    valor_calculado = tk.Label(frame_blanco, text=cl.total_pagar(marca[contador]["Precio"]), bg="white", font=("georgia", 20))
    valor_calculado.place(relx=0.4, rely=0.4)
    meses_entry = tk.Entry(frame_blanco)
    meses_entry.config(width=12, font=("georgia", 20))
    meses_entry.place(relx=0.4, rely=0.5)
    
    seleccion = tk.StringVar()
    seleccion.set("Seleccione el sistema")
    opciones = ["sistecredito", "addi", "su"]
    sistema_desplegable = tk.OptionMenu(frame_blanco, seleccion, *opciones)
    sistema_desplegable.config(bg="white", font=("georgia", 20))
    sistema_desplegable.place(relx=0.4, rely=0.6)
    
    i_boton = tk.Button(frame_blanco, text="i", font=("georgia", 12), bg="black", fg="white", command=pag_info)
    i_boton.place(relx=0.7, rely=0.6)
    calcular_boton = tk.Button(frame_blanco, text="Calcular",bg="black", fg="white", font=("georgia", 20),
                               command=lambda: si_no(cl.calculadora_credito(marca[contador]["Precio"], meses_entry.get(), seleccion.get())),
                               activebackground="white", activeforeground="black", cursor="hand2")                            
    calcular_boton.place(relx=0.45, rely=0.75)
    regresar_boton = tk.Button(frame_blanco, text=" < ", bg="black", fg="white", font=("georgia", 20), command=credito)
    regresar_boton.place(x=70, y=520)

#----------------------aceptar o rechazar credito----------------------#
def si_no(lista_con_informacion):
    if lista_con_informacion:
        global precio, meses, meses_entry, sistema_entry
        precio = round(lista_con_informacion[0])
        meses = round(lista_con_informacion[1])
        clean(interfaz)
        frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
        frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
        titulo1 = tk.Label(frame_blanco, text="- TU CREDITO -", font=("Georgia", 70), bg="white", fg="gold")
        titulo1.place(relx=0.5,rely=0.15, anchor="center")
        boton1= tk.Button(frame_blanco, text="Aceptar", bg="black", fg="white", font=("georgia", 20), 
                          command=lambda: informacion_comprador(True))
        boton1.place(relx=0.3, rely=0.92, anchor="center")
        boton2= tk.Button (frame_blanco, text="Rechazar", bg="black", fg="white", font=("georgia", 20), command=calculadora_interfaz)
        boton2.place(relx=0.7, rely=0.92, anchor="center")

        modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Georgia", 25), bg="white", fg="black")
        modelo_label.place(relx=0.14, rely=0.28)
        meses_a_pagar_label=tk.Label(frame_blanco, text="Meses a pagar:", font=("Georgia", 25), bg="white", fg="black")
        meses_a_pagar_label.place(relx=0.14, rely=0.38)
        precio_label=tk.Label(frame_blanco, text="Precio:", font=("Georgia", 25), bg="white", fg="black")
        precio_label.place(relx=0.14, rely=0.48)
        precio_intereses=tk.Label(frame_blanco, text="Precio con intereses:", font=("Georgia", 25), bg="white", fg="black")
        precio_intereses.place(relx=0.14, rely=0.58)    
        total_label=tk.Label(frame_blanco, text="Total:", font=("Georgia", 25), bg="white", fg="black")
        total_label.place(relx=0.14, rely=0.68)
        valor_pagar_mensual=tk.Label(frame_blanco, text="Valor a pagar mensual:", font=("Georgia", 25), bg="white", fg="black")
        valor_pagar_mensual.place(relx=0.14, rely=0.78)

        modelo_=tk.Label(frame_blanco, text=marca[contador]["Modelo"], font=("Georgia", 25), bg="white", fg="black")
        modelo_.place(relx=0.55, rely=0.28)
        meses_=tk.Label(frame_blanco, text=meses, font=("Georgia", 25), bg="white", fg="black")
        meses_.place(relx=0.55, rely=0.38)
        preci = tk.Label(frame_blanco, text=cl.total_pagar(marca[contador]["Precio"]), font=("Georgia", 25), bg="white", fg="black")
        preci.place(relx=0.55, rely=0.48)
        preci_interes = tk.Label(frame_blanco, text=precio, font=("Georgia", 25), bg="white", fg="black")
        preci_interes.place(relx=0.55, rely=0.58)
        meses_pagar = tk.Label(frame_blanco, text=round(precio / meses), font=("Georgia", 25), bg="white", fg="black")
        meses_pagar.place(relx=0.55, rely=0.78)

#------------ Credito --------
def credito():
    global sistecredito, addi, su, tarjeta
    clean(interfaz)
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")

    titulo1=tk.Label(frame_blanco, text="- SELECIONA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="TU CREDITO", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.29, anchor="center")
        
    sistecredito = img.conversor("sistecredito logo.png", 200, 100)
    label_siste = tk.Label(interfaz,image=sistecredito)
    label_siste.place(x=125, y=210)

    addi = img.conversor("addi logo.png", 200, 100)
    label_addi = tk.Label(interfaz,image=addi)
    label_addi.place(x=125, y=400)

    su = img.conversor("su+ logo.png", 200, 100)
    label_su = tk.Label(interfaz,image=su)
    label_su.place(x=450, y=300)

    tarjeta = img.conversor("tarjeta.jpg", 250, 100)
    label_tarjeta = tk.Label(interfaz,image=tarjeta)
    label_tarjeta.place(x=850, y=250)

    Boton1= tk.Button( interfaz, bg= "black", text= "Establecer \n Credito", font=("georgia", 15), fg="white", command=calculadora_interfaz,
                      activebackground="white", activeforeground="black", cursor="hand2") 
    Boton1.config(width=25, height=3)
    Boton1.place(x= 850, y= 425)
    
    regresar_boton = tk.Button(frame_blanco, text=" < ", bg="black", fg="white", font=("georgia", 20), command=pag_compra)
    regresar_boton.place(x=70, y=520)


#----------------------Página de compra----------------------#
def pag_compra():
    clean(interfaz)

    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- COMPRA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="TU CARRO", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.29, anchor="center")
    subrayado1=tk.Label(frame_blanco, text="________________________", font=("Georgia", 18), bg="white", fg="black", width=20, height=1)
    subrayado1.place(relx=0.25, rely=0.47, anchor="center")
    texto_confirma=tk.Label(frame_blanco, text="CONFIRMA TU COMPRA", font=("Georgia", 18), bg="white", fg="black")
    texto_confirma.place(relx=0.25, rely=0.45, anchor="center")
    texto_modelo=tk.Label(frame_blanco, text="Modelo:", font=("Georgia", 18), bg="white", fg="black")
    texto_modelo.place(relx=0.14, rely=0.52)
    texto_precio=tk.Label(frame_blanco, text="Precio:", font=("Georgia", 18), bg="white", fg="black")
    texto_precio.place(relx=0.14, rely=0.6)
    texto_papeleo=tk.Label(frame_blanco, text="Papeleo:", font=("Georgia", 18), bg="white", fg="black")
    texto_papeleo.place(relx=0.14, rely=0.68)
    subrayado2=tk.Label(frame_blanco, text="_________________________", font=("Georgia", 18), bg="white", fg="black", width=20, height=1)
    subrayado2.place(relx=0.135, rely=0.80)
    texto_impuesto=tk.Label(frame_blanco, text="Impuesto:", font=("Georgia", 18), bg="white", fg="black")
    texto_impuesto.place(relx=0.135, rely=0.76)
    texto_total=tk.Label(frame_blanco, text="Total:", font=("Georgia", 18), bg="white", fg="black")
    texto_total.place(relx=0.14, rely=0.88)

    contado_boton=tk.Button(frame_blanco, text="PAGAR DE CONTADO", font=("Georgia", 20), bg="black", fg="white", 
                            activebackground="white", activeforeground="black", cursor="hand2", 
                            command=lambda: informacion_comprador(False))
    contado_boton.place(relx=0.7, rely=0.52, anchor="center")
    hacer_credito_boton=tk.Button(frame_blanco, text="HACER UN CRÉDITO", font=("Georgia", 20), bg="black", fg="white", activebackground="white", activeforeground="black", cursor="hand2", command= credito)
    hacer_credito_boton.place(relx=0.7, rely=0.82, anchor="center")
    
    modelo_ = tk.Label(frame_blanco, text=marca[contador]["Modelo"], font=("Georgia", 18), bg="white", fg="black")
    modelo_.place(relx=0.3, rely=0.52)
    precio_ = tk.Label(frame_blanco, text=marca[contador]["Precio"], font=("Georgia", 18), bg="white", fg="black")
    precio_.place(relx=0.3, rely=0.6)
    papeleo_ = tk.Label(frame_blanco, text="$5.000.000", font=("Georgia", 18), bg="white", fg="black") 
    papeleo_.place(relx=0.3, rely=0.68)
    impuesto_ = tk.Label(frame_blanco, text="1,9%", font=("Georgia", 18), bg="white", fg="black")
    impuesto_.place(relx=0.3, rely=0.76)
    total_ = tk.Label(frame_blanco, text=cl.total_pagar(marca[contador]["Precio"]), font=("Georgia", 18), bg="white", fg="black")
    total_.place(relx=0.3, rely=0.88)
    
#----------------------Páginas de compra exitosa----------------------#
def pag_compra_exitosa2():
    clean(interfaz)
    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1100, height=480)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- TU COMPRA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="HA SIDO EXITOSA", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.32, anchor="center")
    texto_modelo=tk.Label(frame_blanco, text="Modelo:", font=("Georgia", 25), bg="white", fg="black")
    texto_modelo.place(relx=0.14, rely=0.42)
    texto_precio_total=tk.Label(frame_blanco, text="Precio Total:", font=("Georgia", 25), bg="white", fg="black")
    texto_precio_total.place(relx=0.14, rely=0.52)
    texto_cancelado=tk.Label(frame_blanco, text="Abonado:", font=("Georgia", 25), bg="white", fg="black")
    texto_cancelado.place(relx=0.14, rely=0.62)
    cancelado_=tk.Label(frame_blanco, text=round(precio / meses), font=("Georgia", 25), bg="white", fg="black")
    cancelado_.place(relx=0.4, rely=0.62)
    texto_gracias=tk.Label(frame_blanco, text="GRACIAS POR CONFIAR EN", font=("Georgia", 40), bg="white", fg="black")
    texto_gracias.place(relx=0.5, rely=0.9, anchor="center")
    titulo1=tk.Label(interfaz, text="- LUXURY -", font=("Georgia", 25), bg="yellow", fg="black") 
    titulo1.place(relx=0.5,rely=0.92, anchor="center")
    titulo2=tk.Label(interfaz, text="  CARS  ", font=("Georgia", 15), bg="black", fg="yellow") 
    titulo2.place(relx=0.5,rely=0.97, anchor="center")
    
    modelo_ = tk.Label(interfaz, text=marca[contador]["Modelo"], font=("Georgia", 25), bg="white", fg="black")
    modelo_.place(relx=0.4, rely=0.44)
    precio_ = tk.Label(interfaz,text=precio, font=("Georgia", 25), bg="white", fg="black")
    precio_.place(relx=0.4, rely=0.52)

def pag_compra_exitosa():
    clean(interfaz)
    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1100, height=480)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- TU COMPRA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="HA SIDO EXITOSA", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.32, anchor="center")
    texto_modelo=tk.Label(frame_blanco, text="Modelo:", font=("Georgia", 25), bg="white", fg="black")
    texto_modelo.place(relx=0.14, rely=0.42)
    texto_precio_total=tk.Label(frame_blanco, text="Precio Total:", font=("Georgia", 25), bg="white", fg="black")
    texto_precio_total.place(relx=0.14, rely=0.52)
    texto_cancelado=tk.Label(frame_blanco, text="Cancelado:", font=("Georgia", 25), bg="white", fg="black")
    texto_cancelado.place(relx=0.14, rely=0.62)
    cancelado_=tk.Label(frame_blanco, text=cl.total_pagar(marca[contador]["Precio"]), font=("Georgia", 25), bg="white", fg="black")
    cancelado_.place(relx=0.4, rely=0.62)
    texto_gracias=tk.Label(frame_blanco, text="GRACIAS POR CONFIAR EN", font=("Georgia", 40), bg="white", fg="black")
    texto_gracias.place(relx=0.5, rely=0.9, anchor="center")
    titulo1=tk.Label(interfaz, text="- LUXURY -", font=("Georgia", 25), bg="yellow", fg="black") 
    titulo1.place(relx=0.5,rely=0.92, anchor="center")
    titulo2=tk.Label(interfaz, text="  CARS  ", font=("Georgia", 15), bg="black", fg="yellow") 
    titulo2.place(relx=0.5,rely=0.97, anchor="center")
    
    modelo_ = tk.Label(interfaz, text=marca[contador]["Modelo"], font=("Georgia", 25), bg="white", fg="black")
    modelo_.place(relx=0.4, rely=0.44)
    precio_ = tk.Label(interfaz,text=cl.total_pagar(marca[contador]["Precio"]), font=("Georgia", 25), bg="white", fg="black")
    precio_.place(relx=0.4, rely=0.52)


#----------------------Página de Lamborghini----------------------#
def pag_lamborghini():
    global carro, marca, precio_, descripcion_, año_, modelo_
    clean(interfaz)
    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- LAMBORGHINI -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="black", fg="gold", activebackground="gold", activeforeground="black", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.25, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Lamborguini")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    
    precio_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    precio_.place(relx=0.7, rely=0.4)
    
    año_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    año_.place(relx=0.7, rely=0.5)
    
    modelo_ = tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    modelo_.place(relx=0.7, rely=0.6)

    descripcion_= tk.Label(frame_blanco, font=("Times New Roman", 15), bg="white", fg="black", wraplength=350)
    descripcion_.place(relx=0.7, rely=0.7)

    avanzar()
    regresar()
    suma_avanzar()

#----------------------Página de Ferrari----------------------#
def pag_ferrari():
    global carro, marca, precio_, descripcion_, año_, modelo_
    clean(interfaz)
    interfaz.config(bg="#EB1B00")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")

    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- FERRARI -", font=("Georgia", 80), bg="white", fg="#DBD407")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="#EB1B00", fg="white", activebackground="white", activeforeground="#EB1B00", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.25, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Ferrari")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    
    precio_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    precio_.place(relx=0.7, rely=0.4)
    
    año_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    año_.place(relx=0.7, rely=0.5)
    
    modelo_ = tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    modelo_.place(relx=0.7, rely=0.6)

    descripcion_= tk.Label(frame_blanco, font=("Times New Roman", 15), bg="white", fg="black", wraplength=350)
    descripcion_.place(relx=0.7, rely=0.7)
    
    avanzar()
    regresar()
    suma_avanzar()

#----------------------Página de Mercedes----------------------#
def pag_mercedes():
    global carro, marca, precio_, descripcion_, año_, modelo_
    clean(interfaz)
    interfaz.config(bg="#929292")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- MERCEDES -", font=("Georgia", 80), bg="white", fg="#929292")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="#929292", fg="white", activebackground="white", activeforeground="#929292", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.25, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Mercedes")
    
    precio_=tk.Label(frame_blanco, text=marca[contador]["Precio"], font=("Times New Roman", 30), bg="white", fg="black")
    precio_.place(relx=0.7, rely=0.4)

    descripcion_=tk.Label(frame_blanco, text=marca[contador]["Descripción"], font=("Times New Roman", 15), bg="white", fg="black", wraplength=350)
    descripcion_.place(relx=0.7, rely=0.7)

    año_=tk.Label(frame_blanco, text=marca[contador]["Año"], font=("Times New Roman", 30), bg="white", fg="black")
    año_.place(relx=0.7, rely=0.5)

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    
    precio_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    precio_.place(relx=0.7, rely=0.4)
    
    año_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    año_.place(relx=0.7, rely=0.5)
    
    modelo_ = tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    modelo_.place(relx=0.7, rely=0.6)

    descripcion_= tk.Label(frame_blanco, font=("Times New Roman", 15), bg="white", fg="black", wraplength=350)
    descripcion_.place(relx=0.7, rely=0.7)
    
    avanzar()
    regresar()
    suma_avanzar()

#----------------------Página de BMW----------------------#
def pag_bmw():
    global carro, marca, precio_, descripcion_, año_, modelo_
    clean(interfaz)
    interfaz.config(bg="#1786EB")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- BMW -", font=("Georgia", 80), bg="white", fg="#1786EB")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="#1786EB", fg="white", activebackground="white", activeforeground="#1786EB", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.25, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Bmw")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)

    precio_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    precio_.place(relx=0.7, rely=0.4)
    
    año_= tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    año_.place(relx=0.7, rely=0.5)
    
    modelo_ = tk.Label(frame_blanco, font=("Times New Roman", 30), bg="white", fg="black")
    modelo_.place(relx=0.7, rely=0.6)

    descripcion_= tk.Label(frame_blanco, font=("Times New Roman", 15), bg="white", fg="black", wraplength=350)
    descripcion_.place(relx=0.7, rely=0.7)

    avanzar()
    regresar()
    suma_avanzar() # Hace el moviento al principio


#----------------------Interfaz principal----------------------#
def menu():
    global interfaz
    clean(interfaz) 
    interfaz.config(bg="yellow")
    frametitulo=tk.Frame(interfaz, bg="black", width=1240, height=620)
    frametitulo.pack()
    titulo1=tk.Label(frametitulo, text="- LUXURY -", font=("Georgia", 80), bg="yellow", fg="black") 
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frametitulo, text="  CARS  ", font=("Georgia", 50), bg="black", fg="yellow") 
    titulo2.place(relx=0.5,rely=0.285, anchor="center")

    escoger_marca=tk.Label(frametitulo, text="- ESCOGE TU MARCA -", font=("Georgia", 30), bg="black", fg="yellow")
    escoger_marca.place(relx=0.5, rely=0.43, anchor="center")

    boton_bmw=tk.Button(frametitulo, text="BMW", font=("Georgia", 20), bg="white", fg="black", width=10, height=1, activebackground="#1786EB", activeforeground="white", cursor="hand2", command=pag_bmw)
    boton_bmw.place(relx=0.15, rely=0.85, anchor="center")

    boton_mercedes=tk.Button(frametitulo, text="Mercedes", font=("Georgia", 20), bg="white", fg="black", width=10, height=1, activebackground="black", activeforeground="white", cursor="hand2", command=pag_mercedes)
    boton_mercedes.place(relx=0.385, rely=0.85, anchor="center")

    boton_ferrari=tk.Button(frametitulo, text="Ferrari", font=("Georgia", 20), bg="white", fg="black", width=10, height=1, activebackground="#EB1B00", activeforeground="white", cursor="hand2", command=pag_ferrari)
    boton_ferrari.place(relx=0.615, rely=0.85, anchor="center")

    boton_lamborghini=tk.Button(frametitulo, text="Lamborghini", font=("Georgia", 20), bg="white", fg="black", width=10, height=1,  activebackground="black", activeforeground="#EBBD36", cursor="hand2", command=pag_lamborghini)
    boton_lamborghini.place(relx=0.85, rely=0.85, anchor="center")

    #------logo de carros-----
    logo_bmw = img.conversor("BMW logo.jpg", 150,150)
    label_logo_bmw = tk.Label(interfaz, image=logo_bmw)
    label_logo_bmw.place(relx=0.15, rely=0.65, anchor="center")

    logo_mercedes = img.conversor("logo mercedes.jpg", 150,150)
    label_logo_mecedes = tk.Label(interfaz, image=logo_mercedes)
    label_logo_mecedes.place(relx=0.385, rely=0.65, anchor="center")

    logo_ferrari = img.conversor("ferrari logo.png", 150,150)
    label_logo_ferrari = tk.Label(interfaz, image=logo_ferrari)
    label_logo_ferrari.place(relx=0.615, rely=0.65, anchor="center")

    logo_lamborguni = img.conversor("lamborghini logo.jpg", 150,150)
    label_logo_lamborguni = tk.Label(interfaz, image=logo_lamborguni)
    label_logo_lamborguni.place(relx=0.85, rely=0.65, anchor="center")

    interfaz.mainloop()

menu()

