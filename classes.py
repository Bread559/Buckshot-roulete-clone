#importaciones
import random

#inico general de las classes

class color:
    #Definir codigos ANSI para colores
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"


class jugador:
    nombre = ""
    desfibriladores = 0


class escopeta:
    MaxBalas = 0
    balas_vacias = 0
    balas_cargadas = 0

    def __init__(self, balas_vacias, balas_cargadas):
        self.balas_vacias = balas_vacias
        self.balas_cargadas = balas_cargadas
    
    def disparar(self):
        self.disparos +=1
        print("¡Bang!")
    
    def recargar(orden_de_balas, escopeta):
        cont = 0
        cont2 = 0
        while (cont2 < escopeta.MaxBalas):
            if (random.randint(1, (escopeta.balas_vacias + escopeta.balas_cargadas)) <= escopeta.balas_vacias):
                orden_de_balas[cont] = False
                escopeta.balas_vacias -=1
            else:
                orden_de_balas[cont] = True
                escopeta.balas_cargadas -= 1
            cont += 1
            cont2 +=1
        print("Se recargo la escopeta en un orden aleatorio") 
    
"""
sadaasdasdasdad
"""