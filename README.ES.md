# ft_linear_regression - Proyecto de 42 School

Implementación de un algoritmo de regresión lineal simple desde cero usando gradiente descendente para predecir precios de coches según su kilometraje.

## Descripción General

Este proyecto predice precios de coches usando la hipótesis lineal:

```
precio = theta0 + theta1 * kilometraje
```

El modelo se entrena usando gradiente descendente con normalización min-max para una mejor convergencia. Los parámetros se guardan en `trained_data.json` para predicciones posteriores.

## Características

### Entrenamiento
- Optimización por gradiente descendente
- Normalización min-max para mejor convergencia
- Tasa de aprendizaje e iteraciones configurables
- Guarda los parámetros entrenados en JSON
- Maneja casos edge (datos vacíos, punto único, valores idénticos)

### Predicción y Evaluación
- Estimación de precio en tiempo real desde la entrada de kilometraje
- Gráfica visual con línea de regresión y puntos de datos
- Métricas de precisión del modelo (MSE, RMSE, MAE, R²)
- Validación de entrada para valores negativos/inválidos

## Estructura del Proyecto

```
linearRegression/
├── data.csv              # Dataset con 24 coches (kilometraje y precio)
├── training.py           # Entrena el modelo y guarda los parámetros
├── predict.py            # Predice precio, muestra métricas y visualiza resultados
├── utils.py              # Utilidades compartidas para carga de datos
├── trained_data.json     # Parámetros entrenados (generado)
└── .gitignore
```

## Dependencias

- Python 3
- matplotlib (para visualización)

## Instalación

### Opción 1: Entorno virtual (recomendado)
```bash
python3 -m venv venv
source venv/bin/activate
pip install matplotlib
```

### Opción 2: Paquete del sistema
```bash
sudo apt install python3-matplotlib
```

## Uso

### Entrenar el modelo
```bash
python training.py
```

Salida:
```
theta0: 8481.17
theta1: -0.0213
MSE: 445727.42
```

### Hacer predicciones y evaluar
```bash
python predict.py
```

Introduce el kilometraje cuando se te pida:
```
Enter the car mileage: 100000
The estimated price is: 6353.80

=== Model accuracy metrics ===

MSE  (Mean Squared Error): 445727.42
RMSE (Root Mean Squared Error): 667.63
MAE  (Mean Absolute Error): 556.50
R²   (Coefficient of Determination): 0.7329

Interpretation:
- The model is off by an average of 557€ per prediction
- R² = 73.29% of the price variance is explained by the model
```

Se muestra una gráfica con:
- Puntos azules: datos reales
- Línea verde: línea de regresión
- Punto rojo: tu predicción

## Manejo de Errores

Los programas manejan todos los casos edge correctamente:

- **CSV vacío**: "Error: need at least 2 data points for linear regression"
- **Un solo dato**: "Error: need at least 2 data points for linear regression"
- **Filas incompletas**: "Error: row X is incomplete"
- **Datos inválidos**: "Error: row X has invalid data"
- **Valores negativos**: "Error: row X has negative values"
- **Valores idénticos**: "Error: all mileage/price values are identical"
- **JSON faltante**: Usa valores por defecto con advertencia
- **JSON corrupto**: "Error: trained_data.json is corrupted"
- **Entrada inválida**: Re-pide hasta introducir número válido

## Algoritmo

### Gradiente Descendente

El algoritmo ajusta iterativamente theta0 y theta1 para minimizar el error de predicción:

```
theta0 = theta0 - alpha * (1/m) * sum(y_hat - y)
theta1 = theta1 - alpha * (1/m) * sum(y_hat - y) * x
```

Donde:
- `alpha` = tasa de aprendizaje (0.1)
- `m` = número de muestras
- `y_hat` = valor predicho
- `y` = valor real

### Normalización

Los datos se normalizan usando escalado min-max:

```
x_norm = (x - x_min) / (x_max - x_min)
```

Después del entrenamiento, los parámetros se desnormalizan para trabajar con valores originales.

## Configuración

En `training.py` puedes ajustar:
- **lr** (tasa de aprendizaje): 0.1
- **iterations**: 1000

Una tasa de aprendizaje muy alta puede causar divergencia, una muy baja hará que converja lentamente.

## Calidad del Código

- Manejo exhaustivo de errores para todos los casos edge
- Validación de datos con números de fila para errores en CSV
- Validación de entrada para valores negativos/inválidos
- Validación de JSON para archivos corruptos
- Separación limpia de responsabilidades con utilidades compartidas

## Requisitos

- Python 3
- matplotlib
- Entorno tipo Unix (Linux, macOS o WSL)

## Autor

- **Mario Pico** (@Davter17)

## Licencia

Este proyecto forma parte del plan de estudios de 42 school y sigue sus directrices académicas.
