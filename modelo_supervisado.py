import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def entrenar_modelo():


    datos = pd.read_csv("datos/dataset_transporte.csv")

    X = datos[
        [
            "hora",
            "dia_semana",
            "pasajeros",
            "distancia_km",
            "numero_paradas"
        ]
    ]

    y = datos["duracion_min"]

    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    modelo = DecisionTreeRegressor(
        max_depth=5,
        random_state=42
    )

    modelo.fit(X_entrenamiento, y_entrenamiento)

    predicciones = modelo.predict(X_prueba)

    mae = mean_absolute_error(y_prueba, predicciones)
    mse = mean_squared_error(y_prueba, predicciones)
    r2 = r2_score(y_prueba, predicciones)

    return modelo, mae, mse, r2


def predecir_duracion(
    modelo,
    hora,
    dia_semana,
    pasajeros,
    distancia_km,
    numero_paradas
):


    nuevo_viaje = pd.DataFrame(
        [
            {
                "hora": hora,
                "dia_semana": dia_semana,
                "pasajeros": pasajeros,
                "distancia_km": distancia_km,
                "numero_paradas": numero_paradas
            }
        ]
    )

    prediccion = modelo.predict(nuevo_viaje)[0]

    return prediccion


def ejecutar_modelo():


    modelo, mae, mse, r2 = entrenar_modelo()

    print("\n==========================================")
    print("       MODELO SUPERVISADO DE TRANSPORTE")
    print("==========================================")

    print("\nModelo entrenado correctamente.")

    print("\nRESULTADOS DEL MODELO")
    print(f"MAE: {mae:.2f} minutos")
    print(f"MSE: {mse:.2f}")
    print(f"R²: {r2:.2f}")

    prediccion = predecir_duracion(
        modelo,
        hora=18,
        dia_semana=4,
        pasajeros=250,
        distancia_km=7.0,
        numero_paradas=6
    )

    print("\nPREDICCIÓN DE EJEMPLO")
    print("Hora: 18:00")
    print("Día: Viernes")
    print("Pasajeros: 250")
    print("Distancia: 7.0 km")
    print("Número de paradas: 6")

    print(f"\nDuración estimada: {prediccion:.1f} minutos")


if __name__ == "__main__":
    ejecutar_modelo()
