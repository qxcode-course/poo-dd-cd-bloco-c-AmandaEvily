class Person:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome
    
class Market: 
    def __init__(self, num_caixas: int):
        self.caixas: list[Person | None] = []
        for _ in range (num_caixas):
            self.caixas.append(None)
        self.espera: list[Person] = []

    def __str__(self):
        return f"Caixas:{self.caixas}\nEspera:{self.espera}"
    
person = Person("Maria")
print (person) 
