#criando classe

class Text:
    def __init__(self, nome, idade, profissão):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão
        
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}" + " tenho " +  str(self.idade) + " e trabalho com " + self.profissão)
        

Text1 = Text("Campos", 35, "T.i")

Text1.apresentar()


print(getattr(Text1,"idade"))

setattr(Text1, "idade", 36)

print(getattr(Text1,"idade"))