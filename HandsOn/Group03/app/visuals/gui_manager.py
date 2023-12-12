import pandas as pd
from ipywidgets import widgets
import random
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
import sys
from SPARQLWrapper import TURTLE, SPARQLWrapper, JSON

def reset_cbox(button, cbox):
    cbox.value = ''

def get_barrio_names(graph, dict_namespaces):
    info = {
        "barrio_names" : [],
        "wiki_ids" : [],
        "barrio_ids" : []
    }
    q = prepareQuery(
    '''
    SELECT ?Neighborhood_names ?Neighborhood_id ?wiki_id
    WHERE {
        ?Neighborhood_id rdf:type dog-loc:Neighborhood .
        ?Neighborhood_id rdfs:label ?Neighborhood_names .
        ?Neighborhood_id owl:sameAs ?wiki_id .
    }
    ''',
    initNs=dict_namespaces
    )

    results = list(graph.query(q))
    
    if not results:
        print("No results found.")
    else:
        for r in results:
            # print(r.Neighborhood_names, r.wiki_id)
            info["barrio_names"].append(str(r.Neighborhood_names))
            info["wiki_ids"].append(r.wiki_id)
            info["barrio_ids"].append(r.Neighborhood_id)
    return info
    # print(user_choice.Neighborhood_names, user_choice.wiki_id)

def get_wiki_data(user_choice):
    endpoint_url = "https://query.wikidata.org/sparql"

    query = f"""SELECT ?property ?propertyLabel ?value ?valueLabel 
    WHERE {{
    <{user_choice}> wdt:P1082 ?value.
    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}"""
    results = get_results(endpoint_url, query)
    # for result in results["results"]["bindings"]:
    #     print(result["value"]["value"])
    return results["results"]["bindings"][0]["value"]["value"]

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])

    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    # sparql.setReturnFormat(TURTLE)
    return sparql.query().convert()

def get_center_address(graph, dict_namespaces, district_id):
    showList =  []

    q3 = prepareQuery(
    f'''
    SELECT ?address_id ?streetName ?streetNumber 
    WHERE {{
        ?address_id dog-loc:hasNeighborhood <{district_id}> .
        ?address_id dog-loc:onThoroughfare ?streetName .
        ?address_id dog-loc:hasStreetNumber ?streetNumber .
    }}
    ''',
    initNs=dict_namespaces
    )

    results_care = list(graph.query(q3))

    if not results_care:
        showList.append("No care centers found ")
    else:
        for r in results_care:
           showList.append(f"{str(r.streetName)}, {str(r.streetNumber)}")
    return showList