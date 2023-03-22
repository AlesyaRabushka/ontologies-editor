from rdf_parser import RDFParser


class Model:
    def __init__(self):
        self.parser = RDFParser()
        self.classes_list = []

    def get_classes(self):
        """
        Used to fill in the list of classes
        :return:
        """
        query_text = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        SELECT ?subject ?object
            WHERE { ?subject rdfs:subClassOf ?object }"""
        request_result = self.parser.execute_request(query_text)

        for row in request_result:
            self.classes_list.append(self.parser.get_clear_value(row.subject))
        return self.classes_list