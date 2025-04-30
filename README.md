# DsMarketStore – Retail Analytics & Sales Forecasting End-to-End

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Proyecto final del Máster en Data Science (Nuclio Digital School)**  
Solución completa para DSMarket: desde la exploración de datos y segmentación de tiendas/productos, hasta la predicción de ventas a 28 días y la generación de dashboards interactivos.

---

## 📋 Contenidos

- [Business Context](#business-context)  
- [Objectives](#objectives)  
- [Data](#data)  
- [Methodology](#methodology)  
  - [1. Exploratory Data Analysis (EDA)](#1-exploratory-data-analysis-eda)  
  - [2. Clustering](#2-clustering)  
  - [3. Sales Forecasting](#3-sales-forecasting)  
  - [4. Dashboard & Reporting](#4-dashboard--reporting)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results & Insights](#results--insights)  
- [Future Work](#future-work)  
- [Team & Acknowledgements](#team--acknowledgements)  
- [License](#license)

---

## Business Context

DSMarket es una cadena omnicanal (físico + online) en EE. UU. que busca convertirse en una empresa data-driven. Este proyecto aborda la optimización de inventarios, precios y estrategias de marketing mediante técnicas avanzadas de Data Science.

---

## Objectives

1. **EDA**: Limpieza, unificación y análisis de datos de ventas, precios y eventos.  
2. **Clustering**: Segmentación de tiendas y productos para campañas personalizadas.  
3. **Forecasting**: Modelo XGBoost para predecir ventas a 28 días (métrica principal: RMSE).  
4. **Dashboarding**: Creación de informes interactivos en Power BI para la toma de decisiones.

---

## Data

> _Nota: los archivos raw CSV no están incluidos en el repo por tamaño._  
> Para reproducir los resultados, descarga los CSV de tu fuente original y colócalos en `data_dsmarket/`.

- **data_dsmarket/**  
  - `daily_calendar_with_events.csv`  
  - `item_prices.csv`  
  - `item_sales.csv`

---

## Methodology

### 1. Exploratory Data Analysis (EDA)
- Limpieza y tratamiento de nulos.  
- Análisis de tendencias y estacionalidad por ciudad (New York, Boston, Philadelphia).  
- Visualización de patrones de ventas y outliers.

### 2. Clustering
- **Feature engineering**: ratios de ventas, variación de precios, efectos de eventos.  
- **PCA** para reducción de dimensión.  
- **K-Means**: selección de _k_ óptimo mediante codo y coeficiente Silhouette.

### 3. Sales Forecasting
- Modelo **XGBoostRegressor** con búsqueda de hiperparámetros (GridSearchCV).  
- División Train/Validation/Test temporal y _early stopping_.  
- Evaluación con **RMSE**.

### 4. Dashboard & Reporting
- Dashboard interactivo en **Power BI** (`Visualización_Ventas(BI).pbix`).  
- Visualizaciones clave: ventas por cluster, pronóstico vs real, sensibilidad por evento.

---

## Project Structure

DsMarketStore/ ├── .gitignore ├── Informe_DSMarket_Retail-3.pdf # Informe final del proyecto ├── Visualización_Ventas(BI).pbix # Dashboard Power BI ├── análisis_ventas_py # Script EDA ├── cluster_tiendas.py # Clustering de tiendas ├── cluster_productos.py # Clustering de productos ├── graficos.py # Generación de gráficos ├── preprocessing_datos.py # Preprocesamiento de datos └── timeseries_forecast.py # Forecasting XGBoost

---

## Installation

```bash
git clone https://github.com/EduBayarri/DsMarketStore.git
cd DsMarketStore
python3 -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt

---

### Usage

## 1.Preprocesar datos

python preprocessing_datos.py


## 2.Clustering

python cluster_tiendas.py
python cluster_productos.py


## 3.Forecasting

python timeseries_forecast.py


## 4.Power BI

Abre Visualización_Ventas(BI).pbix en Power BI Desktop para explorar los dashboards.


### Results & Insights

Se definieron clusters de tiendas con comportamiento de ventas similar.

El modelo XGBoost alcanzó un RMSE de ~X en validación (detalles en el informe PDF).

Dashboard filtrable por ciudad, categoría y fecha, facilita la planificación de reabastecimientos.


### Future Work

Desplegar modelo vía API REST y contenedores Docker.

Integrar pipelines CI/CD para reentrenamiento automático.

Añadir análisis de sentimiento de reviews de clientes y precios dinámicos.


### Team & Acknowledgements

Máster DS & IA 2024, Nuclio Digital School

Eduardo Bayarri

Victor Cuenca

Alan Jaén

José Manuel Ruz

Tutora: Raquel Revilla | Defensa: 16 Septiembre 2024

License
Este proyecto está bajo licencia MIT.
