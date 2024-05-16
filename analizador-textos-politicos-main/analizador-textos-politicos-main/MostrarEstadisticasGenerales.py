import nltk
import pandas as pd
from collections import Counter
from CargarInforme import obtener_texto, contar_palabras, contar_palabras_clave

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

def contar_palabras_pdfs(pdf_paths):
    contador_total = Counter()  # Inicializa un contador total para contar las palabras en todos los archivos
    
    for pdf_path in pdf_paths:
        texto = obtener_texto(pdf_path)
        contador = contar_palabras(texto)
        contador_total.update(contador)  # Actualiza el contador total con las palabras del archivo actual
    
    return contador_total

def contar_palabras_clave_pdfs(pdf_paths, palabras_clave):
    contador_total_clave = Counter()
    
    for pdf_path in pdf_paths:
        texto = obtener_texto(pdf_path)
        contador = contar_palabras_clave(texto, palabras_clave)
        contador_total_clave.update(contador)
    
    return contador_total_clave

def exportar_a_csv(contador, nombre_archivo):
    df = pd.DataFrame.from_dict(contador, orient='index', columns=['Conteo']).reset_index()
    df.columns = ['Palabra', 'Conteo']
    df.to_csv(nombre_archivo)
    
    # Ordenar el contador por número de repeticiones en orden descendente
    palabras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    
    # Guardar palabras clave ordenadas en un archivo CSV
    with open(nombre_archivo, 'w') as file:
        file.write('Palabra,Conteo\n')
        for palabra, contador in palabras_ordenadas:
            file.write(f'{palabra},{contador}\n')
            
    print("Tabulación de total de palabras guardadas en el archivo CSV. Verifique la carpeta Tablas_conteo en: ", nombre_archivo, "\n")

def main():    
    # Lista de rutas de archivos PDF
    pdf_paths = ['Informes presidenciales\_1_Carlos_Salinas\_1989_informe_CS.pdf', 
                'Informes presidenciales\_1_Carlos_Salinas\_1990_informe_CS.pdf', 
                'Informes presidenciales\_1_Carlos_Salinas\_1991_informe_CS.pdf',
                'Informes presidenciales\_1_Carlos_Salinas\_1992_informe_CS.pdf',
                'Informes presidenciales\_1_Carlos_Salinas\_1993_informe_CS.pdf',
                'Informes presidenciales\_1_Carlos_Salinas\_1994_informe_CS.pdf']

    # Lista de palabras clave a buscar
    palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad', 'compromiso', 'inversión',
                    'económica', 'trabajadores', 'trabajo', 'deuda', 'externa', 'concertación', 'estabilidad', 'solidaridad', 'democracia',
                    'medio', 'ambiente', 'campesinos', 'salud', 'inflación', 'impuesto', 'salarios']  

    contadorPalabras = contar_palabras_pdfs(pdf_paths)
    contadorClave = contar_palabras_clave_pdfs(pdf_paths, palabras_clave)
    TotalPalabras = sum(contadorPalabras.values())
    TotalDiferentes = len(contadorPalabras)
    TotalClave = sum(contadorClave.values())
    ruta_palabras = 'Tablas_conteo\conteo_palabras.csv'
    ruta_clave = 'Tablas_conteo\conteo_palabras_clave.csv'

    print("Total de palabras encontradas: ", TotalPalabras, "\n")
    print("Promedio de palabras por documento: ", TotalPalabras/len(pdf_paths), "\n")
    print("Total de palabras diferentes: ", TotalDiferentes, "\n")
    print("Conteo de palabras clave encontradas: ", TotalClave, "\n")

    exportar_a_csv(contadorPalabras, 'Tablas_conteo\conteo_palabras.csv')
    exportar_a_csv(contadorClave, 'Tablas_conteo\conteo_palabras_clave.csv')

if __name__ == '__main__':
    main()     
