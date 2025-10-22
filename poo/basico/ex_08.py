# Exercício 8: Classe ListaDeTarefas(Lista como Atributo)
# Chore uma aula ListaDeTarefas:

# Atributo de Instância: tarefas (uma lista vazia, inicializada no __init__).

# Método adicionar_tarefa(tarefa) : Adiciona uma nova string à lista tarefas.

# Métodolistar_tarefas() : Imprima cada tarefa da lista em uma linha separada.

# Dica Pythônica: Inicialize uma lista dentro do __init__para garantir que cada instância tenha sua própria lista de tarefas,
# evitando problemas comuns de POO em Python.

class Lista_De_Tarefas:
    def __init__(self, tarefas=[]):
        self.tarefas = tarefas


    def adicionar_tarefas(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'\033[1;32m"{tarefa}" adicionada com sucesso!\033[m')


    def listar_tarefas(self):
        if len(self.tarefas) == 0:
            print('\033[1;31mNão há nada para listar\033[m')

        else:
            print('Listando as tarefas:')
            for i in range(len(self.tarefas)):
                print(self.tarefas[i])
        


tarefas_hoje = Lista_De_Tarefas()
tarefas_hoje.listar_tarefas()
tarefas_hoje.adicionar_tarefas('Fazer café')
tarefas_hoje.listar_tarefas()
tarefas_hoje.adicionar_tarefas('Fazer almoço')
tarefas_hoje.listar_tarefas()
