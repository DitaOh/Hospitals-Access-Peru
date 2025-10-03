# 🏥 Hospitals-Access-Peru

Análisis geoespacial del acceso a hospitales públicos en el Perú, en el marco del **Diplomado en Ciencia de Datos PUCP**.

## 📂 Estructura del repositorio

```
Hospitals-Access-Peru/
├─ code/
│  ├─ app.py                 # aplicación Streamlit
│  ├─ analysis.ipynb         # notebook de análisis estático (mapas y gráficos)
│  └─ folium.ipynb           # notebook de mapas interactivos (Folium)
├─ output/                   # resultados generados que consume la app
│  ├─ mapa1_hospitales_por_distrito.png
│  ├─ mapa2_distritos_sin_hospitales.png
│  ├─ mapa3_top10_distritos.png
│  ├─ hospitales_por_departamento.csv
│  ├─ grafico_hospitales_por_departamento.png
│  ├─ mapa_hospitales_por_departamento.png
│  ├─ mapa_hospitales.html
│  └─ mapa_proximidades.html
├─ requirements.txt          # dependencias completas para reproducir análisis
└─ README.md
```

## 📊 Datos utilizados

- **MINSA – IPRESS**: subset filtrado para hospitales **operativos** con coordenadas válidas.  
- **Centros poblados (INEI)**: geometrías puntuales.  
- **Distritos y Departamentos (INEI / GORE / IGN)**: shapes administrativos.

## 🗺️ Metodología

- **CRS base**: `EPSG:4326` (lat/lon).  
- Para análisis de proximidad (buffers de **10 km** en Lima y Loreto):  
  - Se reproyectan los datos a un CRS métrico local (`estimate_utm_crs`)  
  - Se generan buffers circulares de 10 km  
  - Se identifican los **centros poblados más aislados** y los **más concentrados** en hospitales.  
  - Se vuelve a `EPSG:4326` para exportar a mapas Folium.  

- Hospitales asignados a distritos/departamentos usando `geopandas.sjoin(..., predicate="within")`.  
- Resultados:
  - **Estáticos (PNG/CSV)** para análisis y reporte.
  - **Interactivos (HTML)** con Folium para visualización dinámica.

## ⚙️ Reproducibilidad

Requiere librerías geoespaciales (GeoPandas, Fiona, Shapely, etc.).

```bash
pip install -r requirements.txt
```

Luego correr los notebooks:

```bash
jupyter notebook code/analysis.ipynb
jupyter notebook code/folium.ipynb
```

Esto generará/actualizará todos los archivos en `output/`.

Ejecutar la app desde la raíz del proyecto:

```bash
streamlit run code/app.py
```

La aplicación abrirá en `http://localhost:8501` y mostrará 3 pestañas:
1. **Data Description**
2. **Static Maps & Department Analysis**
3. **Dynamic Maps**

## 📺 Video de demostración

👉 [Enlace al video en YouTube](https://youtube.com/)  

## 👥 Integrantes

- Diana  
- Pedro  
- María Paula  
- Nadia
