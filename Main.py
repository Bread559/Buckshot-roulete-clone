#importaciones
import classes
import funciones
#----- Inicio del algoritmo -----
classes.jugador.nombre = str(input("Cual es tu nombre? "))
if (classes.jugador.nombre == "jefer"):
    print("Hola jefer bienvenido")
    funciones.preguntas_de_nivel_personalizado()
else:
    pass

funciones.relleno()
funciones.crear_orden_de_cartuchos()
funciones.eleccion_de_niveles()

classes.escopeta.recargar(classes.escopeta.orden_de_cartuchos)
print("orden de los cartuchos en esta ronda: ")
print(str(classes.escopeta.orden_de_cartuchos))
print(funciones.a)