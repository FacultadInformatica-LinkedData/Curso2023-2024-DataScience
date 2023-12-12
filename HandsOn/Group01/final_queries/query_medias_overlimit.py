def overlimit(G):
    q1 = '''

            prefix ns: <http://pittsburgh.linkeddata.es/traffic/ontology/ont1#>
            prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
            prefix db: <http://dbpedia.org/resource/classes#>
            prefix m3: <http://purl.org/iot/vocab/m3-lite#>
            prefix w3: <https://www.w3.org/2006/time#>
            prefix dc: <http://purl.org/dc/terms/>
            prefix owl: <http://www.w3.org/2002/07/owl#>
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            prefix xsd: <http://www.w3.org/2001/XMLSchema#>
            prefix rr: <http://www.w3.org/ns/r2rml#>
            prefix rml: <http://semweb.mmlab.be/ns/rml#>
            prefix ql: <http://semweb.mmlab.be/ns/ql#>
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

             SELECT DISTINCT  ?district ?x WHERE {
                 ?sensor ns:locatedIn ?district .       

             }
      '''
    q1_res = G.query(q1)
    distritos = []
    medias = []
    for i in range(len(q1_res)):
        distritos += [i]
        medias += [0]
    k = 0

    for r, p in q1_res:
        distritos[k] = str(r)
        medias[k] = 0

        q2_1 = '''

                prefix ns: <http://pittsburgh.linkeddata.es/traffic/ontology/ont1#>
                prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
                prefix db: <http://dbpedia.org/resource/classes#>
                prefix m3: <http://purl.org/iot/vocab/m3-lite#>
                prefix w3: <https://www.w3.org/2006/time#>
                prefix dc: <http://purl.org/dc/terms/>
                prefix owl: <http://www.w3.org/2002/07/owl#>
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix xsd: <http://www.w3.org/2001/XMLSchema#>
                prefix rr: <http://www.w3.org/ns/r2rml#>
                prefix rml: <http://semweb.mmlab.be/ns/rml#>
                prefix ql: <http://semweb.mmlab.be/ns/ql#>
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

                 SELECT ?sensor ?x WHERE {
                     ?sensor ns:locatedIn <'''

        q2_2 = '''>.
                     ?sensor ns:takes ?measurement .
                     ?measurement ns:hasStatisticsMeasures ?statistic .
                     ?statistic ns:hasPercentOverLimit ?x.
                }
          '''
        q2 = q2_1 + str(r) + q2_2

        q2_res = G.query(q2)

        for x, num in q2_res:
            medias[k] += int(num)

        medias[k] = medias[k] / len(q2_res)
        k += 1

    return distritos, medias