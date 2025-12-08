class Biblioteca():
    def __init__(self):
        self.lista = []
    
    def adicionar_item(self, *args):
        for item in args:
            self.lista.append(item)
    
biblioteca = Biblioteca()

biblioteca.adicionar_item('oi', 123)
print(biblioteca.lista)
    