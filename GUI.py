import customtkinter as ctk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
import tkinter as tk
import time
from matplotlib.figure import Figure

# Función para obtener la selección del primer menú de la pestaña "Tiempo Continuo - Punto 1"
def seleccion_boton1_c1():
    seleccion_opcion_b1 = opcion1_tiempo_continuo_punto1.get()
    return seleccion_opcion_b1

# Función para obtener la selección del segundo menú de la pestaña "Tiempo Continuo - Punto 1"
def seleccion_boton2_c1():
    seleccion_opcion_b2 = opcion2_tiempo_continuo_punto1.get()
    return seleccion_opcion_b2

#------------------------------------------------------------------------------------------

def seleccion_menu_d1():
    seleccion_menu_b1 = menu1_tiempo_discreto_punto1.get()
    return seleccion_menu_b1

# Función para obtener la selección del segundo menú de la pestaña "Tiempo Discreto - Punto 1"
def seleccion_menu_d2():
    seleccion_menu_b2 = menu2_tiempo_discreto_punto1.get()
    return seleccion_menu_b2

#------------------------------------------------------------------------------------------

def seleccion_menu_c2():
    seleccion_menu_b11 = menu1_tiempo_continuo_punto2.get()
    return seleccion_menu_b11
#------------------------------------------------------------------------------------------

# Asignación para elegir pestaña y tiempo
punto = None
tipo_convolucion = None
senal_continua_1 = None #(1 - 6, señal desplazada)
senal_continua_2 = None #(1 - 6, señal fija)

#------------------------------------------------------------------------------------------

# Pestaña 1: Función para asignar un nuevo valor a senal_continua_1 y senal_continua_2 basado en las selecciones de los menús

def eleccion_continuo1():
    
    global senal_continua_1
    global senal_continua_2    
    global punto    
    global tipo_convolucion    

    seleccion_menu1 = seleccion_boton1_c1()
    seleccion_menu2 = seleccion_boton2_c1()
    
    if seleccion_menu1 == "Señal A" and seleccion_menu2 == "Señal A":
        senal_continua_1 = 1
        senal_continua_2 = 1
    elif seleccion_menu1 == "Señal A" and seleccion_menu2 == "Señal B":
        senal_continua_1 = 1
        senal_continua_2 = 2
    elif seleccion_menu1 == "Señal A" and seleccion_menu2 == "Señal C":
        senal_continua_1 = 1
        senal_continua_2 = 3
    elif seleccion_menu1 == "Señal A" and seleccion_menu2 == "Señal D":
        senal_continua_1 = 1
        senal_continua_2 = 4
    elif seleccion_menu1 == "Señal A" and seleccion_menu2 == "Señal E":
        senal_continua_1 = 1
        senal_continua_2 = 5
    elif seleccion_menu1 == "Señal A" and seleccion_menu2 == "Señal F":
        senal_continua_1 = 1
        senal_continua_2 = 6
    elif seleccion_menu1 == "Señal B" and seleccion_menu2 == "Señal A":
        senal_continua_1 = 2
        senal_continua_2 = 1
    elif seleccion_menu1 == "Señal B" and seleccion_menu2 == "Señal B":
        senal_continua_1 = 2
        senal_continua_2 = 2
    elif seleccion_menu1 == "Señal B" and seleccion_menu2 == "Señal C":
        senal_continua_1 = 2
        senal_continua_2 = 3
    elif seleccion_menu1 == "Señal B" and seleccion_menu2 == "Señal D":
        senal_continua_1 = 2
        senal_continua_2 = 4
    elif seleccion_menu1 == "Señal B" and seleccion_menu2 == "Señal E":
        senal_continua_1 = 2
        senal_continua_2 = 5
    elif seleccion_menu1 == "Señal B" and seleccion_menu2 == "Señal F":
        senal_continua_1 = 2
        senal_continua_2 = 6
    elif seleccion_menu1 == "Señal C" and seleccion_menu2 == "Señal A":
        senal_continua_1 = 3
        senal_continua_2 = 1
    elif seleccion_menu1 == "Señal C" and seleccion_menu2 == "Señal B":
        senal_continua_1 = 3
        senal_continua_2 = 2
    elif seleccion_menu1 == "Señal C" and seleccion_menu2 == "Señal C":
        senal_continua_1 = 3
        senal_continua_2 = 3
    elif seleccion_menu1 == "Señal C" and seleccion_menu2 == "Señal D":
        senal_continua_1 = 3
        senal_continua_2 = 4
    elif seleccion_menu1 == "Señal C" and seleccion_menu2 == "Señal E":
        senal_continua_1 = 3
        senal_continua_2 = 5
    elif seleccion_menu1 == "Señal C" and seleccion_menu2 == "Señal F":
        senal_continua_1 = 3
        senal_continua_2 = 6
    elif seleccion_menu1 == "Señal D" and seleccion_menu2 == "Señal A":
        senal_continua_1 = 4
        senal_continua_2 = 1
    elif seleccion_menu1 == "Señal D" and seleccion_menu2 == "Señal B":
        senal_continua_1 = 4
        senal_continua_2 = 2
    elif seleccion_menu1 == "Señal D" and seleccion_menu2 == "Señal C":
        senal_continua_1 = 4
        senal_continua_2 = 3
    elif seleccion_menu1 == "Señal D" and seleccion_menu2 == "Señal D":
        senal_continua_1 = 4
        senal_continua_2 = 4
    elif seleccion_menu1 == "Señal D" and seleccion_menu2 == "Señal E":
        senal_continua_1 = 4
        senal_continua_2 = 5
    elif seleccion_menu1 == "Señal D" and seleccion_menu2 == "Señal F":
        senal_continua_1 = 4
        senal_continua_2 = 6
    elif seleccion_menu1 == "Señal E" and seleccion_menu2 == "Señal A":
        senal_continua_1 = 5
        senal_continua_2 = 1
    elif seleccion_menu1 == "Señal E" and seleccion_menu2 == "Señal B":
        senal_continua_1 = 5
        senal_continua_2 = 2
    elif seleccion_menu1 == "Señal E" and seleccion_menu2 == "Señal C":
        senal_continua_1 = 5
        senal_continua_2 = 3
    elif seleccion_menu1 == "Señal E" and seleccion_menu2 == "Señal D":
        senal_continua_1 = 5
        senal_continua_2 = 4
    elif seleccion_menu1 == "Señal E" and seleccion_menu2 == "Señal E":
        senal_continua_1 = 5
        senal_continua_2 = 5
    elif seleccion_menu1 == "Señal E" and seleccion_menu2 == "Señal F":
        senal_continua_1 = 5
        senal_continua_2 = 6
    elif seleccion_menu1 == "Señal F" and seleccion_menu2 == "Señal A":
        senal_continua_1 = 6
        senal_continua_2 = 1
    elif seleccion_menu1 == "Señal F" and seleccion_menu2 == "Señal B":
        senal_continua_1 = 6
        senal_continua_2 = 2
    elif seleccion_menu1 == "Señal F" and seleccion_menu2 == "Señal C":
        senal_continua_1 = 6
        senal_continua_2 = 3
    elif seleccion_menu1 == "Señal F" and seleccion_menu2 == "Señal D":
        senal_continua_1 = 6
        senal_continua_2 = 4
    elif seleccion_menu1 == "Señal F" and seleccion_menu2 == "Señal E":
        senal_continua_1 = 6
        senal_continua_2 = 5
    elif seleccion_menu1 == "Señal F" and seleccion_menu2 == "Señal F":
        senal_continua_1 = 6
        senal_continua_2 = 6

    fig, axs = plt.subplots(2, 2, figsize=(8, 6))

    Delta = 0.001

    #Definir señal 1
    if senal_continua_1 == 1:
        t_1 = np.round(np.arange(-1, 1 + Delta, Delta)/Delta)*Delta
        x_t = np.zeros(len(t_1))
        x_t[1:-1] = np.ones(len(t_1)-2)

        limite_x_inf_1 = -2
        limite_x_sup_1 = 2
        limite_y_inf_1 = -1
        limite_y_sup_1 = 2
    elif senal_continua_1 == 2:
        t_1_1 = np.round(np.arange(1, 3, Delta)/Delta)*Delta
        x_t_1 = np.zeros(len(t_1_1))
        x_t_1[1:len(x_t_1)] = np.ones(len(t_1_1)-1)
        t_1_2 = np.round(np.arange(3, 4 + Delta, Delta)/Delta)*Delta
        x_t_2 = np.zeros(len(t_1_2))
        x_t_2[0:len(x_t_2)-1] = 2*np.ones(len(t_1_2)-1)
        t_1 = np.append(t_1_1,t_1_2)
        x_t = np.append(x_t_1,x_t_2)

        limite_x_inf_1 = -1
        limite_x_sup_1 = 5
        limite_y_inf_1 = -1
        limite_y_sup_1 = 3
    elif senal_continua_1 == 3:
        t_1_1 = np.round(np.arange(-2, 0, Delta)/Delta)*Delta
        x_t_1 = np.zeros(len(t_1_1))
        x_t_1[1:len(x_t_1)] = -1*np.ones(len(t_1_1)-1)
        t_1_2 = np.round(np.arange(0, 2 + Delta, Delta)/Delta)*Delta
        x_t_2 = np.zeros(len(t_1_2))
        x_t_2[0:len(x_t_2)-1] = np.ones(len(t_1_2)-1)
        t_1 = np.append(t_1_1,t_1_2)
        x_t = np.append(x_t_1,x_t_2)

        limite_x_inf_1 = -3
        limite_x_sup_1 = 3
        limite_y_inf_1 = -2
        limite_y_sup_1 = 2
    elif senal_continua_1 == 4:
        t_1 = np.round(np.arange(-1, 1 + Delta, Delta)/Delta)*Delta
        x_t = np.zeros(len(t_1))
        x_t[1:-1] = t_1[1:-1]

        limite_x_inf_1 = -2
        limite_x_sup_1 = 2
        limite_y_inf_1 = -2
        limite_y_sup_1 = 2
    elif senal_continua_1 == 5:
        t_1_1 = np.round(np.arange(-4, -2, Delta)/Delta)*Delta
        x_t_1 = np.zeros(len(t_1_1))
        x_t_1[1:len(x_t_1)] = (1/2)*t_1_1[1:len(t_1_1)] + 2
        t_1_2 = np.round(np.arange(-2, 0, Delta)/Delta)*Delta
        x_t_2 = np.ones(len(t_1_2))
        t_1_3 = np.round(np.arange(0, 1 + Delta, Delta)/Delta)*Delta
        x_t_3 = np.zeros(len(t_1_3))
        x_t_3[0:len(x_t_3)-1] = -1*t_1_3[0:len(t_1_3)-1] + 1
        t_1 = np.concatenate((t_1_1,t_1_2,t_1_3))
        x_t = np.concatenate((x_t_1,x_t_2,x_t_3))

        limite_x_inf_1 = -5
        limite_x_sup_1 = 2
        limite_y_inf_1 = -1
        limite_y_sup_1 = 3
    elif senal_continua_1 == 6:
        t_1 = np.round(np.arange(0, 1 + Delta, Delta)/Delta)*Delta
        x_t = np.zeros(len(t_1))
        x_t[1:-1] = np.exp(-1*t_1[1:-1])

        limite_x_inf_1 = -1
        limite_x_sup_1 = 2
        limite_y_inf_1 = -1
        limite_y_sup_1 = 2

    if senal_continua_2 == 1:
        t_2 = np.round(np.arange(-1, 1 + Delta, Delta)/Delta)*Delta
        h_t = np.zeros(len(t_2))
        h_t[1:-1] = np.ones(len(t_2)-2)

        limxi2 = -2
        limxs2 = 2
        limyi2 = -1
        limys2 = 2
    elif senal_continua_2 == 2:
        t_2_1 = np.round(np.arange(1, 3, Delta)/Delta)*Delta
        h_t_1 = np.zeros(len(t_2_1))
        h_t_1[1:len(h_t_1)] = np.ones(len(t_2_1)-1)
        t_2_2 = np.round(np.arange(3, 4 + Delta, Delta)/Delta)*Delta
        h_t_2 = np.zeros(len(t_2_2))
        h_t_2[0:len(h_t_2)-1] = 2*np.ones(len(t_2_2)-1)
        t_2 = np.append(t_2_1,t_2_2)
        h_t = np.append(h_t_1,h_t_2)

        limxi2 = -1
        limxs2 = 5
        limyi2 = -1
        limys2 = 3
    elif senal_continua_2 == 3:
        t_2_1 = np.round(np.arange(-2, 0, Delta)/Delta)*Delta
        h_t_1 = np.zeros(len(t_2_1))
        h_t_1[1:len(h_t_1)] = -1*np.ones(len(t_2_1)-1)
        t_2_2 = np.round(np.arange(0, 2 + Delta, Delta)/Delta)*Delta
        h_t_2 = np.zeros(len(t_2_2))
        h_t_2[0:len(h_t_2)-1] = np.ones(len(t_2_2)-1)
        t_2 = np.append(t_2_1,t_2_2)
        h_t = np.append(h_t_1,h_t_2)

        limxi2 = -3
        limxs2 = 3
        limyi2 = -2
        limys2 = 2
    elif senal_continua_2 == 4:
        t_2 = np.round(np.arange(-1, 1 + Delta, Delta)/Delta)*Delta
        h_t = np.zeros(len(t_2))
        h_t[1:-1] = t_2[1:-1]

        limxi2 = -2
        limxs2 = 2
        limyi2 = -2
        limys2 = 2
    elif senal_continua_2 == 5:
        t_2_1 = np.round(np.arange(-4, -2, Delta)/Delta)*Delta
        h_t_1 = np.zeros(len(t_2_1))
        h_t_1[1:len(h_t_1)] = (1/2)*t_2_1[1:len(t_2_1)] + 2
        t_2_2 = np.round(np.arange(-2, 0, Delta)/Delta)*Delta
        h_t_2 = np.ones(len(t_2_2))
        t_2_3 = np.round(np.arange(0, 1 + Delta, Delta)/Delta)*Delta
        h_t_3 = np.zeros(len(t_2_3))
        h_t_3[0:len(h_t_3)-1] = -1*t_2_3[0:len(t_2_3)-1] + 1
        t_2 = np.concatenate((t_2_1,t_2_2,t_2_3))
        h_t = np.concatenate((h_t_1,h_t_2,h_t_3))

        limxi2 = -5
        limxs2 = 2
        limyi2 = -1
        limys2 = 3
    elif senal_continua_2 == 6:
        t_2 = np.round(np.arange(0, 1 + Delta, Delta)/Delta)*Delta
        h_t = np.zeros(len(t_2))
        h_t[1:-1] = np.exp(-1*t_2[1:-1])

        limxi2 = -1
        limxs2 = 2
        limyi2 = -1
        limys2 = 2

    # Graficar las señales originales

    axs[0,0].axhline(0, color='black', linewidth=1)
    axs[0,0].axvline(0, color='black', linewidth=1) 
    axs[0,0].plot(t_1, x_t, color = "purple")
    axs[0,0].grid()
    axs[0,0].set_title('Señal Desplazada')
    axs[0,0].set_xlabel('t')
    axs[0,0].set_ylabel('x(t)')
    axs[0,0].set_xlim(limite_x_inf_1, limite_x_sup_1)
    axs[0,0].set_ylim(limite_y_inf_1, limite_y_sup_1)

    axs[0,1].axhline(0, color='black', linewidth=1)
    axs[0,1].axvline(0, color='black', linewidth=1)
    axs[0,1].plot(t_2, h_t, color = 'orange')
    axs[0,1].grid()
    axs[0,1].set_title('Señal Fija')
    axs[0,1].set_xlabel('t')
    axs[0,1].set_ylabel('h(t)')
    axs[0,1].set_xlim(limxi2, limxs2)
    axs[0,1].set_ylim(limyi2, limys2)

    # Arreglar señal 1
    # Reflejar la señal
    t_x_inversa = []

    for i in reversed(t_1):
        t_x_inversa.append(-i)

    x_n_inversa = []

    for i in reversed(x_t):
        x_n_inversa.append(i)

    # Mover la señal
    
    t_x_desplazada = t_x_inversa - (max(t_x_inversa) - min(t_2) + 1)

    # Calcular los límites del nuevo vector n
    t_final_min = min(np.append(t_x_desplazada, t_2))
    t_final_max = max(np.append(t_x_desplazada, t_2))

    # Crear el nuevo vector n
    t_final = np.round(np.arange(t_final_min, t_final_max + (len(x_t)*Delta) + 1 + Delta, Delta)/Delta)*Delta

    # Encontrar puntos iniciales y finales de la señal en el nuevo vector n
    punto_inicial_x = 0
    punto_final_x = 0

    for i in range(len(t_final)):
        if t_final[i] == min(t_x_desplazada):
            punto_inicial_x = i
            break

    for i in range(len(t_final)):
        if t_final[i] == max(t_x_desplazada):
            punto_final_x = i
            break
            

    # Crear nuevo vector x1[n]
    x_t_final = np.zeros(len(t_final))

    for i in range(len(t_final)):
        if i < punto_inicial_x:
            x_t_final[i] = 0
        elif punto_inicial_x <= i <= punto_final_x:
            x_t_final[i] = x_n_inversa[i - punto_inicial_x]
        else:
            x_t_final[i] = 0

    #Arreglar señal 2

    # Encontrar puntos iniciales y finales de la señal en el nuevo vector n
    punto_inicial_h = 0
    punto_final_h = 0

    for i in range(len(t_final)):
        if t_final[i] == min(t_2):
            punto_inicial_h = i
            break

    for i in range(len(t_final)):
        if t_final[i] == max(t_2):
            punto_final_h = i
            break

    # Crear nuevo vector x2[n]
    h_t_final = np.zeros(len(t_final))

    for i in range(len(t_final)):
        if i < punto_inicial_h:
            h_t_final[i] = 0
        elif punto_inicial_h <= i <= punto_final_h:
            h_t_final[i] = h_t[i - punto_inicial_h]
        else:
            h_t_final[i] = 0

    # Crear variables de la convolución

    t_convolucion = t_final
    senal_desplazada_convolucion = x_t_final
    senal_quieta_convolucion = h_t_final
    senal_quieta = h_t
    senal_desplazada = x_t

    # Crear variables propias de la convolución
    
    senal_desplazada_convolucion_m = []
    convolucion = []
    t_convolucion_array = []

    # Definir el paso de la convolución

    if len(t_convolucion)<10500:
        step = 100
    else:
        step = 200

    # Proceso de convolución
    
    for i in range(0,len(x_t)+len(h_t) + round(2/Delta),step):
        axs[1,0].axhline(0, color='black', linewidth=1)
        axs[1,0].axvline(0, color='black', linewidth=1) 
        axs[1,0].plot(t_convolucion, senal_quieta_convolucion, color = 'orange')
        axs[1,0].set_title('Proceso de convolución')
        axs[1,0].set_xlabel('t')
        axs[1,0].set_ylabel('y(t)')
        axs[1,0].grid()
        axs[1,0].set_xlim(min(t_convolucion), max(t_convolucion))
        axs[1,0].set_ylim(min(np.append(senal_desplazada_convolucion, senal_quieta_convolucion)) - 1, max(np.append(senal_desplazada_convolucion, senal_quieta_convolucion)) + 1)

        senal_desplazada_convolucion_m = np.concatenate((np.zeros(i), senal_desplazada_convolucion[0:len(senal_desplazada)], np.zeros(len(t_convolucion) - len(senal_desplazada) - i)))

        axs[1,0].plot(t_convolucion, senal_desplazada_convolucion_m, color = 'purple')

        t_convolucion_array.append(i*Delta + min(t_1) + min(t_2) - 1)
        convolucion.append(np.sum(senal_desplazada_convolucion_m * senal_quieta_convolucion)*Delta)
        
        axs[1,1].axhline(0, color='black', linewidth=1)
        axs[1,1].axvline(0, color='black', linewidth=1) 
        axs[1,1].plot(t_convolucion_array, convolucion, color = 'orange')
        axs[1,1].set_title('Resultado de la convolución')
        axs[1,1].set_xlabel('t')
        axs[1,1].set_ylabel('y(t)')
        axs[1,1].grid()
        axs[1,1].set_xlim(min(t_convolucion_array)-1, max(t_convolucion_array)+1)
        axs[1,1].set_ylim(min(convolucion)-1, max(convolucion)+1)

        plt.tight_layout()
        plt.pause(0.005*Delta)

        if i != (len(x_t)+len(h_t) + round(2/Delta) - 1)-(len(x_t)+len(h_t) + round(2/Delta) - 1)%step:
            axs[1,0].cla() 
            axs[1,1].cla()
    plt.tight_layout()
    plt.show()
#------------------------------------------------------------------------------------------

# Pestaña 2: Función para asignar un nuevo valor a senal_continua_1 y senal_continua_2 basado en las selecciones de los menús

def eleccion_discreto1():
    
    global senal_discreta
    global senal_desplazar  
    global punto
    global tipo_convolucion

    seleccion_opcion_1 = seleccion_menu_d1()
    seleccion_opcion_2 = seleccion_menu_d2()
    
    if seleccion_opcion_1 == "Punto A" and seleccion_opcion_2 == "Desplazar x[n]":
        senal_discreta = 1
        senal_desplazar = 1
    elif seleccion_opcion_1 == "Punto A" and seleccion_opcion_2 == "Desplazar h[n]":
        senal_discreta = 1
        senal_desplazar = 2
    if seleccion_opcion_1 == "Punto B" and seleccion_opcion_2 == "Desplazar x[n]":
        senal_discreta = 2
        senal_desplazar = 1
    elif seleccion_opcion_1 == "Punto B" and seleccion_opcion_2 == "Desplazar h[n]":
        senal_discreta = 2
        senal_desplazar = 2

    fig, axs = plt.subplots(2, 2, figsize=(8, 6))

    Delta = 1

    #Definir Señal 1
    if senal_discreta == 1:
        #Definir X
        t_1 = np.arange(-5, 5 + Delta, Delta)
        x_t = 5 - np.absolute(t_1)

        #Definir h
        t_2 = np.arange(-4, 6 + Delta, Delta)
        h_t = np.ones(len(t_2))

        limite_y_inferior = -1
        limite_y_x = 6
        limite_y_h = 2

    #Definir Señal 2
    elif senal_discreta == 2:
        #Definir X
        t_1 = np.arange(-5, 5 + Delta, Delta)
        x_t = np.ones(len(t_1))

        #Definir h
        t_2 = np.arange(0, 10 + Delta, Delta)
        h_t = (7/8) ** t_2

        limite_y_inferior = -1
        limite_y_x = 2
        limite_y_h = 2


    # Arreglar señal x
    if senal_desplazar == 1:
        
        # Reflejar la señal
        n_1_inversa = []

        for i in reversed(t_1):
            n_1_inversa.append(-i)

        x_n_inversa = []

        for i in reversed(x_t):
            x_n_inversa.append(i)

        # Mover la señal
        t_1_desplazada = n_1_inversa - (max(n_1_inversa) - min(t_2) + 1)

        # Calcular límites del nuevo vector n
        n_nuevo_min = min(np.append(t_1_desplazada, t_2))
        n_nuevo_max = max(np.append(t_1_desplazada, t_2))

        # Crear el nuevo vector n
        n_nuevo = np.arange(n_nuevo_min, n_nuevo_max + (len(x_t)* Delta) + Delta, Delta)

        # Encontrar puntos iniciales y finales de la señal en el nuevo vector n
        punto_inicial_1 = 0
        punto_final_1 = 0

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == min(t_1_desplazada):
                punto_inicial_1 = i
                break

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == max(t_1_desplazada):
                punto_final_1 = i
                break

        # Crear nuevo vector x[n]
        x_n_nuevo = np.zeros(len(n_nuevo))

        for i in range(len(n_nuevo)):
            if i < punto_inicial_1:
                x_n_nuevo[i] = 0
            elif punto_inicial_1 <= i <= punto_final_1:
                x_n_nuevo[i] = x_n_inversa[i - punto_inicial_1]
            else:
                x_n_nuevo[i] = 0

        # Arreglar señal h
        # Encontrar puntos iniciales y finales de la señal en el nuevo vector n
        punto_inicial_2 = 0
        punto_final_2 = 0

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == min(t_2):
                punto_inicial_2 = i
                break

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == max(t_2):
                punto_final_2 = i
                break

        # Crear nuevo vector h[n]
        h_n_nuevo = np.zeros(len(n_nuevo))

        for i in range(len(n_nuevo)):
            if i < punto_inicial_2:
                h_n_nuevo[i] = 0
            elif punto_inicial_2 <= i <= punto_final_2:
                h_n_nuevo[i] = h_t[i - punto_inicial_2]
            else:
                h_n_nuevo[i] = 0

        # Definir variables de convolucion

        n_convolucion = n_nuevo
        senal_desplazada_convolucion = x_n_nuevo
        senal_quieta_convolucion = h_n_nuevo
        senal_quieta = h_t
        senal_desplazada = x_t

        # Graficar las señales originales

        axs[0,0].axhline(0, color='black', linewidth=1)
        axs[0,0].axvline(0, color='black', linewidth=1) 
        axs[0,0].stem(t_1, x_t, linefmt='r-', markerfmt='ro', basefmt=' ')
        axs[0,0].grid()
        axs[0,0].set_title('Señal Desplazada')
        axs[0,0].set_xlabel('n')
        axs[0,0].set_ylabel('x[n]')
        axs[0,0].set_ylim(limite_y_inferior, limite_y_x)

        axs[0,1].axhline(0, color='black', linewidth=1)
        axs[0,1].axvline(0, color='black', linewidth=1)
        axs[0,1].stem(t_2, h_t, linefmt='b-', markerfmt='bo', basefmt=' ')
        axs[0,1].grid()
        axs[0,1].set_title('Señal Fija')
        axs[0,1].set_xlabel('n')
        axs[0,1].set_ylabel('h[n]')
        axs[0,1].set_ylim(limite_y_inferior, limite_y_h)

    # Arreglar señal h
    elif senal_desplazar == 2:
        # Reflejar la señal
        n_2_i = []

        for i in reversed(t_2):
            n_2_i.append(-i)

        h_n_i = []

        for i in reversed(h_t):
            h_n_i.append(i)

        # Mover la señal
        
        n_2_d = n_2_i - (max(n_2_i) - min(t_1) + 1)

        # Calcular límites del nuevo vector n
        n_nuevo_min = min(np.append(n_2_d, t_1))
        n_nuevo_max = max(np.append(n_2_d, t_1))

        # Crear el nuevo vector n
        n_nuevo = np.arange(n_nuevo_min, n_nuevo_max + (len(h_t) * Delta) + Delta, Delta)

        # Encontrar puntos iniciales y finales de la señal en el nuevo vector n
        punto_inicial_2 = 0
        punto_final_2 = 0

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == min(n_2_d):
                punto_inicial_2 = i
                break

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == max(n_2_d):
                punto_final_2 = i
                break

        # Crear nuevo vector h[n]
        h_n_nuevo = np.zeros(len(n_nuevo))

        for i in range(len(n_nuevo)):
            if i < punto_inicial_2:
                h_n_nuevo[i] = 0
            elif punto_inicial_2 <= i <= punto_final_2:
                h_n_nuevo[i] = h_n_i[i - punto_inicial_2]
            else:
                h_n_nuevo[i] = 0

        #Arreglar señal x

        # Encontrar puntos iniciales y finales de la señal en el nuevo vector n
        punto_inicial_1 = 0
        punto_final_1 = 0

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == min(t_1):
                punto_inicial_1 = i
                break

        for i in range(len(n_nuevo)):
            if n_nuevo[i] == max(t_1):
                punto_final_1 = i
                break

        # Crear nuevo vector x[n]
        x_n_nuevo = np.zeros(len(n_nuevo))

        for i in range(len(n_nuevo)):
            if i < punto_inicial_1:
                x_n_nuevo[i] = 0
            elif punto_inicial_1 <= i <= punto_final_1:
                x_n_nuevo[i] = x_t[i - punto_inicial_1]
            else:
                x_n_nuevo[i] = 0

        # Definir variables de convolucionolución

        n_convolucion = n_nuevo
        senal_desplazada_convolucion = h_n_nuevo
        senal_quieta_convolucion = x_n_nuevo
        senal_quieta = x_t
        senal_desplazada = h_t

        # Graficar las señales originales

        axs[0,0].axhline(0, color='black', linewidth=1)
        axs[0,0].axvline(0, color='black', linewidth=1) 
        axs[0,0].stem(t_2, h_t, linefmt='r-', markerfmt='ro', basefmt=' ')
        axs[0,0].grid()
        axs[0,0].set_title('Señal Desplazada')
        axs[0,0].set_xlabel('n')
        axs[0,0].set_ylabel('h[n]')
        axs[0,0].set_ylim(limite_y_inferior, limite_y_h)

        axs[0,1].axhline(0, color='black', linewidth=1)
        axs[0,1].axvline(0, color='black', linewidth=1)
        axs[0,1].stem(t_1, x_t, linefmt='b-', markerfmt='bo', basefmt=' ')
        axs[0,1].grid()
        axs[0,1].set_title('Señal Fija')
        axs[0,1].set_xlabel('n')
        axs[0,1].set_ylabel('x[n]')
        axs[0,1].set_ylim(limite_y_inferior, limite_y_x)
    
    # Crear variables propias de la convolucion

    senal_desplazada_convolucion_m = []
    convolucion = []
    n_convolucion_array = []

    #Proceso de convolucion

    for i in range(len(x_t)+len(h_t)+1):
        axs[1,0].axhline(0, color='black', linewidth=1)
        axs[1,0].axvline(0, color='black', linewidth=1) 
        axs[1,0].stem(n_convolucion, senal_quieta_convolucion, linefmt='b-', markerfmt='bo', basefmt=' ')
        axs[1,0].grid()
        axs[1,0].set_title('Proceso de convolución')
        axs[1,0].set_xlabel('n')
        axs[1,0].set_xlim(min(n_convolucion), max(n_convolucion))
        axs[1,0].set_ylim(min(np.append(senal_desplazada_convolucion, senal_quieta_convolucion)) - 1, max(np.append(senal_desplazada_convolucion, senal_quieta_convolucion)) + 1)

        senal_desplazada_convolucion_m = np.concatenate((np.zeros(i), senal_desplazada_convolucion[0:len(senal_desplazada)], np.zeros(len(n_convolucion) - len(senal_desplazada) - i)))

        axs[1,0].stem(n_convolucion, senal_desplazada_convolucion_m, linefmt='r-', markerfmt='ro', basefmt=' ')

        n_convolucion_array.append(i + min(t_1) + min(t_2) - 1)
        convolucion.append(np.sum(senal_desplazada_convolucion_m * senal_quieta_convolucion))
        axs[1,1].axhline(0, color='black', linewidth=1)
        axs[1,1].axvline(0, color='black', linewidth=1) 
        axs[1,1].stem(n_convolucion_array, convolucion, linefmt='b-', markerfmt='bo', basefmt=' ')
        axs[1,1].grid()
        axs[1,1].set_title('Resultado de la convolución')
        axs[1,1].set_xlabel('n')
        axs[1,1].set_xlim(min(n_convolucion_array)-1, max(n_convolucion_array)+1)
        axs[1,1].set_ylim(min(convolucion)-1, max(convolucion)+1)

        plt.tight_layout()
        plt.pause(0.1)

        if i != len(x_t)+len(h_t):
            axs[1,0].cla() 
            axs[1,1].cla()

    print(convolucion)
    plt.tight_layout()
    plt.show()
#------------------------------------------------------------------------------------------

# Pestaña 3: Función para asignar un nuevo valor a senal_continua_1 y senal_continua_2 basado en las selecciones de los menús

def eleccion_continuo2():
    
    global senal_discreta
    global senal_desplazar  
    global punto
    global tipo_convolucion

    seleccion_menu11 = seleccion_menu_c2()
    
    if seleccion_menu11 == "Punto A":
        senal_continua_p2 = 1
    elif seleccion_menu11 == "Punto B":
        senal_continua_p2 = 2
    elif seleccion_menu11 == "Punto C":
        senal_continua_p2 = 3

    Delta = 0.01
    inicio = -10
    final = 10

    # Figura y subplots
    fig = plt.figure(figsize=(10, 8))
    gs = plt.GridSpec(2, 4, figure=fig)

    # Definir señales
    if senal_continua_p2 == 1:
        t_1 = np.arange(inicio, final + Delta, Delta)
        x_t = np.zeros_like(t_1)
        x_t[(t_1 >= -1) & (t_1 <= 6)] = np.exp(-(1/4) * t_1[(t_1 >= -1) & (t_1 <= 6)])

        h_t = np.zeros_like(t_1)
        h_t[t_1 >= 0 ] = np.exp(-(1/2) * t_1[t_1 >= 0])

        inferior_x_x = -2
        superior_x_x = 7
        inferior_x_h = -1
        superior_x_h = 5

        # Convolución matemática
        t_convolucion_mat = np.arange(inicio, final + Delta, Delta)
        amplitud_convolucion_mat = np.zeros_like(t_convolucion_mat)
        amplitud_convolucion_mat[(t_convolucion_mat >= -1) & (t_convolucion_mat < 6)] = 4 * np.exp(-1/2 * t_convolucion_mat[(t_convolucion_mat >= -1) & (t_convolucion_mat < 6)]) * (np.exp(1/4 * t_convolucion_mat[(t_convolucion_mat >= -1) & (t_convolucion_mat < 6)]) - np.exp(-1/4))
        amplitud_convolucion_mat[t_convolucion_mat >= 6] = 4 * np.exp(-1/2 * t_convolucion_mat[t_convolucion_mat >= 6]) * (np.exp(3/2) - np.exp(-1/4))
    elif senal_continua_p2 == 2:
        t_1 = np.arange(inicio, final + Delta, Delta)
        x_t = np.zeros_like(t_1)

        x_t[(t_1 >= -10) & (t_1 < 0)] = np.exp(t_1[(t_1 >= -10) & (t_1 < 0)])
        x_t[(t_1 <= 10) & (t_1 >= 0)] = np.exp(-1 * t_1[(t_1 <= 10) & (t_1 >= 0)])

        h_t = np.zeros_like(t_1)
        h_t[(t_1 >= -1)] = np.exp(-2 * t_1[(t_1 >= -1)])

        inferior_x_x = -3
        superior_x_x = 3
        inferior_x_h = -2
        superior_x_h = 2

        # Convolución matemática
        t_convolucion_mat = np.arange(inicio, final + Delta, Delta)
        amplitud_convolucion_mat = np.zeros_like(t_convolucion_mat)
        amplitud_convolucion_mat[t_convolucion_mat < -1] = (1/3) * np.exp(t_convolucion_mat[t_convolucion_mat < -1] + 3)
        amplitud_convolucion_mat[t_convolucion_mat >= -1] = np.exp(1 - t_convolucion_mat[t_convolucion_mat >= -1]) - (2/3)*(np.exp(-2 * t_convolucion_mat[t_convolucion_mat >= -1]))
    elif senal_continua_p2 == 3:
        t_1 = np.arange(inicio, final + Delta, Delta)
        x_t = np.zeros_like(t_1)

        x_t[(t_1 >= -1) & (t_1 <= 4)] = np.ones_like(t_1[(t_1 >= -1) & (t_1 <= 4)])

        h_t = np.zeros_like(t_1)
        h_t[(t_1 <= 1)] = np.exp(t_1[(t_1 <= 1)])

        inferior_x_x = -2
        superior_x_x = 5
        inferior_x_h = -2
        superior_x_h = 2

        # Convolución matemática
        t_convolucion_mat = np.arange(inicio, final + Delta, Delta)
        amplitud_convolucion_mat = np.zeros_like(t_convolucion_mat)
        amplitud_convolucion_mat[t_convolucion_mat <= 0] = np.exp(t_convolucion_mat[t_convolucion_mat <= 0]) * (np.exp(1) - np.exp(-4))
        amplitud_convolucion_mat[(t_convolucion_mat > 0) & (t_convolucion_mat <= 5)] = np.exp(t_convolucion_mat[(t_convolucion_mat > 0) & (t_convolucion_mat <= 5)]) * (np.exp(-(t_convolucion_mat[(t_convolucion_mat > 0) & (t_convolucion_mat <= 5)] - 1)) - np.exp(-4))

    # Convolucionar usando convolve
    t_convolucion = np.arange((inicio * 2), (final * 2) + 0.001, Delta ) 
    amplitud_convolucion = np.convolve(x_t, h_t, mode='full') * Delta

    # Señales Originales
    ax0 = plt.subplot(gs[0, 0:2])
    ax0.axhline(0, color='black', linewidth=1)
    ax0.axvline(0, color='black', linewidth=1)
    ax0.plot(t_1, x_t, color='purple')
    ax0.grid()
    ax0.set_title('Señal 1')
    ax0.set_xlabel('t')
    ax0.set_ylabel('x(t)')
    ax0.set_xlim(inferior_x_x, superior_x_x)

    ax1 = plt.subplot(gs[0, 2:4])
    ax1.axhline(0, color='black', linewidth=1)
    ax1.axvline(0, color='black', linewidth=1)
    ax1.plot(t_1, h_t, color='orange')
    ax1.grid()
    ax1.set_title('Señal 2')
    ax1.set_xlabel('t')
    ax1.set_ylabel('h(t)')
    ax1.set_xlim(inferior_x_h, superior_x_h)

    superior_x = 2 * max(superior_x_h, superior_x_x)
    inferior_x = 2 * min(inferior_x_h, inferior_x_x)

    # Gráfica Comparación convolve y expresión
    ax2 = plt.subplot(gs[1, 1:3])
    ax2.axhline(0, color='black', linewidth=1)
    ax2.axvline(0, color='black', linewidth=1)
    ax2.plot(t_convolucion, amplitud_convolucion, color='red', label='Función Python')
    ax2.plot(t_convolucion_mat, amplitud_convolucion_mat, color='green', label='Expresión Matemática')
    ax2.grid()
    ax2.set_title('Comparación')
    ax2.set_xlabel('t')
    ax2.set_ylabel('y(t)')
    ax2.set_xlim(inferior_x, superior_x)
    ax2.legend()

    # Esconder figura segunda fila y primera columna
    ax3 = plt.subplot(gs[1, 0])
    ax3.axis('off')

    plt.tight_layout()
    plt.show()
#------------------------------------------------------------------------------------------

# Creacion de la interfaz

ventana = ctk.CTk()

# Get the width and height of the screen
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calculate the X and Y coordinates for the top-right corner
x_position = screen_width - 500  # Assuming the width of the window is 500
y_position = 0

# Set the position of the window
ventana.geometry("500x350+{}+{}".format(x_position, y_position))

# Crear el Notebook para las pestañas
notebook = ttk.Notebook(master=ventana)
notebook.pack(fill="both", expand=True)

#------------------------------------------------------------------------------------------

# Crear la pestaña "Tiempo Continuo - Punto 1"
pestana_tiempo_continuo_punto1 = ctk.CTkFrame(master=notebook)
notebook.add(pestana_tiempo_continuo_punto1, text="Tiempo Continuo - Punto 1")

# Crear los elementos de la pestaña "Tiempo Continuo - Punto 1"
titulo_tiempo_continuo_punto1 = ctk.CTkLabel(master=pestana_tiempo_continuo_punto1, text="Tiempo Continuo", font=("Roboto", 25))
titulo_tiempo_continuo_punto1.pack(pady=12, padx=10)

contenedor_opciones_tiempo_continuo_punto1 = ctk.CTkFrame(master=pestana_tiempo_continuo_punto1)
contenedor_opciones_tiempo_continuo_punto1.pack(pady=12, padx=10)

opcion1_tiempo_continuo_punto1 = ctk.CTkOptionMenu(master=contenedor_opciones_tiempo_continuo_punto1, values=["Señal A", "Señal B", "Señal C", "Señal D", "Señal E", "Señal F"])
opcion1_tiempo_continuo_punto1.pack(side="left", pady=10, padx=10)
opcion1_tiempo_continuo_punto1.set("Señal x(t)")

opcion2_tiempo_continuo_punto1 = ctk.CTkOptionMenu(master=contenedor_opciones_tiempo_continuo_punto1, values=["Señal A", "Señal B", "Señal C", "Señal D", "Señal E", "Señal F"])
opcion2_tiempo_continuo_punto1.pack(side="left", pady=10, padx=10)
opcion2_tiempo_continuo_punto1.set("Señal h(t)")

boton_tiempo_continuo_punto1 = ctk.CTkButton(master=contenedor_opciones_tiempo_continuo_punto1, text="Calcular Convolución", command = eleccion_continuo1)
boton_tiempo_continuo_punto1.pack(side="left", pady=10, padx=10)

#------------------------------------------------------------------------------------------

# Crear la pestaña "Tiempo Discreto - Punto 1"
pestana_tiempo_discreto_punto1 = ctk.CTkFrame(master=notebook)
notebook.add(pestana_tiempo_discreto_punto1, text="Tiempo Discreto - Punto 1")

# Crear los elementos de la pestaña "Tiempo Discreto - Punto 1"
titulo_tiempo_discreto_punto1 = ctk.CTkLabel(master=pestana_tiempo_discreto_punto1, text="Tiempo Discreto", font=("Roboto", 25))
titulo_tiempo_discreto_punto1.pack(pady=12, padx=10)

contenedor_opciones_tiempo_discreto_punto1 = ctk.CTkFrame(master=pestana_tiempo_discreto_punto1)
contenedor_opciones_tiempo_discreto_punto1.pack(pady=12, padx=10)

# Menú 1: Elegir entre "Punto A" y "Punto B"
menu1_tiempo_discreto_punto1 = ctk.CTkOptionMenu(master=contenedor_opciones_tiempo_discreto_punto1, values=["Punto A", "Punto B"])
menu1_tiempo_discreto_punto1.pack(side="left", pady=10, padx=10)
menu1_tiempo_discreto_punto1.set("Punto")

menu2_tiempo_discreto_punto1 = ctk.CTkOptionMenu(master=contenedor_opciones_tiempo_discreto_punto1, values=["Desplazar x[n]", "Desplazar h[n]"])
menu2_tiempo_discreto_punto1.pack(side="left", pady=10, padx=10)
menu2_tiempo_discreto_punto1.set("Señal Desplazada")

boton_calcular_tiempo_discreto_punto1 = ctk.CTkButton(master=contenedor_opciones_tiempo_discreto_punto1, text="Calcular Convolución", command = eleccion_discreto1)
boton_calcular_tiempo_discreto_punto1.pack(side="left", pady=10, padx=10)

#------------------------------------------------------------------------------------------

# Crear la pestaña "Tiempo Continuo - Punto 2"
pestana_tiempo_continuo_punto2 = ctk.CTkFrame(master=notebook)
notebook.add(pestana_tiempo_continuo_punto2, text="Tiempo Continuo - Punto 2")

# Crear los elementos de la pestaña "Tiempo Continuo - Punto 2"
titulo_tiempo_continuo_punto2 = ctk.CTkLabel(master=pestana_tiempo_continuo_punto2, text="Tiempo Continuo", font=("Roboto", 25))
titulo_tiempo_continuo_punto2.pack(pady=12, padx=10)

contenedor_opciones_tiempo_continuo_punto2 = ctk.CTkFrame(master=pestana_tiempo_continuo_punto2)
contenedor_opciones_tiempo_continuo_punto2.pack(pady=12, padx=10)

# Menú 1: Elegir entre "Punto A", "Punto B" y "Punto C"
menu1_tiempo_continuo_punto2 = ctk.CTkOptionMenu(master=contenedor_opciones_tiempo_continuo_punto2, values=["Punto A", "Punto B", "Punto C"])
menu1_tiempo_continuo_punto2.pack(side="left", pady=10, padx=10)
menu1_tiempo_continuo_punto2.set("Punto")

boton_calcular_tiempo_continuo_punto2 = ctk.CTkButton(master=contenedor_opciones_tiempo_continuo_punto2, text="Calcular Convolución", command = eleccion_continuo2)
boton_calcular_tiempo_continuo_punto2.pack(side="left", pady=10, padx=10)
#------------------------------------------------------------------------------------------

ventana.mainloop()