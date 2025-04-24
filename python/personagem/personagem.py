import random

class PersonagemGame:
    def __init__(self, nome, ranking, vida, força, guilda):
        self.nome = nome
        self.ranking = ranking
        self.vida = vida
        self.força = força
        self.guilda = guilda
        self.inventario = []
        self.defendendo = False

    def atacar(self, outro):
        dano_base = random.randint(int(self.força * 0.8), self.força)
        if outro.defendendo:
            dano = int(dano_base / 2)
            print(f"{outro.nome} defendeu! O dano foi reduzido para {dano}.")
        else:
            dano = dano_base
        print(f"{self.nome} ataca {outro.nome} causando {dano} de dano!")
        outro.vida -= dano
        if outro.vida < 0:
            outro.vida = 0

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} está se defendendo neste turno!")

    def status(self):
        print(f"\n👤 Personagem: {self.nome}")
        print(f"🏆 Ranking: {self.ranking}")
        print(f"🏰 Guilda: {self.guilda}")
        print(f"❤️ Vida: {self.vida}")
        print(f"💪 Força: {self.força}")
        print(f"🎒 Inventário: {self.inventario}")
