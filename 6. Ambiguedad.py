import nltk

# Descargar recursos necesarios (si no los tienes ya)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk import word_tokenize, pos_tag

# Oración de ejemplo ambigua
sentence = "I saw a man with a telescope."

# Tokenización y etiquetado gramatical
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

print("Tokens:", tokens)
print("Etiquetas gramaticales:", pos_tags)
