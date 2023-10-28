from pyparsing import Word, alphas, OneOrMore, ZeroOrMore, Literal, Forward, infixNotation

# Definición de gramática causal
AND = Literal("and")
THEN = Literal("then")
IF = Literal("if")
OPERATORS = ["and", "then"]
expr = Forward()
identifier = Word(alphas)
operand = identifier.setResultsName("operand")
relation = infixNotation(operand, [
    (AND, 2, 1, 1),
    (THEN, 2, 1, 1),
])
causal_statement = IF + relation + THEN + operand

# Oración de ejemplo con relación causal
sentence = "if A and B then C"

# Análisis de la oración
result = causal_statement.parseString(sentence)

# Extraer información de la relación causal
causes = result[1]
effect = result[3]

print(f"Causas: {', '.join(causes)}")
print(f"Efecto: {effect}")
