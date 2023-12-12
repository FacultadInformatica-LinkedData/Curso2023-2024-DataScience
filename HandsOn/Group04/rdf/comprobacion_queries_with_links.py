from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

g=Graph()

g.namespace_manager.bind('base', Namespace("http://deportesMadrid/ontology#"), override=False)
g.namespace_manager.bind('owl', Namespace("http://www.w3.org/2002/07/owl#"), override=False)
g.namespace_manager.bind('rdf', Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"), override=False)

base=Namespace("http://deportesMadrid/ontology#")
owl=Namespace("http://www.w3.org/2002/07/owl#")

g.parse("./rdf/output_tripletas-with-links.nt", format="nt")

# 1. Dado el código postal 28024 devolver los nombres de los polideportivos (que sean distintos) y los id de los aparcabicis de ese código postal.
q1= prepareQuery(
    '''
    SELECT DISTINCT ?nombre_pol ?id_apar
    WHERE {
	    ?loc base:tiene_codigo-postal 28024.
	    ?polideportivo base:se_encuentra_en ?loc.
    	    ?polideportivo base:tiene_nombre ?nombre_pol .
	    ?aparcabicis base:se_encuentra_en ?loc.
    	    ?aparcabicis base:tiene_id ?id_apar.
    }
    GROUP BY ?nombre_pol
    LIMIT 20
    ''',
    initNs={"base":base}
)
for r in g.query(q1):
  print(r)


# 2. Devolver todos los nombres de polideportivos, que sean distintos, y los id de aparcabicis del modelo "MU-51" que estén situados en la misma via y se encuentren en el distrito "Villa de Vallecas".
q2= prepareQuery(
    '''
    SELECT ?nombre ?id_apar ?via
    WHERE {
	    ?loc base:tiene_distrito "Villa de Vallecas".
	    ?polideportivo base:se_encuentra_en ?loc.
            ?polideportivo base:tiene_nombre-numero-via ?via.
    	    ?polideportivo base:tiene_nombre ?nombre.
	    ?aparcabicis base:se_encuentra_en ?loc.
            ?aparcabicis base:tiene_nombre-numero-via ?via.
    	    ?aparcabicis base:tiene_modelo 'MU-51'.
    	    ?aparcabicis base:tiene_id ?id_apar.
    }
    GROUP BY ?nombre
    LIMIT 20
    ''',
    initNs={"base":base}
)
for m in g.query(q2):
  print(m)


# 3. Mostrar el id de los aparcabicis que su clase vial no sea una avenida, el identificador del polideportivo (pk) que este en la misma via que el aparcabicis y mostrar la propia via (sin que se repita la via).
q3= prepareQuery(
    '''
    SELECT ?id_apar ?pk ?via
    WHERE {
        ?aparcabicis base:tiene_clase-vial ?clase.
        FILTER (?clase != "AVENIDA")
        ?aparcabicis base:tiene_id ?id_apar.
        ?aparcabicis base:tiene_nombre-numero-via ?via.
        ?aparcabicis base:se_encuentra_en ?barrio.
        ?polideportivo base:se_encuentra_en ?barrio.
        ?polideportivo base:tiene_nombre-numero-via ?via.
        ?polideportivo base:tiene_pk ?pk.

    }
    GROUP BY ?via
    LIMIT 20
    ''',
    initNs={"base":base}
)
for t in g.query(q3):
  print(t)


# 4. Devuelve los id de los aparcabicis que se pueden encontrar en una calle del barrio Aluche y los nombres de los polideportivos que hay en ese barrio.
q4= prepareQuery(
    '''
    SELECT ?id_apar ?nombre
    WHERE {
        ?loc owl:same_as <http://wikidata.org/entity/Q31140> .
        ?aparcabicis base:se_encuentra_en ?loc.
        ?aparcabicis base:tiene_clase-vial 'CALLE'.
        ?aparcabicis base:tiene_id ?id_apar.
        ?polideportivo base:se_encuentra_en ?loc.
        ?polideportivo base:tiene_nombre ?nombre.
      }
      LIMIT 20    
    ''',
    initNs={"base":base, "owl":owl}
)
for j in g.query(q4):
  print(j)


# 5. Dado la fecha de instalacion 2021-09-21 de los aparcabicis devolver el barrio, junto con su link a wikidata, el estado de los aparcabicis y la url de los polideportivos (sin que se repitan) de ese barrio.
q5= prepareQuery(
    '''
    SELECT ?barrio ?link_barrio ?estado ?url
    WHERE {
	  ?aparcabicis base:tiene_fecha-instalacion '2021-09-21'.
  	  ?aparcabicis base:tiene_estado ?estado.
          ?aparcabicis base:se_encuentra_en ?loc.
          ?loc base:tiene_barrio ?barrio.
          ?loc owl:same_as ?link_barrio.
          ?polideportivo base:se_encuentra_en ?loc.
          ?polideportivo base:tiene_url ?url.
    }
    GROUP BY ?url
    LIMIT 20
    ''',
    initNs={"base":base, "owl":owl}
)
for h in g.query(q5):
  print(h)


# 6. Dado un distrito (Chamartín) y filtrando por el nombre del barrio (Nueva España) devolver el nombre del polideportivo (sin repetirse) y el ID del aparcabicis.
q6= prepareQuery(
    '''
    SELECT ?nombre ?id
    WHERE {
            ?loc base:tiene_distrito "Chamartín".
  	    ?loc owl:same_as <http://wikidata.org/entity/Q10338128>.
	    ?polideportivo base:se_encuentra_en ?loc.
	    ?aparcabicis base:se_encuentra_en ?loc.
 	    ?aparcabicis base:tiene_id ?id.
  	    ?polideportivo base:tiene_nombre ?nombre.
    }
    GROUP BY ?nombre
    LIMIT 20
    ''',
    initNs={"base":base, "owl":owl}
)

for k in g.query(q6):
  print(k)
