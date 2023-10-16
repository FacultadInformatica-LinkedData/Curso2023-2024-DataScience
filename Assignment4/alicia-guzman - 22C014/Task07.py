#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[5]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"


# First let's read the RDF file

# In[22]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# In[16]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# with RDFlib
for s, p, o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):
    print(s)

# with SPARQL
q1 = prepareQuery('''
   SELECT ?Subject WHERE { 
      ?Subject rdfs:subClassOf ns:LivingThing.
    } 
    ''',
    initNs={"rdfs": RDFS, "ns": ns}
)

# Visualize the SPARQL results
for r in g.query(q1):
  print(r.Subject)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[31]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# with RDFlib
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)

# with SPARQL
q2 = prepareQuery('''
   SELECT ?Subject WHERE { 
        ?Subject rdf:type ns:Person .
    } 
    ''',
    initNs = {"rdf": RDF, "ns": ns}
)

q3 = prepareQuery('''
   SELECT ?Subject WHERE { 
      ?Subject rdf:type ?person . 
      ?person rdfs:subClassOf ns:Person .
    } 
    ''',
    initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)

# Visualize the SPARQL results
for r in g.query(q2):
  print(r.Subject)
for r in g.query(q3):
  print(r.Subject)

# Visualize the results


# **TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**
# 

# In[36]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# with RDFlib

for s,p,o in g.triples((None, RDF.type, ns.Person or ns.Animal)):
  for s2,p2,o2 in g.triples((s, None, None)):
    print(s2,p2)

for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person or ns.Animal)):  
  for s2,p2,o2 in g.triples((None, RDF.type, s)):
    for s3,p3,o3 in g.triples((s2, None, None)):
      print(s2,p2)


# with SPARQL
q4 = prepareQuery('''
   SELECT ?Subject ?prop WHERE { 
      ?Subject rdf:type ns:Person || ns:Animal .
      ?Subject ?prop ?value .
    } 
    ''',
    initNs = {"rdf": RDF, "ns": ns}
)

q5 = prepareQuery('''
   SELECT ?Subject ?prop WHERE { 
      ?Subject rdf:type ?person .
      ?person rdfs:subClassOf ns:Person || ns:Animal .
      ?Subject ?prop ?value .
    } 
    ''',
    initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)

# Visualize the results
for r in g.query(q4):
  print(r.Subject)
for r in g.query(q5):
  print(r.Subject)


# **TASK 7.4:  List the name of the persons who know Rocky**

# In[32]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# with RDFlib
from rdflib import  FOAF
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.Jown,VCARD.knows,FOAF.Person))
for s, p, o in g:
  print(s,p,o)

# with SPARQL
q6 = prepareQuery('''
   SELECT ?personName WHERE { 
        ?person a ns:Person ; ns:knows
        ?otherPerson .
        ?otherPerson ns:name "Rocky" .
        ?person ns:name ?personName .
        ?personName foaf:knows ns:RockySmith.
    } 
    ''',
    initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)


# Visualize the results
for r in g.query(q6):
    print(r)


# **Task 7.5: List the entities who know at least two other entities in the graph**

# In[35]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

# with RDFlib
from rdflib import  FOAF
g.add((ns.Entity,FOAF.knows,ns.Entity1))
g.add((ns.Entity,FOAF.knows,ns.Entity2))

for s, p, o in g:
  print(s,p,o)

# with SPARQL
q7 = prepareQuery('''
   SELECT ?entity ?knownEntities WHERE { 
        ?entity a ?class .
        ?entity ns:knows ?knownEntity1 .
        ?entity ns:knows ?knownEntity2 .
    } 
    ''',
    initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)

# Visualize the results
for r in g.query(q7):
    print(r)

