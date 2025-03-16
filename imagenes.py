from PIL import Image, ImageTk

# ---- Abre la imagen y luego ajusta la resolucion -----
def conversor(ubicacion, x, y):
    imagen = Image.open(ubicacion)
    imagen = imagen.resize((x, y))
    foto = ImageTk.PhotoImage(imagen)
    return(foto)
