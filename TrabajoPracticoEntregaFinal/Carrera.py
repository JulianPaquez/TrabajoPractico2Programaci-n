class Carrera():
    def __init__(self,nombre:str,CantAnio:int,):
        self.__nombre = nombre
        self.__CantAnio = CantAnio
    
    def __str__(self):
        return f"Nombre : {self.__nombre}\t Cantidad de año: {self.__CantAnio}"