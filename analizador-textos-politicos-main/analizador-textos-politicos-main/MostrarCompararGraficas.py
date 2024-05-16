import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from collections import Counter
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from nltk.draw.dispersion import dispersion_plot
from CargarInforme import tokenizar_texto_pdf, obtener_texto, contar_palabras_clave
from MostrarEstadisticasGenerales import exportar_a_csv

def combinar_tokens(pdf_paths):
    tokens_combinados = []
    for pdf_path in pdf_paths:
        texto_pdf = obtener_texto(pdf_path)
        tokens_pdf = tokenizar_texto_pdf(texto_pdf)
        tokens_combinados.extend(tokens_pdf)
    return tokens_combinados

def graficar_dispersion(tokens_combinados, palabras_clave):
    dispersion_plot(tokens_combinados, palabras_clave, ignore_case=True, title='Gráfica de Dispersión Léxica')
    plt.gcf().set_size_inches(11, 5)  # Establecer tamaño de la figura
    #plt.tight_layout()  # Ajustar diseño de la figura
    plt.xlabel("Desplazamiento de palabra")
    plt.ylabel("Palabras clave")
    plt.grid(True)
    plt.show()
    
def graficar_barras(ruta_archivo_csv):
    df_clave = pd.read_csv(ruta_archivo_csv, encoding='latin1')
    #print(df_clave.head()) # Imprime las primeras 5 filas del DataFrame para verificar que se haya cargado correctamente

    plt.figure(figsize=(11,5))
    plt.bar(df_clave['Palabra'], df_clave['Conteo'])
    plt.xlabel('Palabra clave')
    plt.ylabel('Conteo')
    plt.title('Conteo de palabras clave en informes presidenciales')
    plt.grid(True)
    plt.xticks(rotation='vertical')

    plt.show()
    
def graficar_wordcloud(ruta_archivo_csv, ruta_png):
    def trasformar_png(png_path):
        # Cargar la máscara desde el archivo PNG
        mapa_mascara = np.array(Image.open(png_path))
        #print(mapa_mascara) # Imprime la matriz de la máscara

        def transform_format(val):
            return np.where(val == 0, 255, val)

        # Aplicar la transformación directamente al array de la máscara
        mapa_mascara_transformada = transform_format(mapa_mascara)

        #print(mapa_mascara_transformada) # Imprime la matriz de la máscara transformada
        return mapa_mascara_transformada
    
    df = pd.read_csv(ruta_archivo_csv, encoding='latin1')
    png_path = ruta_png

    # Crear un diccionario de palabras y sus recuentos a partir del DataFrame
    palabras_dicc = dict(zip(df['Palabra'], df['Conteo']))
    #  'zip' combina estas dos columnas en pares de clave-valor, y 'dict' convierte estos pares en un diccionario.

    # Generar una máscara a partir de un archivo PNG
    mapa_mascara = trasformar_png(png_path)

    # Crear un objeto WordCloud
    wordcloud = WordCloud(width=800, height=400, mask=mapa_mascara, contour_width=1.0, contour_color='black', background_color='white').generate_from_frequencies(palabras_dicc)

    # Visualizar la WordCloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
def generar_grafica_serie_tiempo(df_tiempo, palabras_st):
    plt.figure(figsize=(10, 6))
    for palabra in palabras_st:
        plt.plot(df_tiempo.index, df_tiempo[palabra], label=palabra)

    plt.title('Evolución del Conteo de Palabras Clave')
    plt.xlabel('Año')
    plt.ylabel('Conteo')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def procesar_pdf(pdf_paths, palabras_st):
    contador_total = Counter()
    fechas = []
    conteos = {palabra: [] for palabra in palabras_st}

    for pdf_path in pdf_paths:
        match = re.findall(r'_(\d{4})_', pdf_path)
        if match:
            año = match[0]
        else:
            año = 'Desconocido'
        
        texto_pdf = obtener_texto(pdf_path)
        contador_actual = contar_palabras_clave(texto_pdf, palabras_st)
        contador_total.update(contador_actual)
        nombre_archivo = f'Tablas_conteo\conteo_palabras_clave_{año}.csv'
        exportar_a_csv(contador_actual, nombre_archivo)
        
        fechas.append(año)
        for palabra in palabras_st:
            conteos[palabra].append(contador_actual[palabra])

    df_tiempo = pd.DataFrame(conteos, index=fechas)
    return df_tiempo
""""   
def main():
    # Lista de rutas de archivos PDF
    pdf_paths = ['Informes presidenciales\_1_Carlos_Salinas\_1989_informe_CS.pdf', 
                'Informes presidenciales\_1_Carlos_Salinas\_1990_informe_CS.pdf', 
                'Informes presidenciales\_1_Carlos_Salinas\_1991_informe_CS.pdf',
                'Informes presidenciales\_1_Carlos_Salinas\_1992_informe_CS.pdf',
                'Informes presidenciales\_1_Carlos_Salinas\_1993_informe_CS.pdf',
                'Informes presidenciales\_1_Carlos_Salinas\_1994_informe_CS.pdf']

    ruta_archivo_csv = 'Tablas_conteo\conteo_palabras_clave.csv'

    ruta_png = 'mapa_mexico_2.1.png'

    palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad', 'compromiso', 'inversión',
                    'económica', 'trabajadores', 'trabajo', 'deuda', 'externa', 'concertación', 'estabilidad', 'solidaridad', 'democracia',
                    'medio', 'ambiente', 'campesinos', 'salud', 'inflación', 'impuesto', 'salarios']
        
    palabras_st = ['inflación', 'deuda', 'impuesto', 'salarios', 'gasolina', 'educación', 'corrupción']


    tokens_combinados = combinar_tokens(pdf_paths)
    # Procesar los PDFs y generar la serie de tiempo
    df_tiempo = procesar_pdf(pdf_paths, palabras_st)

    graficar_dispersion(tokens_combinados, palabras_clave)
    generar_grafica_serie_tiempo(df_tiempo, palabras_st)
    graficar_wordcloud(ruta_archivo_csv, ruta_png)
    graficar_barras(ruta_archivo_csv)
 
if __name__ == '__main__':
    main()
"""
