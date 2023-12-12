import webbrowser
from statistics import quantiles
import tkinter as tk
import folium
import morph_kgc
from rdflib import Graph


config = "config.ini"
G = Graph()
G = morph_kgc.materialize(config)


def average_daily_traffic_percen(G):
    q_1 = '''

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
                            ?traffic ns:hasDailyCarTraffic ?x.
                            }
                        '''
    q = G.query(q_1)
    lista = []
    for i in range(len(q)):
        lista += [0]
    k=0
    for s, m in q:
        lista[k] = int(m)
        k+=1
    datos = sorted(lista)
    percentil = quantiles(datos, n=4)

    return percentil


def overlimit_percen(G):
    q_1 = '''

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
                            ?traffic ns:hasPercentOverLimit ?x.
                            }
                        '''
    q = G.query(q_1)
    lista = []
    for i in range(len(q)):
        lista += [0]
    k=0
    for s, m in q:
        lista[k] = int(m)
        k+=1
    datos = sorted(lista)
    percentil = quantiles(datos, n=4)

    return percentil


def speed85_percen(G):
    q_1 = '''

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
                            ?traffic ns:hasSpeed85Percent ?x.
                            }
                        '''
    q = G.query(q_1)
    lista = []
    for i in range(len(q)):
        lista += [0]
    k=0
    for s, m in q:
        lista[k] = int(m)
        k+=1
    datos = sorted(lista)
    percentil = quantiles(datos, n=4)

    return percentil


def speed95_percen(G):
    q_1 = '''

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
                            ?traffic ns:hasSpeed95Percent ?x.
                            }
                        '''
    q = G.query(q_1)
    lista = []
    for i in range(len(q)):
        lista += [0]
    k=0
    for s, m in q:
        lista[k] = int(m)
        k+=1
    datos = sorted(lista)
    percentil = quantiles(datos, n=4)

    return percentil



def peligrosidad(G, v1, v2, v3, v4):
    av=average_daily_traffic_percen(G)
    ov=overlimit_percen(G)
    s85=speed85_percen(G)
    s95=speed95_percen(G)

    q_1 = '''

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

                             SELECT ?id ?lat ?long ?avDcars ?pOverL ?sp85 ?sp95 WHERE {
                                ?sensor ns:hasDeviceId ?id.
                                ?sensor ns:hasLocation ?point.
                                ?point geo:lat ?lat.
                                ?point geo:long ?long.
                                ?sensor ns:takes ?measurements. 
                                ?measurements ns:hasTrafficMeasures ?traffic.
                                ?traffic ns:hasDailyCarTraffic ?avDcars.
                                ?measurements ns:hasStatisticsMeasures ?stats.
                                ?stats ns:hasPercentOverLimit ?pOverL.
                                ?stats ns:hasSpeed85Percent ?sp85.
                                OPTIONAL {
                                    ?stats ns:hasSpeed95Percent ?sp95.
                                    }
                                }
                            '''
    q = G.query(q_1)
    lista = [0] * len(q)
    lista_id = [""] * len(q)
    lista_cord = [0] * len(q)
    k=0
    peso = v1 + v2 + v3 + v4
    peso_sins95 = v1 + v2 + v3
    for id, lat, long, avDcars, pOverL, sp85, sp95 in q:
        if sp95 and peso != 0:
            lista[k] = (clasificar_numero(int(avDcars), av) * v1 + clasificar_numero(int(pOverL), ov) * v2 + clasificar_numero(
                int(sp85), s85) * v3 + clasificar_numero(int(sp95), s95) * v4) / peso
        elif not sp95 and peso_sins95 != 0:
            lista[k] = (clasificar_numero(int(avDcars), av) * v1 + clasificar_numero(int(pOverL), ov) * v2 + clasificar_numero(
                int(sp85), s85) * v3) / peso_sins95
        else:
            lista[k] = 0
        lista_id[k] = str(id)
        lista_cord[k] = (float(lat), float(long))
        k+=1
    return lista_id, lista_cord, lista



def clasificar_numero(numero, marcas):
    if numero <= marcas[0]:
        return 1
    elif numero <= marcas[1]:
        return 2
    elif numero <= marcas[2]:
        return 3
    else:
        return 4


def on_submit():
    valor_1 = scale_1.get()
    valor_2 = scale_2.get()
    valor_3 = scale_3.get()
    valor_4 = scale_4.get()

    a, b, c = peligrosidad(G, valor_1, valor_2, valor_3, valor_4)

    m = folium.Map(location=[40.45573295, -79.96777201], zoom_start=15)
    for i in range(len(a)):
        num = c[i]
        if num == 0:
            color = "pink"
        elif num <= 1:
            color = "beige"
        elif num <= 2:
            color = "orange"
        elif num <= 3:
            color = "red"
        else:
            color = "black"
        folium.Marker(location=b[i], popup=a[i], icon=folium.Icon(color=color)).add_to(m)

    m.save('mapa.html')
    webbrowser.open_new_tab('mapa.html')




ventana = tk.Tk()
ventana.title("Ajustar variables según la importancia")

# Controles deslizantes para ajustar valores de 0 a 1
scale_1 = tk.Scale(ventana, label="average_daily_traffic", from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
scale_1.set(1)
scale_1.pack()

scale_2 = tk.Scale(ventana, label="percent_over_limit", from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
scale_2.set(1)
scale_2.pack()

scale_3 = tk.Scale(ventana, label="speed85_percent", from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
scale_3.set(1)
scale_3.pack()

scale_4 = tk.Scale(ventana, label="speed95_percent", from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
scale_4.set(1)
scale_4.pack()

submit_button = tk.Button(ventana, text="Submit", command=on_submit)
submit_button.pack()

ventana.mainloop()