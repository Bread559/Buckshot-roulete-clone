#importaciones
import random

#inico general de las classes
class get():
    ronda= 1


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
    esposas= 0
    lupa = 0
    cigarrillo = 0
    cerveza = 0
    cuhillo = 0

class JugadorIA:
    nombre = "Chirrete"
    desfibriladores = 0
    esposas= 0
    lupa = 0
    cigarrillo = 0
    cerveza = 0
    cuhillo = 0


class escopeta:
    MaxBalas = 0
    balas_vacias = 0
    balas_cargadas = 0
    orden_de_cartuchos = [False]

    def __init__(self, balas_vacias, balas_cargadas):
        self.balas_vacias = balas_vacias
        self.balas_cargadas = balas_cargadas
    
    def disparar(self):
        self.disparos +=1
        print("¡Bang!")
    
    def recargar(orden_de_cartuchos):
        cont = 0
        cont2 = 0
        while (cont2 < escopeta.MaxBalas):
            if (random.randint(1, (escopeta.balas_vacias + escopeta.balas_cargadas)) <= escopeta.balas_vacias):
                orden_de_cartuchos[cont] = False
                escopeta.balas_vacias -=1
            else:
                orden_de_cartuchos[cont] = True
                escopeta.balas_cargadas -= 1
            cont += 1
            cont2 +=1
        print("Se recargo la escopeta en un orden aleatorio") 
    
