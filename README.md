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

DSMarket es una cadena omnicanal en EE. UU. que busca optimizar inventarios, precios y marketing mediante un enfoque **data-driven**.

---

## 🎯 Objectives

- **EDA:** Limpieza y análisis de ventas, precios y eventos.  
- **Clustering:** Segmentación de tiendas y productos.  
- **Forecasting:** Pronóstico de ventas a 28 días con XGBoost.  
- **Dashboarding:** Informes interactivos en Power BI.

---

## 🛠️ Methodology

| Phase                                    | Tools & Techniques                         |
|------------------------------------------|--------------------------------------------|
| 1. Exploratory Data Analysis (EDA)       | Pandas, Matplotlib, outlier detection      |
| 2. Clustering                            | PCA, K-Means, Silhouette                   |
| 3. Sales Forecasting                     | XGBoost, GridSearchCV, RMSE                |
| 4. Dashboard & Reporting                 | Power BI Desktop (`.pbix`), visual filters |

---

## 📂 Project Structure

DsMarketStore/ ├── .gitignore ├── Informe_DSMarket_Retail-3.pdf # Report ├── Visualización_Ventas(BI).pbix # Power BI dashboard ├── preprocessing_datos.py # Data cleaning & features ├── análisis_ventas_py # EDA script ├── cluster_tiendas.py # Store clustering ├── cluster_productos.py # Product clustering ├── timeseries_forecast.py # XGBoost forecasting ├── graficos.py # Plotting utilities └── README.md # Project overview

yaml
Copiar
Editar

---

## 💻 Installation

```bash
git clone https://github.com/EduBayarri/DsMarketStore.git
cd DsMarketStore
python3 -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
🚀 Usage
Data prep & features

bash
Copiar
Editar
python preprocessing_datos.py
Clustering

bash
Copiar
Editar
python cluster_tiendas.py
python cluster_productos.py
Forecasting

bash
Copiar
Editar
python timeseries_forecast.py
Dashboard

Abre Visualización_Ventas(BI).pbix en Power BI Desktop.

🔍 Results & Insights
Clusters: Agrupaciones de tiendas/prod. con patrones similares.

Forecast: RMSE ~X para horizonte de 28 días.

BI Dashboard: Filtros por ciudad, categoría y evento para planificar reabastecimientos.

🔮 Future Work
🚀 API REST para servir el modelo.

🐳 Docker & CI/CD para despliegue automático.

📊 Análisis de sentimiento de reseñas para pricing dinámico.

