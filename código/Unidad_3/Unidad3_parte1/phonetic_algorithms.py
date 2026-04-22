#pip install metaphone fuzzy
import fuzzy  # Para NYSIIS
from metaphone import doublemetaphone  # Para Metaphone
from fuzzy import Soundex  # Para Soundex

def apply_soundex(word):
    """
       Aplica el algoritmo Soundex a una palabra.
       La biblioteca fuzzy en Python requiere un argumento al inicializar Soundex()
    """
    soundex = fuzzy.Soundex(4)
    return soundex(word)

def apply_metaphone(word):
    """Aplica el algoritmo Metaphone a una palabra."""
    return doublemetaphone(word)  # Devuelve una tupla (primario, alternativo)

def apply_nysiis(word):
    """Aplica el algoritmo NYSIIS a una palabra."""
    return fuzzy.nysiis(word)

# Ejemplos de palabras
words = ["Alberto", "Halberto", "Joshua", "Yoshua", "Marlene", "Marlen"]

print(f"{'Word':<12}{'Soundex':<8}{'Metaphone (P)':<15}{'Metaphone (A)':<15}{'NYSIIS'}")

for word in words:
    soundex_code = apply_soundex(word)
    metaphone_primary, metaphone_alt = apply_metaphone(word)
    nysiis_code = apply_nysiis(word)

    print(f"{word:<12}{soundex_code:<8}{metaphone_primary:<15}{repr(metaphone_alt):<15}{nysiis_code}")
