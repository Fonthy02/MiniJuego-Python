import random

inicio = print("¡Oh no, te han encerrado en una mazmorra y tienes que encontrar la manera para escapar!\n"
      "Lo primero que ves en tu celda es la puerta principal [PP] y arriba un conducto de ventilacion [CV] por los cuales puedes escapar\n")

puerta_conducto = input("¿Que quieres coger....?\n"
                        "[PP] Puerta principal\n"
                        "[CV] Conducto de ventilacion\n"
                        "Opcion que desesa escoger: ")
if puerta_conducto == "PP":
    print("Elegiste la puerta principal, pero resulta que fue una mala eleccion ya que el guardia te descubrio y te mato")
elif puerta_conducto == "CV":
    print("Buena eleccion el conducto de ventilacion te ayudara a poder salir de la mazmorra, pero resulta que das a una sala en la que hay varios guardias y para salir necesitas una llave de acceso\n"
          "\n")

    sala_seguridad = input("Ahora tienes una serie de opciones en esa sala: \n"
          "[MS] Ir de manera sigilosa hasta el puto donde se encuentra la tarjeta y abrir la puerta pudiendo escapar\n"
          "[IC] Ir corriendo hasta la tarjeta y abrir rapido la puerta\n"
          "[AS] Ir de forma sigilosa hasta la posiciones de los guardias e intentar asesinarlos para coger la tarjeta y escapar\n"
          "[CA] Ir corriendo guardia por guardia y asesinarlos a todos para luego coger la tarjeta y escapar\n"
          "Opcion que desesa escoger: ")
    if sala_seguridad == "MS":
        print("Has escogido la opcion correcta, que te permitira escapar de la prision y ser totalmente libre")
    elif sala_seguridad == "IC":
        print("Mal mal muy mal te capturan todos los guardias y te matan, ya que levantaste sospechas yendo corriendo")
    elif sala_seguridad == "AS":
        print("Buena eleccion, solamente que consigues matar a todos los guardias menos al último... solamente te dejara escapar si consigues resolver una operacion aritmetica\n"
              "\n")
        print("[Guardia]: Niñat@ sin verguenza.... ¡para poder escapar de esta mazmorra debrás resolver esta operacion!")
        pregunta_aritmetica = random.randint(0,100)

        formula_aritmetica = 2 * pregunta_aritmetica
        preguntita_arit = int(input("Cuanto es: {}".format(formula_aritmetica)))
        print(preguntita_arit)

    elif sala_seguridad == "CA":
        print("Has sido descubierto y te han asesinado de la peor forma posible..... ¡Que mal!")
    else:
        print("Solamente puedes escoger: \n"
          "[MS] Ir de manera sigilosa hasta el puto donde se encuentra la tarjeta y abrir la puerta pudiendo escapar\n"
          "[IC] Ir corriendo hasta la tarjeta y abrir rapido la puerta\n"
          "[AS] Ir de forma sigilosa hasta la posiciones de los guardias e intentar asesinarlos para coger la tarjeta y escapar\n"
          "[CA] Ir corriendo guardia por guardia y asesinarlos a todos para luego coger la tarjeta y escapar\n")
else:
    print("Solamente puedes escoger: \n"
          "[PP] Puerta principal\n"
          "[CV] Conducto de ventilacion")