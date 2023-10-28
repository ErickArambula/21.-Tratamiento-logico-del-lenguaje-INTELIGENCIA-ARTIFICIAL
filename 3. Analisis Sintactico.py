import nltk

# Frase de entrada para el análisis sintáctico
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenización de palabras
tokens = nltk.word_tokenize(sentence)

# Análisis sintáctico utilizando la gramática en inglés
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> DT JJ NN
    VP -> V NP
    DT -> 'The'
    JJ -> 'quick' | 'brown' | 'lazy'
    NN -> 'fox' | 'dog'
    V -> 'jumps' | 'over'
""")

parser = nltk.ChartParser(grammar)

# Realizar el análisis sintáctico
for tree in parser.parse(tokens):
    tree.pretty_print()
