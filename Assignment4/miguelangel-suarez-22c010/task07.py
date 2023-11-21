# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hc8PzbJgagETnLnGmRsNR7_mehxY1nw6

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

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
"""With RDFLib"""
def list_subclass(x) -> None:
    triplets = g.triples((None, RDFS.subClassOf, x))
    if triplets is not None:
        for s, p, o in tripletaResult:
          print(s)
          list_subclass(s)
list_subclass(ns.LivingThing)

"""With SPARQL"""
q1 = prepareQuery("SELECT ?x WHERE {?x rdfs:subClassOf* ns:LivingThing}", initNs = {"rdfs":RDFS, "ns":ns})

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

"""With RDFLib"""
def list_individuos(x) -> None:
    instancia = g.triples((None, RDFS.type, x))
    if instancia is not None:
        for s, p, o in i:
            print(s)
    subclass = g.triples((None, RDFS.subClassOf, x))
    if subclass is not None:
        for s2, p2, o2 in subclass:
            list_individuos(s2)
list_individuos(ns.Person)

"""With SPARQL"""
q1 = prepareQuery("SELECT  DISTINCT ?x WHERE {?x rdf:type/rdfs:subClassOf* ns:Person}", initNs = {"rdf":RDF, "ns":ns})

for r in g.query(q1):
  print(r)

"""**TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**

"""

"""With RDFLib"""
def ind_proper(x) ->None:
    triplets = g.triples((None, RDF.type, objeto))
    if triplets is not None:
        for elem, p, o in triplets:
            proper = g.triples((elem, None, None))
            if proper is not None:
                for s2, p2, o2 in proper:
                    print(elem, p2, o2)

ind_proper(ns.Person)
ind_proper(ns.Animal)

"""With SPARQL"""
q1 = prepareQuery('''
    SELECT ?x ?relacion
    WHERE{
    {
            ?x rdf:type ns:Animal.
            ?x ?relacion ?o
            }
            UNION
            {
            ?x rdf:type ns:Person.
            ?x ?relacion ?o
            }

    }''', initNs = {"rdf": RDF, "ns": ns}
)
for r in g.query(q1):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky**"""

"""With RDFLib"""
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
for persona,p,o in g.triples((None, FOAF.knows, ns.RockySmith)):
    print(persona)

"""With SPARQL"""
q1 = prepareQuery('''
    SELECT DISTINCT ?nombre
    WHERE{
            ?x FOAF:knows ns:RockySmith.
            ?x <http://www.w3.org/2001/vcard-rdf/3.0/Given> ?nombre
    }''', initNs = {"ns": ns, "FOAF":FOAF}
    )
for r in g.query(q1):
  print(r)

"""**Task 7.5: List the entities who know at least two other entities in the graph**"""

"""With RDFLib"""
diccionario = {}
lista = []
for s,p,o in g.triples((None, FOAF.knows, None)):
  if s in diccionario:
    diccionario[s] += 1
  else:
    diccionario[s] = 0
for clave, valor in diccionario.items():
    if valor >= 2:
        lista.append(clave)
print(lista)

"""With SPARQL"""
q1 = prepareQuery('''
    SELECT ?x
    WHERE {
        ?x FOAF:knows ?persona
    }
    GROUP BY ?x
    HAVING (COUNT(?persona) >= 2)
    LIMIT 100
    ''', initNs = {"ns": ns, "FOAF":FOAF}
    )
for r in g.query(q1):
  print(r)
