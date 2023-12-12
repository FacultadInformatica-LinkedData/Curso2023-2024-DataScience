import random
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

dict_namespaces = {
    "rr": Namespace("http://www.w3.org/ns/r2rml#"),
    "rml": Namespace("http://semweb.mmlab.be/ns/ql#"),
    "ql": Namespace("http://vocab.org/transit/terms/"),
    "transit": Namespace("http://www.w3.org/2001/XMLSchema#"),
    "wgs84_pos": Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#"),
    "vocab": Namespace("http://example.org#"),
    "dog-loc": Namespace("https://w3id.org/DogFriendlyMadrid/info/ontology/location#"),
    "dog-det": Namespace("https://w3id.org/DogFriendlyMadrid/info/ontology/details#"),
    "dog-ser": Namespace("https://w3id.org/DogFriendlyMadrid/info/ontology/services#"),
    "schema-org": Namespace("http://schema.org/"),
    "dbo": Namespace("https://dbpedia.org/ontology/"),
    "rdfs": Namespace("http://www.w3.org/2000/01/rdf-schema#"),
    "rdf": Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
    "owl": Namespace("http://www.w3.org/2002/07/owl#")
}

graph_Parks = Graph()
graph_CareCenter = Graph()
graph_DogGarbage = Graph()
graph_DogZone = Graph()
graph_Fountain = Graph()

for shortcut, new_namespace in dict_namespaces.items():
    graph_Parks.namespace_manager.bind(shortcut, new_namespace, override=False)
for shortcut, new_namespace in dict_namespaces.items():
    graph_CareCenter.namespace_manager.bind(shortcut, new_namespace, override=False)
for shortcut, new_namespace in dict_namespaces.items():
    graph_DogGarbage.namespace_manager.bind(shortcut, new_namespace, override=False)
for shortcut, new_namespace in dict_namespaces.items():
    graph_DogZone.namespace_manager.bind(shortcut, new_namespace, override=False)
for shortcut, new_namespace in dict_namespaces.items():
    graph_Fountain.namespace_manager.bind(shortcut, new_namespace, override=False)

graph_Parks.parse("./Parks-with-links.nt", format="nt")
graph_CareCenter.parse("./CareCenters-with-links.nt", format="nt")
graph_DogGarbage.parse("./DogGarbageBins-with-links.nt", format="nt")
graph_DogZone.parse("./DogZones-with-links.nt", format="nt")
graph_Fountain.parse("./FuentesMascotas-with-links_data.nt", format="nt")

# q1 = prepareQuery(
#     '''
#     SELECT ?park_names
#     WHERE {
#         ?park_ids rdf:type schema-org:Park .
#         ?park_ids schema-org:name ?park_names
#     }
#     ''',
#     initNs=dict_namespaces
# )

# results = list(g.query(q1))

# if not results:
#     print("No results found.")
# else:
#     for r in results:
#         print(r.park_names)

# <https://w3id.org/DogFriendlyMadrid/info/ontology/location#District>
q2 = prepareQuery(
    '''
    SELECT ?district_name ?District_id ?wiki_id
    WHERE {
        ?District_id rdf:type dog-loc:District .
        ?District_id rdfs:label ?district_name .
        ?District_id owl:sameAs ?wiki_id .
    }
    ''',
    initNs=dict_namespaces
)

results_1 = list(graph_Parks.query(q2))
# print(results_1)

# if not results_1:
#     print("No results found.")
# else:
#     for r in results_1:
#         print(r.district_name, r.wiki_id)

print("------User Choice")
user_choice =random.choice(results_1) # "https://w3id.org/DogFriendlyMadrid/info/resource/District/Centro"
print(user_choice.district_name, user_choice.wiki_id, user_choice.District_id)

# # pip install sparqlwrapper
# # https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import TURTLE, SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"


query = f"""SELECT ?property ?propertyLabel ?value ?valueLabel 
WHERE {{
<{user_choice.wiki_id}> wdt:P1082 ?value.
SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
}}"""



def get_results(endpoint_url, query):
    user_agent = "DOGCITY Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    return sparql.query().convert()

print("----------WIKIDATA POBLACION")
results = get_results(endpoint_url, query)
for result in results["results"]["bindings"]:
    print(result["value"]["value"])

print("----------CARE CENTER")
q3 = prepareQuery(
    f'''
    SELECT ?center_id ?address_id ?streetName ?streetNumber 
    WHERE {{
        ?address_id dog-loc:hasDistrict <{user_choice.District_id}>.
        # <https://w3id.org/DogFriendlyMadrid/info/resource/District/Retiro> .
        ?address_id dog-loc:onThoroughfare ?streetName .
        ?address_id dog-loc:hasStreetNumber ?streetNumber .
    }}
    ''',
    initNs=dict_namespaces
)

results_care = list(graph_CareCenter.query(q3))

if not results_care:
    print("No results found q3.")
else:
    for r in results_care:
        print(r.streetName, r.streetNumber)

print("----------GARBAGE")
q4 = prepareQuery(
    f'''
    SELECT ?item_id ?address_id ?geoID ?lat ?long
    WHERE {{
        ?address_id dog-loc:hasDistrict <{user_choice.District_id}> .
        ?item_id dog-loc:hasAddress ?address_id .
        ?item_id schema-org:geo ?geoID .
        ?geoID schema-org:latitude ?lat .
        ?geoID schema-org:longitude ?long .

    }}
    ''',
    initNs=dict_namespaces
)

results_care = list(graph_DogGarbage.query(q4))

if not results_care:
    print("No results found q4.")
else:
    for r in results_care:
        # print(r.item_id, r.geoID, r.lat, r.long)
        print(r.lat, r.long)


print("----------FOUNTAIN")
q5 = prepareQuery(
    f'''
    SELECT ?item_id ?address_id ?geoID ?lat ?long
    WHERE {{
        ?address_id dog-loc:hasDistrict <{user_choice.District_id}> .
        ?item_id dog-loc:hasAddress ?address_id .
        ?item_id schema-org:geo ?geoID .
        ?geoID schema-org:latitude ?lat .
        ?geoID schema-org:longitude ?long .

    }}
    ''',
    initNs=dict_namespaces
)

results_care = list(graph_Fountain.query(q5))

if not results_care:
    print("No results found q5.")
else:
    for r in results_care:
        # print(r.item_id, r.geoID, r.lat, r.long)
        print(r.lat, r.long)

print("----------PARKS")
q6 = prepareQuery(
    f'''
    SELECT ?item_id ?address_id ?geoID ?lat ?long
    WHERE {{
        ?address_id dog-loc:hasDistrict <{user_choice.District_id}> .
        ?item_id dog-loc:hasAddress ?address_id .
        ?item_id schema-org:geo ?geoID .
        ?geoID schema-org:latitude ?lat .
        ?geoID schema-org:longitude ?long .

    }}
    ''',
    initNs=dict_namespaces
)

results_care = list(graph_Parks.query(q6))

if not results_care:
    print("No results found q6.")
else:
    for r in results_care:
        # print(r.item_id, r.geoID, r.lat, r.long)
        print(r.lat, r.long)
print("----------DOG ZONE")
q7 = prepareQuery(
    f'''
    SELECT ?center_id ?address_id ?streetName ?streetNumber 
    WHERE {{
        ?address_id dog-loc:hasDistrict <{user_choice.District_id}> .
        ?address_id dog-loc:onThoroughfare ?streetName .
        ?address_id dog-loc:hasStreetNumber ?streetNumber .
    }}
    ''',
    initNs=dict_namespaces
)

results_care = list(graph_DogZone.query(q7))

if not results_care:
    print("No results found q7.")
else:
    for r in results_care:
        print(r.address_id, r.streetNumber)