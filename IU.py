import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def salir():
    ventana.destroy()

def cargar_archivos():
    archivos_seleccionados = filedialog.askopenfilenames()
    for archivo in archivos_seleccionados:
        print("Archivo seleccionado:", archivo)

def regresar():
    ventana.geometry('500x500')
    boton_cargar.pack_forget()
    boton_regresar.pack_forget()
    titulo.pack(pady=15)
    boton1.pack(pady=15)
    boton2.pack(pady=15)
    boton3.pack(pady=15)
    boton4.pack(pady=15)

def mostrar_opciones():
    ventana.geometry('500x100')
    titulo.pack_forget()
    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack_forget()
    boton4.pack_forget()
    boton_cargar.pack(pady=10)
    boton_regresar.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador de informes políticos")
estilo = ttk.Style()

ventana.geometry('500x500')
#titulo
titulo = tk.Label(ventana, text='Analizador de informes políticos', padx=15, pady=15, font=('Helvetica', 20), fg='Blue')




# Crear los cuatro botones principales
boton1 = tk.Button(ventana, text="Cargar informes", command=mostrar_opciones, padx=60, pady=15)
boton2 = tk.Button(ventana, text="Mostrar estadísticas generales", command=lambda: print("Botón 2 presionado"), padx=60, pady=20)
boton3 = tk.Button(ventana, text="Mostrar/Comparar gráficas", command=lambda: print("Botón 3 presionado"), padx=60, pady=20)
boton4 = tk.Button(ventana, text="Salir del programa", command=salir, padx=60, pady=20)

# Crear los botones de cargar archivos y regresar, pero inicialmente ocultos
boton_cargar = tk.Button(ventana, text="Cargar Archivos", command=cargar_archivos, padx=110, pady=10)
boton_regresar = tk.Button(ventana, text="Regresar", command=regresar)
boton_cargar.pack_forget()
boton_regresar.pack_forget()

# Alinear los botones al centro
titulo.pack(pady=15)
boton1.pack(pady=15)
boton2.pack(pady=15)
boton3.pack(pady=15)
boton4.pack(pady=15)


# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
