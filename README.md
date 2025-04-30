<p align="center">
  <img src="https://img.shields.io/badge/Master%20Project-Data%20Science-blue" alt="Master Project"/>
  <img src="https://img.shields.io/badge/XGBoost-Forecasting-orange" alt="XGBoost"/>
  <img src="https://img.shields.io/badge/PowerBI-Dashboard-yellow" alt="Power BI"/>
</p>

<h1 align="center">🛒 DsMarketStore</h1>
<p align="center"><strong>Retail Analytics & Sales Forecasting End-to-End</strong></p>

<p align="center">
  <a href="#business-context">📈 Business Context</a> •
  <a href="#objectives">🎯 Objectives</a> •
  <a href="#methodology">🛠️ Methodology</a> •
  <a href="#project-structure">📂 Structure</a> •
  <a href="#installation">💻 Installation</a> •
  <a href="#usage">🚀 Usage</a> •
  <a href="#results--insights">🔍 Results</a> •
  <a href="#future-work">🔮 Future</a> •
  <a href="#license">📄 License</a>
</p>

---

## 🏬 Business Context

DSMarket es una cadena omnicanal en EE. UU. que busca optimizar inventarios, precios y marketing mediante un enfoque **data-driven**.

---

## 🎯 Objectives

- **EDA:** Limpieza y análisis de ventas, precios y eventos.  
- **Clustering:** Segmentación de tiendas y productos.  
- **Forecasting:** Pronóstico de ventas a 28 días con XGBoost.  
- **Dashboarding:** Informes interactivos en Power BI.

---

## 🛠️ Methodology

| Phase                                | Tools & Techniques                     |
|--------------------------------------|----------------------------------------|
| 1. Exploratory Data Analysis (EDA)   | Pandas, Matplotlib, outlier detection  |
| 2. Clustering                        | PCA, K-Means, Silhouette               |
| 3. Sales Forecasting                 | XGBoost, GridSearchCV, RMSE            |
| 4. Dashboard & Reporting             | Power BI Desktop (`.pbix`), filters    |

---

## 📂 Project Structure

```
DsMarketStore/
├── .gitignore
├── Informe_DSMarket_Retail-3.pdf      # Informe final
├── Visualización_Ventas(BI).pbix     # Dashboard Power BI
├── preprocessing_datos.py            # Limpieza y feature engineering
├── análisis_ventas_py                 # EDA script
├── cluster_tiendas.py                 # Clustering tiendas
├── cluster_productos.py               # Clustering productos
├── timeseries_forecast.py             # Forecasting XGBoost
├── graficos.py                        # Utilidades de gráficos
└── README.md                          # Descripción del proyecto
```

---

## 💻 Installation

```bash
git clone https://github.com/EduBayarri/DsMarketStore.git
cd DsMarketStore
python3 -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 Usage

1. **Data Preparation**  
   ```bash
   python preprocessing_datos.py
   ```

2. **Clustering**  
   ```bash
   python cluster_tiendas.py
   python cluster_productos.py
   ```

3. **Forecasting**  
   ```bash
   python timeseries_forecast.py
   ```

4. **Dashboard**  
   Abre `Visualización_Ventas(BI).pbix` en Power BI Desktop.

---

## 🔍 Results & Insights

- **Clusters:** Grupos de tiendas y productos con patrones de venta similares.  
- **Forecast:** RMSE ~X para horizonte de 28 días (consulta el informe PDF para métricas).  
- **Dashboard:** Interfaz filtrable por ciudad, categoría y fecha.

---

## 🔮 Future Work

- **API & Docker:** Desplegar el modelo con FastAPI en contenedores Docker.  
- **CI/CD:** Integrar pipelines automáticos para reentrenamiento y despliegue.  
- **Sentiment Analysis:** Integrar análisis de sentimiento de reseñas.

---

## 📄 License

MIT © Eduardo Bayarri
