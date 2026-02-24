from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import jaccard
'''
CountVectorizer de sklearn.feature_extraction.text se usa para convertir cadenas en conjuntos de n-gramas.
jaccard de scipy.spatial.distance nos permite calcular la distancia de Jaccard entre dos conjuntos.
'''

'''
Se define una función que recibe dos cadenas (str1 y str2).
También tiene un parámetro n (opcional) que indica el tamaño de los n-gramas (por defecto, bigramas).
'''
def jaccard_dissimilarity(str1, str2, n=2):
    # Convertimos las cadenas en conjuntos de n-gramas
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(n, n), binary=True)
    '''
    CountVectorizer se configura con:
        analyzer='char': Analiza caracteres en lugar de palabras.
        ngram_range=(n, n): Extrae n-gramas de tamaño n.
        binary=True: Indica si un n-grama está presente (1) o no (0), en lugar de contar su frecuencia.
        
        Por ejemplo, para "casa" y "caso" con n=2, los bigramas serían:
        # "casa" → {'ca', 'as', 'sa'}
        # "caso" → {'ca', 'as', 'so'}

    '''
    ngram_matrix = vectorizer.fit_transform([str1, str2]).toarray()
    '''
        fit_transform([str1, str2]): Genera una matriz donde cada fila representa una cadena y cada columna un n-grama.
        .toarray(): Convierte la matriz en un arreglo NumPy.

        [
        [1, 1, 1, 0],  # "casa" → "ca", "as", "sa" (sin "so")
        [1, 1, 0, 1]   # "caso" → "ca", "as", "so" (sin "sa")
        ]


    '''
    print(ngram_matrix)



    # Calculamos la similitud de Jaccard
    dissimilarity = jaccard(ngram_matrix[0], ngram_matrix[1])
    '''
        jaccard(ngram_matrix[0], ngram_matrix[1]) calcula dis-similitud de Jaccard entre las dos cadenas.
        Dis-similitud Jaccard va de 0 (idénticos) a 1 (completamente diferentes).
    '''

    return dissimilarity

# Ejemplo de uso
cadena1 = "casa"
cadena2 = "caso"

jaccard_sim = 1- jaccard_dissimilarity(cadena1, cadena2, n=2)
'''
    Similitud de Jaccard = 1 − Dis-similitud de Jaccard
'''
print(jaccard_sim)
