import tkinter as tk
from threading import Thread
from tkinter import PhotoImage,NW
#from PIL import Image, ImageTk
import pygame as py
import time
import sys
import math
import random


#Colores
verde="#008F39"
navy = "#2B3467"
celeste = "#99B4D1"
celesteoscuro = "#296d98"
amarillo = "#FCFFE7"
rojo = "#EB455F"
gris = "#b5b5b5"
grisoscuro = "#666666"
azul = "#3E5F8A"
negro = "#000000"
blanco = "#FFFFFF"
azulclaro="#256d7b"
grisoscuro = "#666666"

#Fuentes
impact = "Impact"
arial="Arial"
timesnewroman="TimesNewRoman"

# Funcion para mostrar ventanas
def mostrar_ventana(ventana_a_mostrar):
    global ventana_actual
    usuario.delete(0, "end")
    canvasC1.delete("all")
    canvasC1.create_text(249, 145, text="Ingrese su nombre para comenzar", font=("Impact", 13), fill=negro)
    ventana_actual.withdraw()  # Oculta la ventana actual
    ventana_a_mostrar.deiconify()  # Muestra la nueva ventana
    ventana_actual = ventana_a_mostrar

def subir_foto(canvas):
    foto = Image.open("Foto.jpg")
    foto = foto.resize((100, 130), Image.BILINEAR)
    foto_tk = ImageTk.PhotoImage(foto)
    canvas.create_image(15, 90, anchor=tk.NW, image=foto_tk)
    canvas.imagen_foto = foto_tk  # Almacenar la imagen en el atributo del canvas

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.geometry("600x500")
ventana_principal.configure(background="#3E5F8A")
ventana_principal.title("Proyecto programado #2")
canvasC1 = tk.Canvas(ventana_principal, width=500, height=350, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC1.place(x=300, y=245, anchor=tk.CENTER)
nombre_juego=tk.Label(ventana_principal, text="PAC-MAN", font=(impact, 30), bg=navy, fg=celeste)
nombre_juego.place(x=228,y=5)

# Crear la nueva ventana para el juego
ventana_nueva = tk.Toplevel(ventana_principal)
ventana_nueva.geometry("940x720")
ventana_nueva.title("PAC-MAN")
ventana_nueva.configure(background="#3E5F8A")
ventana_nueva.withdraw()  # Oculta la ventana nueva al principio
canvasC2 = tk.Canvas(ventana_nueva, width=779, height=699, borderwidth=0, highlightthickness=0, bg=negro)
canvasC2.place(x=470, y=355, anchor=tk.CENTER)

# Crear la nueva ventana para ayuda
ventana_help = tk.Toplevel(ventana_principal)
ventana_help.geometry("450x350")
ventana_help.title("Ayuda")
ventana_help.configure(background="#3E5F8A")
ventana_help.withdraw()
canvasC4 = tk.Canvas(ventana_help, width=400, height=300, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC4.place(x=225, y=175, anchor=tk.CENTER)
canvasC4.create_text(197, 20, text=" ", font=(timesnewroman, 12), fill=negro)

# Crear la nueva ventana para salon de la fama
ventana_salon = tk.Toplevel(ventana_principal)
ventana_salon.geometry("450x350")
ventana_salon.title("Salon de la fama")
ventana_salon.configure(background="#3E5F8A")
ventana_salon.withdraw()
canvasC5 = tk.Canvas(ventana_salon, width=400, height=300, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC5.place(x=225, y=175, anchor=tk.CENTER)
canvasC5.create_text(197, 20, text=" ", font=(timesnewroman, 12), fill=negro)

# Crear la nueva ventana para acerca de
ventana_acerca = tk.Toplevel(ventana_principal)
ventana_acerca.geometry("450x350")
ventana_acerca.title("Acerca de")
ventana_acerca.configure(background="#3E5F8A")
ventana_acerca.withdraw()
canvasC6 = tk.Canvas(ventana_acerca, width=400, height=300, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC6.place(x=225, y=175, anchor=tk.CENTER)
#subir_foto(canvasC6)
#subir_bandera(canvasC6)
#canvasC6.create_text(250,100, text=" Estudiante: Steven Solano Zuñiga", font=(timesnewroman, 13), fill=negro)
#canvasC6.create_text(200, 135, text=" Carné: 2019077611", font=(timesnewroman, 13), fill=negro)
#canvasC6.create_text(259, 170, text=" Curso: Introducción a la programación", font=(timesnewroman, 12), fill=negro)
#canvasC6.create_text(239, 205, text=" Profesor: Jeff Schmidt Peralta", font=(timesnewroman, 13), fill=negro)
#canvasC6.create_text(190, 290, text="     Producido en: CR                     Año:2023                     v1.0.0", font=(timesnewroman, 11), fill=negro)
#canvasC6.create_text(200, 250, text="-----------------------------------------------------------------", font=(timesnewroman, 13), fill=negro)

# Funcion para iniciar juego con nombre de usuario
def comprobar_usuario(entry):
    nombre = str(entry.get()).strip()
    if not nombre:
        canvasC1.delete("all")
        canvasC1.create_text(247, 145, text="Error: Debe ingresar su nombre para continuar", font=("Impact", 13), fill=rojo)
    else:
        canvasC1.delete("all")
        mostrar_ventana(ventana_nueva)
        #Funciones especificas del juego

# Funcion para cerrar el juego
def cerrar_aplicacion():
    ventana_principal.quit()
    ventana_principal.destroy()

canvasC1.delete("all")
canvasC1.create_text(249, 145, text="Ingrese su nombre para comenzar", font=("Impact", 13), fill=negro)

# Calcular el centro de la pantalla
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()
x_centro = (ancho_pantalla - 700) // 2  # El ancho de la ventana principal es 700
y_centro = (alto_pantalla - 600) // 2   # El alto de la ventana principal es 600

# Establecer la posición de la ventana principal en el centro
ventana_principal.geometry(f"600x500+{x_centro}+{y_centro}")

# Agregar nombre
usuario = tk.Entry(ventana_principal, font=(impact, 12), justify="center")
usuario.pack()
usuario.place(x=303, y=190, anchor=tk.CENTER)

# Botón para abrir una nueva ventana
boton_abrir = tk.Button(ventana_principal, text="Comenzar juego",font=(timesnewroman, 13),fg=blanco, command=lambda: comprobar_usuario(usuario),bg=verde)
boton_abrir.pack()
boton_abrir.place(x=297, y=460, anchor=tk.CENTER)

# Botón para ayuda y regresar 
ayuda = PhotoImage(file="ayuda.png").subsample(3,3)
boton_ayuda = tk.Button(ventana_principal,image=ayuda,font=(timesnewroman, 10),fg=blanco, command=lambda: mostrar_ventana(ventana_help),bg=celeste)
boton_ayuda.pack()
boton_ayuda.place(x=533, y=404, anchor=tk.CENTER)

# Botón para salon de la fama
fama = PhotoImage(file="fama.png").subsample(6,6)
boton_fama = tk.Button(ventana_principal,compound="left",image=fama,text="Salon de la fama",font=(timesnewroman, 12),fg=blanco, command=lambda: mostrar_ventana(ventana_salon),bg=celesteoscuro)
boton_fama.pack()
boton_fama.place(x=198, y=320, anchor=tk.CENTER)

# Botón para Acerca de
acerca = PhotoImage(file="acerca.png").subsample(12,12)
boton_acerca = tk.Button(ventana_principal,compound="left",image=acerca,text="  Acerca de ",font=(timesnewroman, 12),fg=blanco, command=lambda: mostrar_ventana(ventana_acerca),bg=celesteoscuro)
boton_acerca.pack()
boton_acerca.place(x=420, y=320, anchor=tk.CENTER)

# Botón exit
boton_exit = tk.Button(ventana_principal,text="Salir ",font=(timesnewroman, 12),fg=blanco, command=lambda: cerrar_aplicacion(),bg=rojo)
boton_exit.pack()
boton_exit.place(x=76, y=87, anchor=tk.CENTER)

# Calcular el centro de la pantalla para las nuevas ventanas
x_centro_nueva = (ancho_pantalla - 940) // 2
y_centro_nueva = (alto_pantalla - 750) // 2
x_centro_ayuda = (ancho_pantalla - 450) // 2
y_centro_ayuda = (alto_pantalla - 450) // 2
x_centro_fama = (ancho_pantalla - 450) // 2
y_centro_fama = (alto_pantalla -450) // 2
x_centro_acerca = (ancho_pantalla - 450) // 2
y_centro_acerca = (alto_pantalla - 450) // 2


# Establecer la posición de las ventanas al centro
ventana_nueva.geometry(f"940x720+{x_centro_nueva}+{y_centro_nueva}")
ventana_help.geometry(f"450x350+{x_centro_ayuda}+{y_centro_ayuda}")
ventana_salon.geometry(f"450x350+{x_centro_fama}+{y_centro_fama}")
ventana_acerca.geometry(f"450x350+{x_centro_acerca}+{y_centro_acerca}")

# Botón para regresar a la ventana principal desde la nueva ventana
atras = PhotoImage(file="atras.png").subsample(15, 15)
boton_regresar = tk.Button(ventana_nueva, image=atras, text="",font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=gris)
boton_regresar.pack()
boton_regresar.place(x=36, y=600, anchor=tk.CENTER)


# Botones para regresar a la pantalla inicial
regresar1 = PhotoImage(file="atras.png").subsample(15, 15)
boton_regresar2 = tk.Button(canvasC4, image=regresar1, text=" Inicio  ",font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=azulclaro)
boton_regresar2.pack()
boton_regresar2.place(x=48, y=280, anchor=tk.CENTER)
boton_regresar3 = tk.Button(canvasC5, image=regresar1,font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=celeste)
boton_regresar3.pack()
boton_regresar3.place(x=19, y=282, anchor=tk.CENTER)
boton_regresar4 = tk.Button(canvasC6, image=regresar1,font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=celeste)
boton_regresar4.pack()
boton_regresar4.place(x=19, y=19, anchor=tk.CENTER)


matriz=[]
matriz.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])																	
matriz.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])																	
matriz.append([0,0,9,9,9,9,9,9,9,9,0,0,0,9,9,9,9,9,9,9,9,9,9,9,9,9,0,0,0,0,9,9,9,9,9,9,9,9,0,0])																	
matriz.append([0,0,9,2,1,1,1,1,1,9,0,0,0,9,1,1,1,1,1,2,1,1,1,1,1,9,0,0,0,0,9,1,1,1,1,1,2,9,0,0])																	
matriz.append([0,0,9,1,9,9,9,9,1,9,0,0,0,9,1,9,9,9,9,1,9,9,9,9,1,9,0,0,0,0,9,1,9,9,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,0,0,9,1,9,0,0,0,9,1,9,0,0,9,1,9,0,0,9,1,9,0,0,0,0,9,1,9,0,0,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,0,0,9,1,9,9,9,9,9,1,9,9,9,9,1,9,9,9,9,1,9,9,9,9,9,9,1,9,0,0,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,0,0,9,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,9,0,0,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,9,9,1,9,9,9,9,9,1,9,9,9,9,9,9,9,9,9,9,1,9,9,9,9,9,1,9,9,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,1,3,1,1,1,9,0,0,0,9,1,9,0,0,0,0,0,0,0,0,9,1,9,0,0,0,9,1,1,1,1,1,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,9,9,1,9,0,9,9,9,1,9,9,9,9,9,9,9,9,9,9,1,9,9,9,0,9,1,9,9,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,0,0,9,1,9,0,9,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,9,0,9,1,9,0,0,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,0,9,1,9,0,9,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,9,0,9,1,9,0,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,1,1,0,9,1,9,0,9,1,9,0,0,0,0,9,9,9,0,0,0,0,0,9,1,9,0,9,1,9,0,1,1,3,9,0,0])																	
matriz.append([0,0,9,9,9,9,0,9,1,9,0,9,1,9,0,0,0,0,0,0,0,0,0,0,0,0,9,1,9,0,9,1,9,0,9,9,9,9,0,0])																	
matriz.append([0,0,0,0,0,0,0,9,1,9,0,9,1,9,0,9,9,9,9,9,9,9,9,9,9,0,9,1,9,0,9,1,9,0,0,0,0,0,0,0])																	
matriz.append([9,9,9,9,9,9,9,9,1,9,9,9,1,9,0,9,9,9,9,9,9,9,9,9,9,0,9,1,9,9,9,1,9,9,9,9,9,9,9,9])																	
matriz.append([1,1,3,1,1,1,1,1,1,1,1,1,2,9,0,9,9,9,9,9,9,9,9,9,9,0,9,2,1,1,1,1,1,1,1,1,1,3,1,1])																	
matriz.append([9,9,9,9,9,9,9,9,1,9,9,9,1,9,0,0,0,0,0,0,0,0,0,0,0,0,9,1,9,9,9,1,9,9,9,9,9,9,9,9])																	
matriz.append([0,0,0,0,0,0,0,9,1,9,0,9,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,9,0,9,1,9,0,0,0,0,0,0,0])																	
matriz.append([0,0,9,9,9,9,9,9,1,9,0,9,1,1,1,1,1,1,1,2,1,1,1,1,3,1,1,1,9,0,9,1,9,9,9,9,9,9,0,0])																	
matriz.append([0,0,9,1,1,1,1,1,1,9,0,9,1,9,9,9,9,9,9,1,9,9,9,9,9,9,9,1,9,0,9,1,1,1,1,1,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,9,9,1,9,0,9,1,9,0,0,0,0,9,1,9,0,0,0,0,0,9,1,9,0,9,1,9,9,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,0,0,9,1,9,0,9,1,9,0,0,0,0,9,1,9,0,0,0,0,0,9,1,9,0,9,1,9,0,0,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,9,9,1,9,9,9,1,9,9,9,9,9,9,1,9,9,9,9,9,9,9,1,9,9,9,1,9,9,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,9,9,9,9,9,9,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,9,9,9,9,9,9,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,0,0,0,0,0,0,9,1,9,0,0,0,0,0,0,0,0,0,0,0,0,9,1,9,0,0,0,0,0,0,9,1,9,0,0])																	
matriz.append([0,0,9,1,9,9,0,0,9,9,9,9,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,9,9,9,9,0,0,9,9,1,9,0,0])																	
matriz.append([0,0,9,1,1,9,0,0,9,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9,0,0,9,1,1,9,0,0])																	
matriz.append([0,0,9,9,1,9,0,0,9,1,9,9,9,9,9,1,9,9,9,9,9,9,9,9,1,9,9,9,9,9,1,9,0,0,9,1,9,9,0,0])																	
matriz.append([0,0,0,9,1,9,0,0,9,1,9,0,0,0,9,1,9,0,0,0,0,0,0,9,1,9,0,0,0,9,1,9,0,0,9,1,9,0,0,0])																	
matriz.append([0,0,0,9,1,9,9,9,9,1,9,9,9,9,9,1,9,9,9,0,0,9,9,9,1,9,9,9,9,9,1,9,9,9,9,1,9,0,0,0])																	
matriz.append([0,0,0,9,2,1,1,1,1,1,1,1,1,1,1,1,1,1,9,0,0,9,1,1,1,1,3,1,1,1,1,1,1,1,1,2,9,0,0,0])																	
matriz.append([0,0,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,0,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,0,0,0])																	
matriz.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])																	



# Funcion para dibujar matriz (posible inspector)
def dibujar_matriz(matriz):
    ancho = canvasC2.winfo_reqwidth()
    alto = canvasC2.winfo_reqheight()
    
    # Calcula el ancho y alto de una celda en el canvas
    ancho_celda = ancho // len(matriz[0])
    alto_celda = alto // len(matriz)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            x = (j+1) * ancho_celda
            y = (i+1)* alto_celda
            valor = str(matriz[i][j])
            if valor=="1":
                canvasC2.create_text(x, y, text=valor, font=("Arial", 12), fill=verde)
            elif valor=="2":
                canvasC2.create_text(x, y, text=valor, font=("Arial", 12), fill=rojo)
            elif valor=="3":
                canvasC2.create_text(x, y, text=valor, font=("Arial", 12), fill=amarillo)
            elif valor=="9":
                canvasC2.create_text(x, y, text=valor, font=("Arial", 12), fill=gris)
            else:
                canvasC2.create_text(x, y, text=valor, font=("Arial", 12), fill=azul)


# Dibujar la matriz en el canvasC2
dibujar_matriz(matriz)


pacman = tk.PhotoImage(file="pacman.png").subsample(21, 22)
pacman_img = canvasC2.create_image(389, 349, anchor=tk.NW, image=pacman)

##ESTA ES UNA IDEA PARA COMPARAR LA POSICION DEL PACMAN CON LA MATRIZ####################
def obtener_texto(x, y):
    elementos_superpuestos = canvasC2.find_overlapping(x, y, x, y)
    for elemento in elementos_superpuestos:
        if canvasC2.type(elemento) == "text":
            texto = canvasC2.itemcget(elemento, "text")
            return texto
    return None

# Obtener el texto en la posición (100, 100)
x = 2
y = 2
texto = obtener_texto(x, y)
print (texto)

if texto is not None:
    print("Texto en la posición ({}, {}): {}".format(x, y, texto))
else:
    print("No se encontró texto en la posición ({}, {})".format(x, y))
##########################################################################################


ventana_actual = ventana_principal  # Inicialmente, la ventana actual es la principal

ventana_principal.mainloop()


