class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre: float = calibre
        self.__dureza: str = dureza
        self.__tamanho: int = tamanho

    def grafitePorFolha(self):
        gasto = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}[self.__dureza]
        self.__tamanho -= gasto
        return self.__tamanho
    
    def get_calibre(self) -> float:
        return self.__calibre
    
    def get_dureza(self) -> str:
        return self.__dureza
    
    def get_tamanho(self) -> int:
        return self.__tamanho
    
    def set_tamanho(self, tamanho: int) -> int:
        return self.__tamanho
    
    def __str__(self) -> str:
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"

class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre: float = calibre 
        self.__bico: Grafite | None = None
        self.__tambor: list[Grafite] = []

    def set_tambor(self, tambor: list):
        self.__tambor = tambor

    def get_tambor(self) -> str:
        return self.__tambor
    
    def temGrafite(self) -> bool:
        if self.__bico == None:
            return False
        if 
    
