# Exercício 1: Gerenciamento de Tarefas
# Crie uma classe chamada Tarefa que represente uma única tarefa.

# Atributos :

# descricao(string): a descrição da tarefa.

# concluida(booleano): indica se a tarefa foi concluída ou não. O valor inicial deve ser False.

# Métodos :

# marcar_como_concluida(): um método que muda o estado da tarefa para concluida = True.

# __str__(): um método especial que retorna uma string formatada para exibir uma tarefa. Por exemplo, se uma tarefa não estiver concluída, retorne "[ ] Fazer compras". Se quiser, retorne "[X] Fazer compras".

# Dica profissional: O método __str__()é essencial para facilitar a depuração e a leitura de objetos. Usar f-strings aqui é a forma mais moderna e "Pythônica" de formatar a saída.


class Tarefa():

    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_como_concluida(self):
        if self.concluida:
            print(f'\033[1;31mA tarefa \033[m"{self.descricao}"\033[m\033[1;31m já está concluída!\033[m')
        
        else:
            print(f'\033[1;32m{self.descricao} foi concluída!\033[m')
            self.concluida = True


    def __str__(self):

        status = 'X' if self.concluida else ''
        return f'[{status}] {self.descricao}'


tarefa_1 = Tarefa('café')
print(f'Tarefa criada: {tarefa_1}')
tarefa_1.marcar_como_concluida()
print(f'Tarefa atualizada: {tarefa_1}')
tarefa_1.marcar_como_concluida()
