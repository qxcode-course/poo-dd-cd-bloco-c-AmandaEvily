class Person:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self) -> str:
        return self.nome

    def __str__(self):
        return self.nome
    
class Market: 
    def __init__(self, num_caixas: int):
        self.caixas: list[Person | None] = []
        for _ in range (num_caixas):
            self.caixas.append(None)
        self.espera: list[Person] = []

    def enter(self, person: Person): 
        self.espera.append(person)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("indice inexistente")
            return 
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
        if len(self.espera) == 0:
            print("ninguem esperando")
            return
        self.caixas[index] = self.espera[0]
        del self.espera[0] 

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("indice inexistente")
            return 
        if self.caixas[index] is None:
            print("caixa vazio")
            return
        self.caixas [index] = None

    def give_up(self, nome: str) -> Person | None:
        for i, person in enumerate(self.espera):
            if person.nome == nome:
                aux = self.espera[i]
                del self.espera[i]
                return aux
            return None

    def __str__(self):
        self.caixas = [Person(" [-----, -----]")]
        ", ".join([str(x)for x in self.caixas])
        caixas = ", ".join([str(x) for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas:{caixas}\nEspera:{espera} "
    
def main():
    market = Market(0)

    while True:
        line = input()
        print("$"+ line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        if args[0] == "init":
            market = Market(int(args[1]))
        if args[0] == "show":
            print (market)
        if args[0] == "enter":
            market.enter(Person(args[1]))
        if args[0] == "call":
            fila = int(int(args[1]))
            market.call(fila)
        if args[0] == "finish":
            pessoa = int(args[1])
            market.finish(pessoa)

main ()
            