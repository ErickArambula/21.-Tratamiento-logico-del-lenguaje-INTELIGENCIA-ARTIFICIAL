import nltk
from nltk import CFG

# Conjunto de oraciones de ejemplo
sentences = [
    "The cat sat on the mat.",
    "The dog barked at the mailman.",
    "The sun rises in the east."
]

# Generar una gramática inductiva a partir de las oraciones de ejemplo
def induct_grammar(sentences):
    productions = set()
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tags = nltk.pos_tag(words)
        grammar = CFG.fromstring(tags)
        productions.update(grammar.productions())

    return CFG(tags, list(productions))

# Inducir la gramática
induced_grammar = induct_grammar(sentences)

# Mostrar la gramática inducida
print(induced_grammar)
