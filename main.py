from pongapp.pantallas import *


pantalla_menu = Menu()
valor = pantalla_menu.bucle_pantalla()

if valor == "partida":
    pantalla_juego = Partida()
    pantalla_juego.bucle_pantalla()
    resultado_final = pantalla_juego.fin_de_partida()

    if resultado_final != "":
        pantalla_resultado = Resultado(resultado_final=resultado_final)
        pantalla_resultado.bucle_pantalla()
elif valor == "records":
    pantalla_records = Records()
    pantalla_records.bucle_pantalla()