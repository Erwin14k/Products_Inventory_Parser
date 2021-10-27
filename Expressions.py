from graphviz import Graph

i = 0
dot= Graph('Ast', 'pdf','Arbol de Derivacion')
dot.format = 'pdf'
dot.attr(splines='false')
dot.node_attr.update(shape='circle')
dot.edge_attr.update(color = 'blue')

def start():
	global i
	i += 1
	return i 

def get_node_number():
	global i

class Id_Expression() :
    def __init__(self, id) :
        self.id = id
    def get_value(self, environment):
        return environment.get(self.id)
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node , "Expresion")

        id_id = str(start())
        dot.node(id_id , "Identificador")

        expression_id = str(start())
        dot.node(expression_id , self.id)

        dot.edge(id_id, expression_id)
        dot.edge(id_node, id_id)

        return id_node


class Literal_Expression() :
    def __init__(self, type, value) :
        self.type = type
        self.value = value

    def get_value(self, environment):
        return self.value
    
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node , "Expresion")
        literal_id = str(start())
        dot.node(literal_id , "Literal")
        expression_id = str(start())
        dot.node(expression_id , self.value)
        dot.edge(literal_id, expression_id)
        dot.edge(id_node, literal_id)
        return id_node

class Key_Expression() :
    def __init__(self, type,value) :
        self.type = type
        self.value=value

    def get_value(self, environment):
        return self.value