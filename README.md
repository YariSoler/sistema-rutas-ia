# Sistema Inteligente de Rutas

## Actividad 3 – Aprendizaje Supervisado
PDF:
[pruebas_componente.pdf](https://github.com/user-attachments/files/33183622/pruebas_componente.pdf)
[descripcion_datos.pdf](https://github.com/user-attachments/files/33183627/descripcion_datos.pdf)



Proyecto académico desarrollado como continuación del sistema inteligente de rutas para transporte masivo. El proyecto conserva la búsqueda de rutas mediante el algoritmo A* e incorpora un componente de aprendizaje supervisado para estimar la duración de un viaje.

> **Nota sobre los datos:** el proyecto no dispone de una fuente histórica real de duración de viajes integrada al grafo simplificado utilizado en las actividades anteriores. Por esta razón, se desarrolló un dataset sintético con fines académicos. Los datos no representan registros oficiales de TransMilenio.

---

## 1. Objetivo

Incorporar un modelo de aprendizaje supervisado al sistema inteligente de rutas para estimar la duración de un viaje a partir de características como la hora, el día de la semana, la cantidad de pasajeros, la distancia y el número de paradas.

---

## 2. Funcionalidades

El sistema permite:

1. Consultar las estaciones disponibles.
2. Seleccionar una estación de origen y una estación de destino mediante su número.
3. Encontrar una ruta utilizando el algoritmo A*.
4. Mostrar el proceso de búsqueda de A* mediante los valores `g(n)`, `h(n)` y `f(n)`.
5. Entrenar un modelo supervisado basado en un árbol de decisión.
6. Predecir la duración estimada de un nuevo viaje.
7. Mostrar métricas de evaluación del modelo.
8. Validar los datos ingresados por el usuario.

---

## 3. Tecnologías utilizadas

- Python 3
- pandas
- scikit-learn
- CSV
- Git / GitHub
- Visual Studio Code

---

## 4. Estructura del proyecto

```text
sistema_rutas_ia/
│
├── .gitignore
├── main.py
├── conocimiento.py
├── reglas.py
├── busqueda.py
├── modelo_supervisado.py
│
├── datos/
│   ├── generar_dataset.py
│   └── dataset_transporte.csv
│
├── descripcion_datos.pdf
├── pruebas_componente.pdf
└── README.md
```

---

## 5. Descripción de los principales archivos

### `main.py`

Es el punto de entrada del sistema. Presenta el menú principal y permite seleccionar entre:

- Buscar mejor ruta.
- Predecir duración del viaje.
- Salir.

También integra el algoritmo A* y el modelo de aprendizaje supervisado.

### `conocimiento.py`

Contiene la base de conocimiento del sistema, incluyendo las estaciones, conexiones y posiciones utilizadas para la búsqueda de rutas.

### `reglas.py`

Contiene las reglas utilizadas para validar estaciones y rutas.

### `busqueda.py`

Implementa la búsqueda de rutas mediante el algoritmo A*.

### `modelo_supervisado.py`

Contiene el componente de aprendizaje supervisado. Utiliza `DecisionTreeRegressor` de scikit-learn para estimar la duración de un viaje.

### `datos/generar_dataset.py`

Genera el dataset sintético utilizado para entrenar y evaluar el modelo.

### `datos/dataset_transporte.csv`

Contiene 150 registros sintéticos utilizados por el modelo.

### `descripcion_datos.pdf`

Documento que describe la fuente, naturaleza, estructura y utilización de los datos.

### `pruebas_componente.pdf`

Documento que presenta las pruebas realizadas al componente desarrollado y sus resultados.

---

## 6. Dataset

El archivo `dataset_transporte.csv` contiene 150 registros.

Las variables utilizadas son:

| Variable | Descripción |
|---|---|
| `hora` | Hora del viaje, de 0 a 23 |
| `dia_semana` | Día de la semana, de 0 a 6 |
| `pasajeros` | Cantidad de pasajeros |
| `distancia_km` | Distancia del recorrido en kilómetros |
| `numero_paradas` | Número de paradas |
| `duracion_min` | Duración estimada del viaje en minutos |

Las cinco primeras variables se utilizan como entradas del modelo y `duracion_min` corresponde a la variable objetivo.

---

## 7. Modelo de aprendizaje supervisado

Se utiliza un árbol de decisión para regresión mediante:

```python
DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)
```

El conjunto de datos se divide en:

- 80 % para entrenamiento.
- 20 % para prueba.

El modelo se evalúa mediante:

- MAE (Error Absoluto Medio).
- MSE (Error Cuadrático Medio).
- R² (coeficiente de determinación).

---

## 8. Resultados obtenidos

En las pruebas realizadas se obtuvieron las siguientes métricas:

```text
MAE: 4.93 minutos
MSE: 35.71
R²: 0.42
```

Para un escenario de ejemplo con:

```text
Hora: 18:00
Día: Viernes
Pasajeros: 250
Distancia: 7.0 km
Paradas: 6
```

el modelo obtuvo:

```text
Duración estimada: 47.7 minutos
```

En un segundo escenario:

```text
Hora: 18:00
Día: Sábado
Pasajeros: 2
Distancia: 10 km
Paradas: 6
```

se obtuvo:

```text
Duración estimada: 57.8 minutos
```

---

## 9. Pruebas realizadas

### Prueba 1 – Búsqueda A*

Entrada:

```text
Origen: 2 – Banderas
Destino: 3 – Mundo Aventura
```

Resultado:

```text
Banderas → Mundo Aventura
Número de desplazamientos: 1
```

### Prueba 2 – Predicción

Resultado:

```text
Duración estimada: 47.7 minutos
```

### Prueba 3 – Segundo escenario

Resultado:

```text
Duración estimada: 57.8 minutos
```

### Prueba 4 – Validación

Se ingresó una hora inválida:

```text
25
```

El sistema respondió:

```text
La hora debe estar entre 0 y 23.
```

La prueba fue exitosa.

Para mayor detalle, consultar `pruebas_componente.pdf`.

---

## 10. Instalación

Se recomienda utilizar Python 3.11 o una versión compatible con las librerías utilizadas.

Instalar las dependencias con:

```bash
python -m pip install pandas scikit-learn
```

---

## 11. Ejecución

Desde la carpeta principal del proyecto:

```bash
python main.py
```

El sistema mostrará:

```text
1. Buscar mejor ruta
2. Predecir duración del viaje
3. Salir
```

Para generar nuevamente el dataset:

```bash
python datos/generar_dataset.py
```

---

## 12. Evidencias y documentación

Los resultados de las pruebas y la descripción del dataset se encuentran en:

- `descripcion_datos.pdf`
- `pruebas_componente.pdf`


---

## 13. Autores

Yaridiveth Soler Manjarres - Naomy Restrepo



 
