# -*- coding: utf-8 -*-
"""task06corr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ae7L9n7c0SdciOeRBIdUna_VRiigeH0F

**Task 06: Modifying RDF(s)**

Daniel LLopis, 21C033
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
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
# Visualize the results
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
# Visualize the results
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

g.add((ns.JaneSmith, RDF.type, ns.Researcher))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**"""

# TO DO
# Visualize the results

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

email_address = Literal("janesmith@gmail.com")
g.add((ns.JaneSmith, VCARD.EMAIL, email_address))

full_name = Literal("Jane Smith")
g.add((ns.JaneSmith, VCARD.FN, full_name))

given_name = Literal("Jane")
g.add((ns.JaneSmith, VCARD.Given, given_name))

family_name = Literal("Smith")
g.add((ns.JaneSmith, VCARD.Family, family_name))

for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
# Visualize the results

work_space = Literal("UPM")
g.add((ns.JhonSmith, ns.WorkSpace, work_space))

for s, p, o in g:
    print(s, p, o)

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**"""

# TO DO
# Visualize the results

from rdflib import FOAF

g.add((ns.JohnSmith, FOAF.knows, ns.JaneSmith))

for s, p, o in g:
  print(s,p,o)