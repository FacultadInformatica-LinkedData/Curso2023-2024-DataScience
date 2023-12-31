# -*- coding: utf-8 -*-
"""Copia de Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHw4gKzVMd9gEDx8i9hPEdPvRiUhN7GS

**Task 07: Querying RDF(s)**
"""

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
# Visualize the results


from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
q1 = """
SELECT distinct ?subclass
WHERE {
    ?subclass rdfs:subClassOf* ns:LivingThing .
}
"""
for s,p,o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):
    print(s)
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results
query_str = """
SELECT ?person
WHERE {
    ?person a/rdfs:subClassOf* ns:Person .
}
"""
q2 = prepareQuery(query_str, initNs={"ns": ns, "rdfs": RDFS})
results = g.query(q2)
for row in results:
  print(row)
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s, None, None)) :
    print (s1, p1, o1)
for s, p, o in g.triples((None, RDF.type, ns.Animal)):
  for s1, p1, o1 in g.triples((s, None, None)) :
    print (s1, p1, o1)

"""**TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**

"""

# TO DO
# Visualize the results
query_str = """
SELECT ?individual ?property ?value ?class
WHERE {
    ?individual a ?class .
    FILTER (?class = ns:Person or ?class = ns:Animal)
    ?individual ?property ?value .
}
"""
q3 = prepareQuery(query_str, initNs={"ns": ns})
results = g.query(q3)
for row in results:
  print(row)
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s, None, None)) :
    print (s1, p1, o1)
for s, p, o in g.triples((None, RDF.type, ns.Animal)):
  for s1, p1, o1 in g.triples((s, None, None)) :
    print (s1, p1, o1)
      
"""**TASK 7.4:  List the name of the persons who know Rocky**"""

# TO DO
# Visualize the results
query_str = """
SELECT ?personName
WHERE {
    ?person a ns:Person ; ns:knows
    ?otherPerson .
    ?otherPerson ns:name "Rocky" .
    ?person ns:name ?personName .
}
"""
q4 = prepareQuery(query_str, initNs={"ns": ns})
results = g.query(q4)
for row in results:
  print(row)
for s, p, o in g.triples((None, FOAF.knows, ns.Rocky)):
  print(s)
    
"""**Task 7.5: List the entities who know at least two other entities in the graph**"""

# TO DO
# Visualize the results
query_str = """
SELECT ?entity ?knownEntities
WHERE {
    ?entity a ?class .
    FILTER (?class = ns:Person || ?class = ns:Animal)
    ?entity ns:knows ?knownEntity1 .
    ?entity ns:knows ?knownEntity2 .
    FILTER (entity1!= entity2)
    BIND(CONCAT(STR(?knownEntity1), ", ", STR(?knownEntity2)) AS ?knownEntities)
}
"""
q5 = prepareQuery(query_str, initNs={"ns": ns})
results = g.query(q5)
for row in results:
  print(row)

for s,p,o in g.triples((None, FOAF.knows, None)):
    entities = []
    if s in entities:
        print(s)
    entities += [s]
