import nltk
from nltk.tokenize import word_tokenize

# Frase de entrada para el análisis léxico
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenización de palabras
tokens = word_tokenize(sentence)

# Imprimir los tokens
for token in tokens:
    print(token)
