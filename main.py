class persona:
    #constructor
    def __init__(self, nombre: str):
        self.nombre: str = ""
    #metodo
    def presentante(self) -> None:
        print(f"Hola, soy {self.nombre}")

#instanciar
Pedro = Persona()
Pedro.nombre = "Pedro Rojas"
Pedro.presentate()