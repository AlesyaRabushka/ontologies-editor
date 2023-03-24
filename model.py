from rdf_parser import RDFParser


class Model:
    def __init__(self, filename):
        self.parser = RDFParser(filename)
        self.subclasses_list = []
        self.class_subclass_list = []
        self.class_item_list = []


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
            if self.parser.get_clear_value(row.subject) not in self.subclasses_list:
                self.subclasses_list.append(self.parser.get_clear_value(row.subject))
            d = {}
            d[self.parser.get_clear_value(row.object)] = self.parser.get_clear_value(row.subject)
            if d not in self.class_subclass_list:
                self.class_subclass_list.append(d)
        return self.subclasses_list


    def get_main_table_info(self):
        """
        Used to get info for the main table
        :return:
        """
        value = ''
        query_text = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX my: <http://www.semanticweb.org/rabus/ontologies/2023/1/dance_directions#>
        
        
        SELECT  ?book
        WHERE {?book rdf:type my:%s}"""%value


        for item in self.subclasses_list:
            request_result = self.parser.execute_request( """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX my: <http://www.semanticweb.org/rabus/ontologies/2023/1/dance_directions#>
            
            
            SELECT  ?book
            WHERE {?book rdf:type my:%s}"""%item)
            # print(request_result)
            for row in request_result:
                for pare in self.class_subclass_list:
                    for class_, subclass in pare.items():
                        if subclass == item:
                            d = {}
                            d['class'] = class_
                            d['subclass'] = item
                            d['object'] = self.parser.get_clear_value(row[0])
                            if d not in self.class_item_list:
                                self.class_item_list.append(d)

        return self.class_item_list



    def update(self, filename):
        """
        Used to update current states of all the fields
        :return:
        """
        self.parser = RDFParser(filename)
        self.get_classes()
        self.get_main_table_info()

    def add_object(self, object_name, class_name):
        """
        Used to add new item into ontology
        :return:
        """
        self.parser.add_object(object_name, class_name)