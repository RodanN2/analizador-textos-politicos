import fitz
import nltk
import string
from collections import Counter
from nltk.tokenize import word_tokenize

def obtener_texto(pdf_path):
    texto = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        texto += page.get_text()  # Obtén el texto de la página
    doc.close()
    return texto

def contar_palabras(texto):
    contador = Counter()  # Inicializa un contador para contar las palabras
    tokens = nltk.word_tokenize(texto)
    palabras = [token.lower() for token in tokens if token.isalnum()]  # Se mantienen solo las palabras alfanuméricas
    contador.update(palabras)  # Actualiza el contador con las palabras
    
    return contador

def contar_palabras_clave(texto, palabras_clave):
    contador = Counter()
    for palabra_clave in palabras_clave:
        contador[palabra_clave] += texto.lower().count(palabra_clave.lower())  # Contabiliza las ocurrencias de la palabra clave en la página
    
    return contador

def tokenizar_texto_pdf(texto):
    tokens = nltk.word_tokenize(texto)
    tokens = [token for token in tokens if token not in string.punctuation]
    return tokens