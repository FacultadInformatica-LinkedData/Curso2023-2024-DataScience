# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZFvzw46Pc2yd54C6o-mtoqFx1ptHPDxK

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
# RDFLib
ns = Namespace("http://somewhere#")
def subclass_LivThing(obj):
  hijo = g.triples((None, RDFS.subClassOf, obj))
  if hijo is not None:
    for s, p, o in hijo:
      print(s)
      subclass_LivThing(s)

subclass_LivThing(ns.LivingThing)


# SPARQL
from rdflib.plugins.sparql import prepareQuery
q1=prepareQuery('''
SELECT ?subject
where{
?subject rdfs:subClassOf* ns:LivingThing.
}
''',
    initNs={"rdfs":RDFS, "ns":ns}
)
for r in g.query(q1):
  print(r)

# Visualize the results


"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# RDFLib
def individuals(obj):
  tipo = g.triples((None, RDF.type, obj))
  if tipo is not None:
    for s1, p1, o1 in tipo:
      print(s1)

  subclass = g.triples((None, RDFS.subClassOf, obj))
  if subclass is not None:
    for sHijo, pHijo, oHijo in subclass:
      individuals(sHijo)

individuals(ns.Person)

print("\n")

# SPARQL
q2=prepareQuery('''
SELECT ?subject
where{
?subject rdf:type/rdfs:subClassOf* ns:Person
}
''',
    initNs={"rdf":RDF, "ns":ns}
)

for r in g.query(q2):
  print(r)

# Visualize the results


"""**TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**

"""

# TO DO
# RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  sujeto=s
  for subj,pred,obj in g.triples((sujeto, None, None)):
    print(subj,pred,obj)

for s1,p1,o1 in g.triples((None, RDF.type, ns.Animal)):
  subject=s1
  for s2,p2,o2 in g.triples((subject, None, None)):
    print(s2,p2,o2)

print("\n")

# SPARQL
q3=prepareQuery('''
SELECT ?subject ?properties
where{
  {
    ?subject rdf:type ns:Person.
    ?subject ?properties ?object
  }
  UNION
  {
    ?subject rdf:type ns:Animal.
    ?subject ?properties ?object    
  }
}
''',
    initNs={"rdf":RDF, "ns":ns}
)


for m in g.query(q3):
  print(m)

# Visualize the results


"""**TASK 7.4:  List the name of the persons who know Rocky**"""

# TO DO
# RDFLib
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
VCARD= Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

for s,p,o in g.triples((None, FOAF.knows, ns.RockySmith)):
  for s1,p1,o1 in g.triples((s, VCARD.Given, None)):
    print(o1)


# SPARQL
q4=prepareQuery('''
SELECT ?name
where{
  ?subject FOAF:knows ns:RockySmith.
  ?subject <http://www.w3.org/2001/vcard-rdf/3.0/Given> ?name
}
''',
    initNs={"FOAF": FOAF, "ns":ns}
)

for t in g.query(q4):
  print(t)
# Visualize the results


"""**Task 7.5: List the entities who know at least two other entities in the graph**"""

# TO DO
# RDFLib
from typing import Dict
diccionario:Dict[str, int]={}
for s,p,o in g.triples((None, FOAF.knows, None)):
  if s in diccionario:
    diccionario[s] +=1
  else:
    diccionario[s]=1
for nombre in diccionario:
  if diccionario[nombre]>=2:
    resultado=nombre
    print(resultado)

# SPARQL
q5 = prepareQuery('''
SELECT ?entidades
where{
  ?entidades FOAF:knows ?persona
    }
group by ?entidades
having (COUNT(?persona) >= 2)
''', 
    initNs = {"FOAF":FOAF}
)

for j in g.query(q5):
  print(j)
# Visualize the results

# Visualize the results
