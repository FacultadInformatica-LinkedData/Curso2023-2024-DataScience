!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")


query_str = """
SELECT ?subclass
WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing .
}
"""

q1 = prepareQuery(query_str, initNs={"ns": ns, "rdfs": RDFS})




# Visualize the results

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

query_str = """
SELECT ?person
WHERE {
    ?person a/rdfs:subClassOf* ns:Person .
}
"""

q2 = prepareQuery(query_str, initNs={"ns": ns, "rdfs": RDFS})
results = g.query(q2)

# Visualize the results
for r in g.query(q2):
    print(r)

"""**TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**

"""

# TO DO

query_str = """
SELECT ?individual ?property ?value ?class
WHERE {
    ?individual a ?class .
    FILTER (?class = ns:Person || ?class = ns:Animal)
    ?individual ?property ?value .
}
"""

q3 = prepareQuery(query_str, initNs={"ns": ns})

# Visualize the results
for r in g.query(q3):
    print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky**"""

# TO DO

query_str = """
SELECT ?personName
WHERE {
    ?person a ns:Person ;
            ns:knows ?otherPerson .
    ?otherPerson ns:Given "Rocky" .
    ?person ns:Given ?personName .
}
"""


q4 = prepareQuery(query_str, initNs={"ns": ns})

# Visualize the results
for r in g.query(q4):
    print(r)

"""**Task 7.5: List the entities who know at least two other entities in the graph**"""

# TO DO

query_str = """
SELECT ?entity ?knownEntities
WHERE {
    ?entity a ?class .
    FILTER (?class = ns:Person || ?class = ns:Animal)
    ?entity ns:knows ?knownEntity1 .
    ?entity ns:knows ?knownEntity2 .
    FILTER (STR(?knownEntity1) < STR(?knownEntity2))
    BIND(CONCAT(STR(?knownEntity1), ", ", STR(?knownEntity2)) AS ?knownEntities)
}
"""


q5 = prepareQuery(query_str, initNs={"ns": ns})


# Visualize the results
for r in g.query(q5):
    print(r)
