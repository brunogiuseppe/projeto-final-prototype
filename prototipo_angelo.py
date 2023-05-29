class Jogador:
    def __init__(self, nome, idade, posicao, clube, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.clube = clube
        self.nacionalidade = nacionalidade

    def clone(self):
        return Jogador(self.nome, self.idade, self.posicao, self.clube, self.nacionalidade)
        
    def dados_do_atleta(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Posição: {self.posicao}")
        print(f"Clube: {self.clube}")
        print(f"Nacionalidade: {self.nacionalidade}")


jogador_base = Jogador("Gabigol", 26, "Atacante", "Flamengo", "Brasil")

jogador_clone = jogador_base.clone()

jogador_clone.nome = "Arrascaeta"
jogador_clone.idade = 28
jogador_clone.posicao = "Meio-Campista"
jogador_clone.clube = "Flamengo"
jogador_clone.nacionalidade = "Uruguai"


jogador_base.dados_do_atleta()

jogador_clone.dados_do_atleta()
