# %% [markdown]
# **Task 06: Modifying RDF(s)**

# %%
!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

# %% [markdown]
# Read the RDF file as shown in class

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

# %% [markdown]
# Create a new class named Researcher

# %%
ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.1: Create a new class named "University"**
# 

# %%
# TO DO
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# %%
# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

# %%
# TO DO
g.add((ns.JaneSmith,RDF.type,ns.Researcher))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**

# %%
# TO DO
from rdflib import XSD
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.JaneSmith, vcard.Email, Literal('jane.smith@email.com', datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.Family, Literal('Smith', datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.Given, Literal('Jane', datatype=XSD.string)))
g.add((ns.JaneSmith, vcard.FN, Literal('Jane Smith', datatype=XSD.string)))
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# %% [markdown]
# **TASK 6.5: Add UPM as the university where John Smith works**

# %%
# TO DO
g.add((ns.UPM,RDF.type,ns.University))
g.add((ns.Work,RDF.type,RDFS.Class))
g.add((ns.JohnSmith,ns.Work,ns.UPM))
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# %% [markdown]
# **Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**

# %%
# TO DO
from rdflib import FOAF
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
g.add((ns.JohnSmith, FOAF.knows,ns.JaneSmith) )
# Visualize the results
for s, p, o in g:
  print(s,p,o)



