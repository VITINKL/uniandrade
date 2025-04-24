from personagem import PersonagemGame
from batalha import batalha_interativa

# Criando personagens
samurai = PersonagemGame("Hiroshi", "Surreal", 110, 23, "Samurais Extintos")
spartano = PersonagemGame("Kratos", "Diamante", 120, 21, "Destruidores")

# Adicionando itens
samurai.inventario.extend(["Katana Lendária", "Furos de estiragem"])
spartano.inventario.extend(["Lâminas do Caos", "Os Olhos da Verdade"])

# Status inicial
print("🏁 Status Inicial dos Combatentes 🏁")
samurai.status()
spartano.status()

# Iniciar batalha
batalha_interativa(samurai, spartano)
