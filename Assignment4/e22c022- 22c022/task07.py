# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tLKNRI9Pvg8c-QPnSxTQ0MMjnk6U1zSN

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

ns = Namespace("http://somewhere#")
from rdflib.plugins.sparql import prepareQuery

#RDFLib

from rdflib import RDF, RDFS

def sc(g, class_name):
    scs = set()
    for s, p, o in g.triples((None, RDF.type, RDFS.Class)):
        if (s, RDFS.subClassOf, class_name) in g:
            scs.add(s)
            scs.update(sc(g, s))
    return scs

subclasses_lt = sc(g, ns.LivingThing)

for subclass in subclasses_lt:
    print(subclass)

#SPARQL

query1 = """
SELECT ?subclass
WHERE {
    ?subclass rdfs:subClassOf* ns:LivingThing .
}
"""

#Visualize the results

for r in g.query(query1):
    print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

#RDFLib

for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)
for s1,p1,o1 in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s2,p2,o2 in g.triples((None, RDF.type, s1)):
    print(s2)

#SPARQL

query2 = """
SELECT distinct ?person
WHERE
{
    {
      ?person rdf:type ns:Person.
    }
    UNION
    {
      ?subclass rdfs:subClassOf* ns:Person.
      ?person a ?subclass.
    }
}
"""

#Visualize the results

for r in g.query(query2):
  print(r)

"""**TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**

"""

# TO DO

#RDFLib

for s,p,o in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s, None, None)) :
    print (s1, p1, o1)
for s,p,o in g.triples((None, RDF.type, ns.Animal)):
  for s1, p1, o1 in g.triples((s1, None, None)) :
    print (s1, p1, o1)

#SPARQL

query3 = '''
SELECT DISTINCT ?person ?property ?value
WHERE
{
    {
        ?person rdf:type ns:Person.
        ?person ?property ?value.
    }
    UNION
    {
        ?person rdf:type ns:Animal.
        ?person ?property ?value.
    }
}
'''

# Visualize the results

for r in g.query(query3):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky**"""

# TO DO

from rdflib import FOAF

#RDFLib

for s,p,o in g.triples((None, FOAF.knows, ns.RockySmith)) :
    print (s)

#SPARQL

query4 = '''
SELECT ?personName
WHERE {
    ?person a ns:Person ;
            ns:knows ?otherPerson.
    ?otherPerson ns:name "Rocky".
    ?person ns:name ?personName.
}
'''

# Visualizar los resultados
for r in g.query(query4):
    print(r)

"""**Task 7.5: List the entities who know at least two other entities in the graph**"""

# TO DO

#RDFLib

contador = {}
for s,p,o in g.triples((None, FOAF.knows, None)):
    contador[s] = contador.get(s, 0)+1
entidades = []
for key, value in contador.items():
    if value >= 2:
        entidades.append(key)
print(entidades)

#SPARQL

query5 = prepareQuery('''
 SELECT ?entity
  WHERE {
    ?entity FOAF:knows ?entity2
  }
  GROUP BY ?entity
  HAVING (COUNT(?entity2) >= 2)
  ''',
  initNs = {"FOAF":FOAF}
)   

# Visualize the results

for r in g.query(query5):
    print(r.entity)
