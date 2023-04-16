from rdflib import Graph, Literal, RDF, URIRef, Namespace
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
            print('in file')
            try:
                print(filename)
                self.graph.parse(filename) # given ontology
                # for s,p,o in self.graph.triples((None, None, None)):
                #     print(s,p,o)
                self.namespace = Namespace('http://www.semanticweb.org/rabus/ontologies/2023/1/dance_directions#')
            except:
                print('HERE IS ERROR')



    def get_clear_value(self, prefixed_value):
        """
        Is used to remove the ontology's PREFIX out of output value
        :param prefixed_value:
        :return:
        """
        # print('get clear')
        output = ''
        print(prefixed_value)
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
        # print('request is done')
        return self.graph.query(query_text)


    def add_object(self, object_name, class_name, new_class_name):
        """
        Used to add item into ontology
        """
        print('class - ', class_name, 'new class', new_class_name)
        object = URIRef('http://www.semanticweb.org/rabus/ontologies/2023/1/dance_directions#' + str(object_name))
        # s = Namespace(self.namespace + f'{class_name}')

        self.graph.bind('my', self.namespace)
        # print(s)
        self.graph.add((object, RDF.type, self.namespace[f'{class_name}']))


        print('done')
        # self.graph.serialize(format="xml")
        self.graph.serialize(destination="D:\Kyrs3\PBZ_6sem\ontologies-editor\Documents\\f.rdf")
        # v = self.graph.serialize(format='trix')
        # print(v)
        # f = open('D:\\Kyrs3\\PBZ_6sem\\ontologies-editor\\Documents\\file.owl', 'w')
        # f.writelines(v)
        # f.close()




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