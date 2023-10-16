# -*- coding: utf-8 -*-
"""Copia de Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6D06oFAYZbnpZnp7idBHYqZkzkSOdFH

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, FOAF
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
g.add((ns.University, RDF.type, RDFS.Class))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
fullName = Literal("Jane Smith")
EX = Namespace("http://example.org/")
janeURI = ns.JaneSmith
resource = (janeURI ,ns.Researcher, fullName)
g.add(resource)
# Visualize the results
print(resource)
print("----------------------------------------")
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**"""

# TO DO
# Visualize the results
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
email=(janeURI, vcard.EMAIL, Literal('jsmith@example.org'))
g.add(email)
nombre = (janeURI, vcard.FN, Literal("Jane Alex Smith"))
g.add(nombre)

print(email)
print(nombre)
print("-----------------------------------------------------")
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
JohnUri = ns.JohnSmith
UPM_uri = EX.Upm
UPM = (UPM_uri, RDF.type, vcard.University)
relacion = (JohnUri, vcard.WorksAt, UPM_uri)
g.add(relacion)
g.add(UPM)
# Visualize the results
print(relacion)
print(UPM)
print("-------------------------------------------")
for s, p, o in g:
  print(s,p,o)

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**"""

# TO DO
foaf = FOAF
g.add((JohnUri, FOAF.knows, janeURI))
# Visualize the results
for s, p, o in g:
  print(s,p,o)