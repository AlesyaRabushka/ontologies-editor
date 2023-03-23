from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD
from rdflib.plugins.sparql import prepareQuery


# g = Graph()
# g.parse('Documents/dance_directions.owl')
#
# # for s,p,o in g:
# #     print(s,p,o)
#
q = ("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT ?subject ?object
	WHERE { ?subject rdfs:subClassOf ?object }""")




class RDFParser:
    def __init__(self, filename):
        self.graph = Graph()
        if filename:
            self.graph.parse(filename) # given ontology


    def get_clear_value(self, prefixed_value):
        """
        Is used to remove the ontology's PREFIX out of output value
        :param prefixed_value:
        :return:
        """
        output = ''
        for c in prefixed_value[::-1]:
            if c != '#':
                output += c
            else:
                break
        return output[::-1]


    def execute_request(self, query_text):
        """
        Used to execute a given query
        :param query_text:
        :return:
        """
        return self.graph.query(query_text)



# p = RDFParser()
# qres = p.set_query(q)
# l = []
# l2 = []
# for row in qres:
#     print(f"{p.get_clear_value(row.subject)} - {p.get_clear_value(row.object)}")
#     l.append(p.get_clear_value(row.subject))
#     l2.append(p.get_clear_value(row.object))
#
# print(l)
# print(l2)