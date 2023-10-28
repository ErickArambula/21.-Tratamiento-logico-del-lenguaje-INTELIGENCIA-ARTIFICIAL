import nltk
from nltk import CFG

# Definir una gramática libre de contexto
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Crear un analizador sintáctico basado en la gramática
parser = nltk.ChartParser(grammar)

# Frase de entrada para analizar
sentence = "the dog chased a cat"

# Analizar la frase
for tree in parser.parse(sentence.split()):
    tree.pretty_print()
