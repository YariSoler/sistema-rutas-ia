from conocimiento import obtener_estaciones
from reglas import validar_ruta
from busqueda import encontrar_ruta
from modelo_supervisado import entrenar_modelo, predecir_duracion


def mostrar_estaciones(estaciones):
    print("\nEstaciones disponibles:")

    for numero, estacion in enumerate(estaciones, start=1):
        print(f"{numero}. {estacion}")


def mostrar_ruta(ruta):
    print("\nRUTA ENCONTRADA\n")

    for i, estacion in enumerate(ruta):

        if i < len(ruta) - 1:
            print(f"{estacion} ↓")
        else:
            print(estacion)

    print("\nNúmero de desplazamientos:", len(ruta) - 1)


def buscar_ruta():
  

    estaciones = obtener_estaciones()

    mostrar_estaciones(estaciones)

    print("\n------------------------------------------")

    origen_numero = input(
        "\nIngrese el número de la estación de origen: "
    ).strip()

    destino_numero = input(
        "Ingrese el número de la estación de destino: "
    ).strip()

    try:
        origen_numero = int(origen_numero)
        destino_numero = int(destino_numero)

    except ValueError:
        print(
            "\nDebe ingresar números de estación válidos."
        )
        return

    if origen_numero < 1 or origen_numero > len(estaciones):
        print("\nEl número de origen no es válido.")
        return

    if destino_numero < 1 or destino_numero > len(estaciones):
        print("\nEl número de destino no es válido.")
        return

    origen = estaciones[origen_numero - 1]
    destino = estaciones[destino_numero - 1]

    print("\n------------------------------------------")

    print(f"\nOrigen seleccionado: {origen}")
    print(f"Destino seleccionado: {destino}")

    print("\n------------------------------------------")

    if not validar_ruta(origen, destino, estaciones):

        print("\nNo se puede realizar la búsqueda.")

        return

    ruta = encontrar_ruta(
        origen,
        destino,
        mostrar_proceso=True
    )

    if ruta:
        mostrar_ruta(ruta)

    else:
        print(
            "\nNo fue posible encontrar una ruta "
            "entre las estaciones seleccionadas."
        )


def realizar_prediccion():
  
    print("\n==========================================")
    print("       PREDICCIÓN DE DURACIÓN")
    print("==========================================")

    try:

        # ------------------------------------------
        # Validar hora
        # ------------------------------------------

        hora = int(
            input("\nIngrese la hora del viaje (0-23): ")
        )

        if hora < 0 or hora > 23:
            print("\nLa hora debe estar entre 0 y 23.")
            return

        # ------------------------------------------
        # Validar día de la semana
        # ------------------------------------------

        dia_semana = int(
            input(
                "Ingrese el día de la semana "
                "(0=Lunes, 1=Martes, ..., 6=Domingo): "
            )
        )

        if dia_semana < 0 or dia_semana > 6:
            print("\nEl día debe estar entre 0 y 6.")
            return

        # ------------------------------------------
        # Validar pasajeros
        # ------------------------------------------

        pasajeros = int(
            input("Ingrese la cantidad de pasajeros: ")
        )

        if pasajeros <= 0:
            print(
                "\nLa cantidad de pasajeros "
                "debe ser mayor que 0."
            )
            return

       
        distancia_km = float(
            input("Ingrese la distancia del recorrido (km): ")
        )

        if distancia_km <= 0:
            print(
                "\nLa distancia debe ser mayor que 0."
            )
            return

    

        numero_paradas = int(
            input("Ingrese el número de paradas: ")
        )

        if numero_paradas <= 0:
            print(
                "\nEl número de paradas "
                "debe ser mayor que 0."
            )
            return

 
        print("\nEntrenando modelo...")

        modelo, mae, mse, r2 = entrenar_modelo()


        prediccion = predecir_duracion(
            modelo,
            hora,
            dia_semana,
            pasajeros,
            distancia_km,
            numero_paradas
        )

        print("\n------------------------------------------")
        print("RESULTADO DE LA PREDICCIÓN")
        print("------------------------------------------")

        print(
            f"Duración estimada: "
            f"{prediccion:.1f} minutos"
        )

        print("\nMétricas del modelo:")
        print(f"MAE: {mae:.2f} minutos")
        print(f"MSE: {mse:.2f}")
        print(f"R²: {r2:.2f}")

    except ValueError:
        print(
            "\nError: ingrese un valor numérico válido."
        )


def main():

    while True:

        print("\n==========================================")
        print("       SISTEMA INTELIGENTE DE RUTAS")
        print("==========================================")

        print("\n1. Buscar mejor ruta")
        print("2. Predecir duración del viaje")
        print("3. Salir")

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion == "1":

            buscar_ruta()

        elif opcion == "2":

            realizar_prediccion()

        elif opcion == "3":

            print(
                "\nGracias por utilizar "
                "el sistema inteligente de rutas."
            )

            break

        else:

            print(
                "\nOpción no válida. "
                "Seleccione 1, 2 o 3."
            )


if __name__ == "__main__":
    main()
