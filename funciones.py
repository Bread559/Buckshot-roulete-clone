import classes
import time
#inicio general de las funciones luego se organizara mejor
def preguntas_de_nivel_personalizado():
    classes.jugador.nombre = str(input("Cual es tu nombre? "))
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