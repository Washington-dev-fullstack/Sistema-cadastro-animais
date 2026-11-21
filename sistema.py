from abc import ABC, abstractmethod

# Classe Abstrata
class Animal(ABC):
    def __init__(self, nome, idade, porte):
        self.nome = nome
        self.idade = idade
        self.porte = porte  # "pequeno", "médio" ou "grande"

    # Método concreto: igual para todos os animais
    def ficha(self):
        return f"{self.nome} | {self.idade} anos | Porte: {self.porte}"

    # Método abstrato: cada classe filha terá que fazer o seu
    @abstractmethod
    def descricao_adocao(self):
        pass


# Classes Concretas

class Cachorro(Animal):
    def __init__(self, nome, idade, porte, raca, vacinado):
        super().__init__(nome, idade, porte)
        self.raca = raca
        self.vacinado = vacinado  # True ou False

    # Implementação obrigatória do método abstrato
    def descricao_adocao(self):
        status = "Sim" if self.vacinado else "Não"
        return f"Cachorro da raça {self.raca} | Vacinado: {status}"


class Gato(Animal):
    def __init__(self, nome, idade, porte, castrado, pelo):
        super().__init__(nome, idade, porte)
        self.castrado = castrado  # True ou False
        self.pelo = pelo          # "curto" ou "longo"

    def descricao_adocao(self):
        status = "Sim" if self.castrado else "Não"
        return f"Gato de pelo {self.pelo} | Castrado: {status}"


# funções Auxiliares para o Menu

def cadastrar_cachorro(lista_animais):
    print("\n--- Cadastro de Cachorro ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    porte = input("Porte (pequeno/médio/grande): ")
    raca = input("Raça: ")
    resp = input("Vacinado? (s/n): ")
    
    # Transforma a resposta 's' em True, e qualquer outra coisa em False
    vacinado = True if resp.lower() == 's' else False
    
    # Cria o objeto e adiciona na lista com append()
    novo_caozinho = Cachorro(nome, idade, porte, raca, vacinado)
    lista_animais.append(novo_caozinho)
    print("Cachorro cadastrado com sucesso!")


def cadastrar_gato(lista_animais):
    print("\n--- Cadastro de Gato ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    porte = input("Porte (pequeno/médio/grande): ")
    pelo = input("Tipo de pelo (curto/longo): ")
    resp = input("Castrado? (s/n): ")
    
    castrado = True if resp.lower() == 's' else False
    
    novo_gatinho = Gato(nome, idade, porte, castrado, pelo)
    lista_animais.append(novo_gatinho)
    print("Gato cadastrado com sucesso!")


def listar_animais(lista_animais):
    if len(lista_animais) == 0:
        print("Nenhum animal cadastrado ainda.")
        return

    print("\n=== Animais para Adoção ===")
    # O laço for percorre a lista usando Polimorfismo
    for animal in lista_animais:
        print(animal.ficha())             # Método da classe pai
        print(animal.descricao_adocao())   # O Python escolhe a versão certa aqui!
        print("-" * 40)


# Fluxo Principal do Programa

animais = []  # Lista que vai guardar todos os animais

while True:
    print("\n=== ONG Patinhas Felizes ===")
    print("1 - Cadastrar Cachorro")
    print("2 - Cadastrar Gato")
    print("3 - Ver animais disponíveis")
    print("4 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        cadastrar_cachorro(animais)
    elif opcao == "2":
        cadastrar_gato(animais)
    elif opcao == "3":
        listar_animais(animais)
    elif opcao == "4":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")