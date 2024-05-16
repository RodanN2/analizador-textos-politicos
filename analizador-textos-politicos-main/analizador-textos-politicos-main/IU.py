import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from MostrarCompararGraficas import graficar_dispersion
from MostrarCompararGraficas import graficar_barras
from MostrarCompararGraficas import generar_grafica_serie_tiempo
from MostrarCompararGraficas import graficar_wordcloud
from MostrarCompararGraficas import combinar_tokens
from MostrarCompararGraficas import procesar_pdf
from MostrarEstadisticasGenerales import contar_palabras


def cargar_archivos():
    archivos_seleccionados = filedialog.askopenfilenames()
    rutas = list(archivos_seleccionados)  # Convertir el objeto en una lista
    print("Archivos seleccionados:", rutas)
    return rutas 


#Ventana que se abre al seleccionar Mostrar estadisticas generales
def abrir_ventana_estadisticas():
    # Crear una nueva ventana
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.withdraw()

    # Crear un botón en la ventana secundaria
    boton_hola = ttk.Button(ventana_secundaria)
    boton_hola.pack(pady=20)
    
#Ventana que se abre al seleccionar Mostrar/Comparar Graficas
def abrir_ventana_graficas():
    
    ventana_secundaria_dos = tk.Toplevel(ventana)
    ventana_secundaria_dos.title('Mostrar/Comparar gráficas')
    ventana_secundaria_dos.geometry('500x500')
    boton_un_presidente = tk.Button(ventana_secundaria_dos, text='Mostrar gráficas para un solo presidente', pady=35, command=hacer_graficas)
    boton_varios_presidentes = tk.Button(ventana_secundaria_dos, text='Mostrar gráficas para varios presidentes', pady=35, command=hacer_graficas)
    boton_un_presidente.pack(padx=50, pady=60)
    boton_varios_presidentes.pack(padx=50, pady=20)


def salir():
    ventana.destroy()


#Arreglo que contiene las rutas de los archivos seleccionados
rutas_de_archivos = cargar_archivos()

#-------------------------------------------------------------
ruta_archivo_csv = 'Tablas_conteo\conteo_palabras_clave.csv'

ruta_png = 'mapa_mexico_2.1.png'

palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad', 'compromiso', 'inversión',
                    'económica', 'trabajadores', 'trabajo', 'deuda', 'externa', 'concertación', 'estabilidad', 'solidaridad', 'democracia',
                    'medio', 'ambiente', 'campesinos', 'salud', 'inflación', 'impuesto', 'salarios']
        
palabras_st = ['inflación', 'deuda', 'impuesto', 'salarios', 'gasolina', 'educación', 'corrupción']


tokens_combinados = combinar_tokens(rutas_de_archivos)
# Procesar los PDFs y generar la serie de tiempo
df_tiempo = procesar_pdf(rutas_de_archivos, palabras_st)

#------------------------------------------------------------- 

def hacer_graficas():
    
    graficar_dispersion(tokens_combinados, palabras_clave)
    generar_grafica_serie_tiempo(df_tiempo, palabras_st)
    graficar_wordcloud(ruta_archivo_csv, ruta_png)
    graficar_barras(ruta_archivo_csv)


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
ventana.geometry('500x500')
titulo = tk.Label(ventana, text='Analizador de informes políticos', padx=15, pady=15, font=('Helvetica', 20), fg='Blue')



# Crear los cuatro botones principales
boton1 = tk.Button(ventana, text="Cargar informes", command=mostrar_opciones, padx=60, pady=15)
boton2 = tk.Button(ventana, text="Mostrar estadísticas generales", command=abrir_ventana_estadisticas, padx=60, pady=20)
boton3 = tk.Button(ventana, text="Mostrar/Comparar gráficas", command=abrir_ventana_graficas, padx=60, pady=20)
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

