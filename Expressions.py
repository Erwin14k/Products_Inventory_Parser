class Id_Expression() :
    def __init__(self, id) :
        self.id = id
    def get_value(self, environment):
        return environment.get(self.id)


class Literal_Expression() :
    def __init__(self, type, value) :
        self.type = type
        self.value = value

    def get_value(self, environment):
        return self.value