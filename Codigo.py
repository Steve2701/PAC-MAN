import tkinter as tk
from threading import Thread
from tkinter import PhotoImage,NW
from PIL import Image, ImageTk
from tkinter.font import Font
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

#Fuentes
impact = "Impact"
arial="Arial"
timesnewroman="TimesNewRoman"



# Colores
grisoscuro = "#666666"




# Función para mostrar una ventana y ocultar la actual
def mostrar_ventana(ventana_a_mostrar):
    global ventana_actual
    usuario.delete(0, "end")
    canvasC1.delete("all")
    Pacmanletra = Font(family="PAC-FONT")
    canvasC1.create_text(249, 145, text="Ingrese su nombre para comenzar", font=(Pacmanletra , 20), fill=negro)
    ventana_actual.withdraw()  # Oculta la ventana actual
    ventana_a_mostrar.deiconify()  # Muestra la nueva ventana
    ventana_actual = ventana_a_mostrar


# Crear la ventana principal sin barra de título
ventana_principal = tk.Tk()
ventana_principal.geometry("600x500")
ventana_principal.configure(background="#3E5F8A")
ventana_principal.title("Proyecto programado #1")
canvasC1 = tk.Canvas(ventana_principal, width=500, height=350, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC1.place(x=300, y=245, anchor=tk.CENTER)
nombre_juego=tk.Label(ventana_principal, text="ROBOTS", font=(impact, 30), bg=navy, fg=celeste)
nombre_juego.place(x=228,y=5)



# Crear la nueva ventana sin barra de título
ventana_nueva = tk.Toplevel(ventana_principal)
ventana_nueva.geometry("650x650")
ventana_nueva.title("ROBOTS")
ventana_nueva.configure(background="#3E5F8A")
ventana_nueva.withdraw()  # Oculta la ventana nueva al principio
canvasC2 = tk.Canvas(ventana_nueva, width=554, height=554, borderwidth=0, highlightthickness=0, bg=gris)
canvasC2.place(x=330, y=300, anchor=tk.CENTER)

 


# Crear la nueva ventana para configuracion
ventana_config = tk.Toplevel(ventana_principal)
ventana_config.geometry("450x350")
ventana_config.title("Configuracion")
ventana_config.configure(background="#3E5F8A")
ventana_config.withdraw()
canvasC3 = tk.Canvas(ventana_config, width=400, height=300, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC3.place(x=225, y=175, anchor=tk.CENTER)
canvasC3.create_text(197, 20, text="Realice los ajustes iniciales de ROBOTS", font=(timesnewroman, 12), fill=negro)


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
# Procesar los datos y cargarlos en el Canvas
canvasC5.create_text(85, 20, text="Mejores jugadores de ROBOTS", anchor=tk.W,font=(impact, 14))




# Crear la nueva ventana para acerca de
ventana_acerca = tk.Toplevel(ventana_principal)
ventana_acerca.geometry("450x350")
ventana_acerca.title("Acerca de")
ventana_acerca.configure(background="#3E5F8A")
ventana_acerca.withdraw()
canvasC6 = tk.Canvas(ventana_acerca, width=400, height=300, borderwidth=0, highlightthickness=0, bg=celeste)
canvasC6.place(x=225, y=175, anchor=tk.CENTER)
canvasC6.create_text(197, 20, text=" ROBOTS ", font=(timesnewroman, 14), fill=negro)

canvasC6.create_text(198, 60, text="------  ITCR. Ingenieria en Computadores (CE)  ------", font=(timesnewroman, 13), fill=negro)
canvasC6.create_text(250,100, text=" Estudiante: Steven Solano Zuñiga", font=(timesnewroman, 13), fill=negro)
canvasC6.create_text(200, 135, text=" Carné: 2019077611", font=(timesnewroman, 13), fill=negro)
canvasC6.create_text(259, 170, text=" Curso: Introducción a la programación", font=(timesnewroman, 12), fill=negro)
canvasC6.create_text(239, 205, text=" Profesor: Jeff Schmidt Peralta", font=(timesnewroman, 13), fill=negro)
canvasC6.create_text(190, 290, text="     Producido en: CR                     Año:2023                     v1.0.0", font=(timesnewroman, 11), fill=negro)
canvasC6.create_text(200, 250, text="-----------------------------------------------------------------", font=(timesnewroman, 13), fill=negro)

 

# matriz = PhotoImage(file="matriz.png").zoom(2,2)
# canvasC2.create_image(0, 0, anchor="nw", image=matriz)



def comprobar_usuario(entry):
    nombre = str(entry.get()).strip()
    if not nombre:
        canvasC1.delete("all")
        canvasC1.create_text(247, 145, text="Error: Debe ingresar su nombre para continuar", font=("Impact", 13), fill=rojo)
    else:
        canvasC1.delete("all")
        mostrar_ventana(ventana_nueva)
        colocar_robots(0,int(robots.get()))





def cerrar_aplicacion():
    ventana_principal.quit()
    ventana_principal.destroy()
    reproducir_cancion("No")
    

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
# Agregar cantidad de robots
robots = tk.Entry(canvasC3, font=(arial, 12), justify="center", width=4)
robots.pack()
robots.place(x=120, y=130, anchor=tk.CENTER)
robots.insert(0, "5")
canvasC3.create_text(118, 155, text="Cantidad de robots", font=(impact, 13), fill=negro)
# Agregar cantidad de balas
balas = tk.Entry(canvasC3, font=(arial, 12), justify="center", width=4)
balas.pack()
balas.place(x=120, y=200, anchor=tk.CENTER)
balas.insert(0, "5")
canvasC3.create_text(120, 225, text="Cantidad de balas", font=(impact, 13), fill=negro)
# Agregar cantidad de teletransportaciones
telet = tk.Entry(canvasC3, font=(arial, 12), justify="center", width=4)
telet.pack()
telet.place(x=290, y=130, anchor=tk.CENTER)
telet.insert(0, "5")
canvasC3.create_text(290, 155, text="T-transportaciones", font=(impact, 13), fill=negro)
# Agregar cantidad de bombas
bombas = tk.Entry(canvasC3, font=(arial, 12), justify="center", width=4)
bombas.pack()
bombas.place(x=290, y=200, anchor=tk.CENTER)
bombas.insert(0, "5")
canvasC3.create_text(290, 225, text="Cantidad de bombas", font=(impact, 13), fill=negro)


# Botón para abrir una nueva ventana
boton_abrir = tk.Button(ventana_principal, text="Comenzar juego",font=(timesnewroman, 13),fg=blanco, command=lambda: comprobar_usuario(usuario),bg=verde)
boton_abrir.pack()
boton_abrir.place(x=297, y=460, anchor=tk.CENTER)

# Botón para configurar el juego y regresar 
configuracion = PhotoImage(file="").subsample(6,6)
boton_configurar = tk.Button(ventana_principal,image=configuracion,font=(timesnewroman, 10),fg=blanco, command=lambda: mostrar_ventana(ventana_config),bg=celeste)
boton_configurar.pack()
boton_configurar.place(x=528, y=91, anchor=tk.CENTER)


boton_regresar1 = tk.Button(canvasC3, image=regresar1,font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=celeste)
boton_regresar1.pack()
boton_regresar1.place(x=19, y=19, anchor=tk.CENTER)
boton_regresar2 = tk.Button(canvasC4, image=regresar1, text=" Inicio  ",font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=azulclaro)
boton_regresar2.pack()
boton_regresar2.place(x=48, y=280, anchor=tk.CENTER)
boton_regresar3 = tk.Button(canvasC5, image=regresar1,font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=celeste)
boton_regresar3.pack()
boton_regresar3.place(x=19, y=282, anchor=tk.CENTER)
boton_regresar4 = tk.Button(canvasC6, image=regresar1,font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=celeste)
boton_regresar4.pack()
boton_regresar4.place(x=19, y=19, anchor=tk.CENTER)


guardar = PhotoImage(file="").subsample(15, 15)
boton_guardar = tk.Button(canvasC3, image=guardar, text=" Guardar  ",font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: actualizar_valores(), bg=azulclaro)
boton_guardar.pack()
boton_guardar.place(x=195, y=280, anchor=tk.CENTER)
boton_si = tk.Button(canvasC3, text=" Si ",font=(timesnewroman, 10),fg=blanco, compound="left", command=lambda: reproducir_cancion("Si"), bg=verde)
boton_si.pack()
boton_si.place(x=250, y=70, anchor=tk.CENTER)
boton_no = tk.Button(canvasC3, text="No ",font=(timesnewroman, 10),fg=blanco, compound="left", command=lambda: reproducir_cancion("No"), bg=rojo)
boton_no.pack()
boton_no.place(x=280, y=70, anchor=tk.CENTER)
canvasC3.create_text(160, 70, text="¿Incluir musica?", font=(arial, 13), fill=negro)

# Botón para ayuda y regresar 
ayuda = PhotoImage(file="").subsample(3,3)
boton_ayuda = tk.Button(ventana_principal,image=ayuda,font=(timesnewroman, 10),fg=blanco, command=lambda: mostrar_ventana(ventana_help),bg=celeste)
boton_ayuda.pack()
boton_ayuda.place(x=533, y=404, anchor=tk.CENTER)

# Botón para salon de la fama
fama = PhotoImage(file="").subsample(6,6)
boton_fama = tk.Button(ventana_principal,compound="left",image=fama,text="Salon de la fama",font=(timesnewroman, 12),fg=blanco, command=lambda: mostrar_ventana(ventana_salon),bg=celesteoscuro)
boton_fama.pack()
boton_fama.place(x=198, y=320, anchor=tk.CENTER)

# Botón para Acerca de
acerca = PhotoImage(file="").subsample(12,12)
boton_acerca = tk.Button(ventana_principal,compound="left",image=acerca,text="  Acerca de ",font=(timesnewroman, 12),fg=blanco, command=lambda: mostrar_ventana(ventana_acerca),bg=celesteoscuro)
boton_acerca.pack()
boton_acerca.place(x=420, y=320, anchor=tk.CENTER)

# Botón exit
boton_exit = tk.Button(ventana_principal,text="Salir ",font=(timesnewroman, 12),fg=blanco, command=lambda: cerrar_aplicacion(),bg=rojo)
boton_exit.pack()
boton_exit.place(x=76, y=87, anchor=tk.CENTER)

# Calcular el centro de la pantalla para las nuevas ventanas
x_centro_nueva = (ancho_pantalla - 700) // 2
y_centro_nueva = (alto_pantalla - 700) // 2
x_centro_config = (ancho_pantalla - 450) // 2
y_centro_config = (alto_pantalla - 450) // 2
x_centro_ayuda = (ancho_pantalla - 450) // 2
y_centro_ayuda = (alto_pantalla - 450) // 2
x_centro_fama = (ancho_pantalla - 450) // 2
y_centro_fama = (alto_pantalla -450) // 2
x_centro_acerca = (ancho_pantalla - 450) // 2
y_centro_acerca = (alto_pantalla - 450) // 2


# Establecer la posición de las ventanas al centro
ventana_nueva.geometry(f"650x650+{x_centro_nueva}+{y_centro_nueva}")
ventana_config.geometry(f"450x350+{x_centro_config}+{y_centro_config}")
ventana_help.geometry(f"450x350+{x_centro_ayuda}+{y_centro_ayuda}")
ventana_salon.geometry(f"450x350+{x_centro_fama}+{y_centro_fama}")
ventana_acerca.geometry(f"450x350+{x_centro_acerca}+{y_centro_acerca}")


# Botón para regresar a la ventana principal desde la nueva ventana
atras = PhotoImage(file="").subsample(15, 15)
boton_regresar = tk.Button(ventana_nueva, image=atras, text=" Inicio  ",font=(timesnewroman, 13),fg=blanco, compound="left", command=lambda: mostrar_ventana(ventana_principal), bg=gris)
boton_regresar.pack()
boton_regresar.place(x=91, y=617, anchor=tk.CENTER)


ventana_actual = ventana_principal  # Inicialmente, la ventana actual es la principal

ventana_principal.mainloop()
