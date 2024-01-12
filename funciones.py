import classes
import time
#inicio general de las funciones luego se organizara mejor
def preguntas_de_nivel_personalizado():
    print("Personalizacion de nivel: activada")
    print("")
    classes.escopeta.MaxBalas = int(input("Cuantas balas quieres ingresar? (max8): "))
    if (classes.escopeta.MaxBalas > 8):
        print("Nuestra escopeta solo puede cargar 8 balas !")
        print("Se seteo 8 como las balas maximas en esta partida ")
        classes.escopeta.MaxBalas = 8
    else:
        pass
    classes.escopeta.balas_cargadas = int(input("Cuantas balas verdaderas quieres ingresar?: "))
    if (classes.escopeta.balas_cargadas > 6):
        print("La cantidad maxima de balas cargadas es 6")
        print("Se seteo como 6 la cantidad de balas cargadas")
        classes.escopeta.balas_cargadas = 6
    else:
        pass
    classes.escopeta.balas_vacias = classes.escopeta.MaxBalas - classes.escopeta.balas_cargadas
    print("Se relleno el cargador con " + str(classes.escopeta.balas_vacias) + " balas vacias")

def relleno():
    print("")
    print("-----------------")
    print("")
    print("El juego inicia en 3 segundos!!!")
    print("Inicia en 3")
    time.sleep(1)
    print("Inicia en 2")
    time.sleep(1)
    print("Inicia en 1")
    time.sleep(1)
    print("")
    print("Pues que comience el juego")
    print("")

def crear_orde_de_cartuchos():
    global orden_de_cartuchos
    classes.escopeta.orden_de_cartuchos = [False] * classes.escopeta.MaxBalas


def ronda1():
    a=1
def ronda2():
    a =1
def ronda3():
    a = 1

def eleccion_de_niveles():
    a=1
    if (classes.get.ronda = 1):
        ronda1():
    elif (classes.get.ronda = 2):
        ronda2():
    else:
        ronda3():
