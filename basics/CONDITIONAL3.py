
temperature = input("Enter the current temperature: ")

humidity = 0.2

#idea general: crea un programa que toma decisiones de riego
#dependiendo de los factores de temperatura y humedad.
if temperature > 33:
    if humidity > 0 and humidity < 0.2:
        print("irrigate 1L per square meter")
temperature = 42
if temperature < 25:
    if humidity > 0.2 and humidity < 0.5:
        print("irrigate 0.5L per square meter") 
