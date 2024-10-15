class Interruptor:
    def __init__(self, id):
        self.id = id
        self.estado = False  # False = desligado, True = ligado

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False


def descobrir_interruptores():
    # Criando os interruptores
    interruptores = [Interruptor(1), Interruptor(2), Interruptor(3)]

    # Ligando o Interruptor 1 por 10 minutos (simulado aqui)
    interruptores[0].ligar()
    print("Interruptor 1 ligado.")

    # Simulando a espera (não necessário no código, mas conceitualmente)
    # Esperamos 10 minutos e depois desligamos o Interruptor 1
    interruptores[0].desligar()
    print("Interruptor 1 desligado.")

    # Ligando o Interruptor 2
    interruptores[1].ligar()
    print("Interruptor 2 ligado.")

    # O resultado será verificado manualmente na sala
    # Resultados simulados
    return (
        "Interruptor 1 controla a lâmpada que está apagada e quente.",
        "Interruptor 2 controla a lâmpada que está acesa.",
        "Interruptor 3 controla a lâmpada que está apagada e fria."
    )


# Executando a função e imprimindo os resultados
resultados = descobrir_interruptores()
for resultado in resultados:
    print(resultado)