#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"


# First let's read the RDF file

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# In[3]:


print(g.serialize(format="ttl"))


# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# In[4]:


q1 = """select distinct ?sub 
where
{
?sub rdfs:subClassOf ns:LivingThing.
}"""

# Visualize the results
for r in g.query(q1):
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[5]:


q2 = """select distinct ?individuals 
where
{
{?individuals a ns:Person.}
union
{?sub rdfs:subClassOf ns:Person. ?individuals a ?sub}
}"""

# Visualize the results
for r in g.query(q2):
  print(r)


# **TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**
# 

# In[6]:


q3 = """select distinct ?individuals ?property
where
{
?sub rdfs:subClassOf ns:LivingThing.
?individuals a ?sub.
?individuals ?property ?value.
}"""

# Visualize the results
for r in g.query(q3):
  print(r)


# **TASK 7.4:  List the name of the persons who know Rocky**

# In[9]:


q4 = """select ?individuals
where
{
?individuals foaf:knows ns:RockySmith.
}"""

# Visualize the results
for r in g.query(q4):
  print(r)


# **Task 7.5: List the entities who know at least two other entities in the graph**

# In[18]:


q5 = """select distinct ?individuals
where
{
?individuals foaf:knows ?x.
?individuals foaf:knows ?y.
filter(?x != ?y).
}"""

# Visualize the results
for r in g.query(q5):
  print(r)

