# --- PROGRAMA DE TEMPERATURA Y LLUVIA ---

temperatura = int(input("¿Qué temperatura hace hoy? (en grados): "))
llueve = input("¿Está lloviendo ahora mismo? (responde si o no): ")

# 1. Primero miramos si hace frío
if temperatura < 15:
    print("¡Hace frío!")
    if llueve == "si":
        print("Lleva abrigo y además coge un paraguas porque te vas a mojar.")
    if llueve == "no":
        print("Lleva abrigo, pero al menos el cielo está despejado.")

# 2. Ahora miramos si hace calor
if temperatura >= 19:
    print("¡Hace buena temperatura o calor!")
    if llueve == "si":
        print("Qué raro, hace calor pero está lloviendo. Coge un paraguas fino.")
    if llueve == "no":
        print("El día está perfecto. ¡Disfruta del buen tiempo!")
