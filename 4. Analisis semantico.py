import spacy

# Cargar el modelo de lenguaje en inglés
nlp = spacy.load("en_core_web_sm")

# Frase de entrada para el análisis semántico
sentence = "The quick brown fox jumps over the lazy dog."

# Realizar el análisis semántico
doc = nlp(sentence)

# Extraer información semántica
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}, Dep: {token.dep_}")

# Analizar las entidades nombradas
for ent in doc.ents:
    print(f"Entidad nombrada: {ent.text}, Etiqueta: {ent.label_}")
