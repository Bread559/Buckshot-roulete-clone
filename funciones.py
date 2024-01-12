import classes
import time
import random

# Inicio general de las funciones; luego se organizará mejor

def preguntas_de_nivel_personalizado():
    print("Personalización de nivel: activada")
    print("")
    classes.escopeta.MaxBalas = int(input("¿Cuántas balas quieres ingresar? (máx. 8): "))
    if classes.escopeta.MaxBalas > 8:
        print("Nuestra escopeta solo puede cargar 8 balas!")
        print("Se estableció 8 como las balas máximas en esta partida.")
        classes.escopeta.MaxBalas = 8
    else:
        pass
    classes.escopeta.balas_cargadas = int(input("¿Cuántas balas verdaderas quieres ingresar?: "))
    if classes.escopeta.balas_cargadas > 6:
        print("La cantidad máxima de balas cargadas es 6")
        print("Se estableció 6 como la cantidad de balas cargadas.")
        classes.escopeta.balas_cargadas = 6
    else:
        pass
    classes.escopeta.balas_vacias = classes.escopeta.MaxBalas - classes.escopeta.balas_cargadas
    print(f"Se rellenó el cargador con {classes.escopeta.balas_vacias} balas vacías")

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
    print("¡Pues que comience el juego!")
    print("")

def crear_orden_de_cartuchos():
    global orden_de_cartuchos
    classes.escopeta.orden_de_cartuchos = [False] * classes.escopeta.MaxBalas

def ronda1():
    global orden_de_cartuchos
    global items
    #global classes.escopeta.MaxBalas
    classes.escopeta.MaxBalas = 3
    print(classes.escopeta.MaxBalas)
    items = None
    crear_orden_de_cartuchos()
    classes.escopeta.balas_cargadas =  random.randint(1,2)
    classes.escopeta.balas_vacias = classes.escopeta.balas_cargadas -classes.escopeta.MaxBalas
    classes.escopeta.recargar(self, classes.escopeta.orden_de_cartuchos)

    

def ronda2():
    classes.escopeta.MaxBalas = 3
    items = 2

def ronda3():
    classes.escopeta.MaxBalas = 3
    items = 4

def eleccion_de_niveles():
    if classes.get.ronda == 1:
        ronda1()
    elif classes.get.ronda == 2:
        ronda2()
    else:
        ronda3()