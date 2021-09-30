class Token:
    def __init__(self, lexem, type,  line, column):
        self.lexem = lexem
        self.type = type
        self.line = line 
        self.column = column 

    def print_token(self):
        print(self.lexem, self.type, self.line, self.column)