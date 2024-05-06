import nltk
from nltk.corpus import treebank
from nltk import Nonterminal, Production, induce_pcfg
from nltk.parse import pchart

# Descargar los recursos necesarios de NLTK (solo se necesita hacer una vez)
nltk.download('treebank')

# Obtener las producciones del corpus de Treebank
productions = []
for tree in treebank.parsed_sents():
    productions += tree.productions()

# Crear una lista de instancias de Produccion
productions = [Production(production.lhs(), production.rhs()) for production in productions]

# Inducir una gramatica PCFG a partir de las producciones
pcfg = induce_pcfg(Nonterminal('S'), productions)

# Mostrar algunas estadisticas basicas de la gramatica
print("Numero total de producciones:", len(productions))
print("Numero total de simbolos no terminales:", len(pcfg._lhs_index.keys()))
print("Numero total de simbolos terminales:", len(pcfg._rhs_index.keys()))

# Generar una oracion aleatoria usando la gramatica PCFG
parser = pchart.InsideChartParser(pcfg)
for t in parser.parse(pcfg.start()):
    print("Oracion generada:", " ".join(t.leaves()))
    break  # Solo imprimimos una oracion generada

