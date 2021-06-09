def conversor(tipo_pesos, valor_peso):
    dolares = input("Ingrese su cantidad" + tipo_pesos + ": ")
    dolares = float(dolares)
    peso = dolares / valor_peso
    peso = round(peso, 2)
    peso = str(peso)
    print("Tienes $" + peso + " dólares")
  

menu = """
Bienvenido al conversor de monedas 😉💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor(" de pesos colombianos", 3607)
elif opcion == 2:
    conversor(" de pesos argentinos", 94.79)
elif opcion == 3:
    conversor(" de pesos mexicanos", 19.96)
else: 
    print("Ingresa una opción correcta por favor")
