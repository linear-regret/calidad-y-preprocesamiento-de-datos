from fuzzywuzzy import fuzz, process
import Levenshtein

# Comparar dos cadenas de texto
print(fuzz.ratio("Luis", "Luis "))  # Maneja diferencias leves en los nombres
print(fuzz.ratio("Luis", "Luisillo"))  # Evalúa similitud en términos de caracteres
