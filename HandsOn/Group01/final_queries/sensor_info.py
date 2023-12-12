from rdflib import term
from rdflib import Literal


def radar_analisis1(g, devId):
    q2 = '''
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
     SELECT ?sensor ?lat ?lon ?district ?overlimStat ?limSpe ?medSpe ?maxSpe ?per85Stat ?per95Stat ?daySta ?monSta ?yeaSta ?dayEnd ?monEnd ?yeaEnd ?average_daily_car_traffic
    WHERE {
            ?sensor ns:hasDeviceId ''' + "'" + str(devId) + "'" + '''   .
            ?sensor ns:locatedIn ?district.
            ?sensor ns:hasLocation ?r.
            ?r geo:lat ?lat.
            ?r geo:long ?lon.
            ?sensor ns:takes ?x.
            ?x ns:hasDuration ?y.
            ?y w3:hasBeginning ?dateTime .
            ?dateTime w3:day ?daySta .
            ?dateTime w3:month ?monSta .
            ?dateTime w3:year ?yeaSta .
            ?y w3:hasEnd ?date .
            ?date w3:day ?dayEnd .
            ?date w3:month ?monEnd .
            ?date w3:year ?yeaEnd .
            ?x ns:hasSpeedMeasures ?z.
            ?z ns:hasMedianSpeed ?medSpe.
            ?z ns:hasSpeedlimit ?limSpe.
            OPTIONAL{ ?z ns:hasMaxSpeed ?maxSpe }.
            ?x ns:hasStatisticsMeasures ?d.
            ?d ns:hasSpeed85Percent ?per85Stat.
            ?d ns:hasSpeed95Percent ?per95Stat.
            ?d ns:hasPercentOverLimit ?overlimStat.
            ?x ns:hasTrafficMeasures ?h.
            ?h ns:hasDailyCarTraffic ?average_daily_car_traffic.
    }
      '''
    for row in g.query(q2):
        district = row.district
        daySta = row.daySta
        monSta = row.monSta
        yeaSta = row.yeaSta
        dayEnd = row.dayEnd
        monEnd = row.monEnd
        yeaEnd = row.yeaEnd
        limSpe = row.limSpe
        medSpe = row.medSpe
        maxSpe = row.maxSpe if row.maxSpe else str('NO INFO.')
        overlimStat = row.overlimStat
        lat = row.lat
        lon = row.lon
        per85Stat = row.per85Stat
        per95Stat = row.per95Stat
        countCar = row.average_daily_car_traffic


        print(f'''
            Sensor with id: {devId}
            Located in Pittsburgh's District: {district}
            Worked from {daySta}\{monSta}\{yeaSta} to {dayEnd}\{monEnd}\{yeaEnd}
            Cars counted: {countCar}
            Speed limit at the location: {limSpe} mph
            Median of speeds recorded: {medSpe} mph
            Maximum speed recorded: {maxSpe} mph
            Percentage of vehicles that were speeding: {overlimStat} %

            Other useful properties:
            Coordinates: {lat}, {lon}
            The 85th percentile of the speed distribution: {per85Stat} mph
            The 95th percentile of the speed distribution: {per95Stat} mph
            ''')