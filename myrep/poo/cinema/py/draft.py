class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.id}:{self.phone}"
    
class Theater:
    def __init__(self, size: int):
        self.seats: list[Client | None] = [None] * size
        
    