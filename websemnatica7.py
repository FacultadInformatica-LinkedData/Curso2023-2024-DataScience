from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse("/rdf/example6.rdf", format="xml")

#1
# Define the SPARQL query
query = prepareQuery("""
    SELECT ?subclass
    WHERE {
        ?subclass rdfs:subClassOf ns:LivingThing .
    }
""")

# Execute the query and print the results
for row in g.query(query):
    print(row.subclass)
#2
q2 = prepareQuery("""
    SELECT ?individual
    WHERE {
        ?individual rdf:type/rdfs:subClassOf* ns:Person .
    }
""")

# Execute the query and print the results
for row in g.query(q2):
    print(row.individual)
#3
# Define the SPARQL query
query = prepareQuery("""
    SELECT ?individual ?property ?value
    WHERE {
        ?individual a/(rdf:subClassOf*)/(rdf:type|rdf:type/rdfs:subClassOf*) ?class ;
                    ?property ?value .
        FILTER (?class = ns:Person || ?class = ns:Animal)
    }
""")

# Execute the query and print the results
for row in g.query(query):
    print("Individual:", row.individual)
    print("Property:", row.property)
    print("Value:", row.value)
    print()
#4
# Define the SPARQL query
query = prepareQuery("""
    SELECT ?personName
    WHERE {
        ?person ns:knows ns:Rocky .
        ?person ns:hasName ?personName .
    }
""")

# Execute the query and print the results
for row in g.query(query):
    print(row.personName)
#5
query = prepareQuery("""
    SELECT ?entity ?knownCount
    WHERE {
        ?entity ns:knows ?known .
        {
            SELECT ?entity (COUNT(?known) AS ?knownCount)
            WHERE {
                ?entity ns:knows ?known .
            }
            GROUP BY ?entity
            HAVING (COUNT(?known) >= 2)
        }
    }
""")

# Execute the query and print the results
for row in g.query(query):
    print(row.entity, row.knownCount)