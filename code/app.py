import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Configuración de la página
st.set_page_config(
    page_title="🏥 Hospitals in Peru",
    page_icon="🏥",
    layout="wide"
)

# Para el sidebar
with st.sidebar:
    st.markdown("### 🏥 Geospatial Analysis of Hospitals Access in Peru")
    st.markdown("---")
    st.markdown("**Curso:** Python Intermedio -  Diplomado PUCP")
    st.markdown("**Integrantes:** Diana, Pedro, María Paula, Nadia")

# Título principal
st.title("🏥 Geospatial Analysis of Hospitals Access in Peru")   # 👈 este aparece arriba de todo
st.markdown("### Análisis de hospitales operativos y acceso en el Perú")

# Para los tabs
tab1, tab2, tab3 = st.tabs(
    ["🗂️ Data Description", "🗺️ Static Maps & Department Analysis", "🌍 Dynamic Maps"]
)

## TAB 1: Data Description
with tab1:
    st.header("Data Description")
    
    st.subheader("Unit of Analysis")
    st.write("Operational public hospitals in Peru.")
    
    st.subheader("Data Sources")
    st.write("- MINSA – IPRESS (operational subset)")
    st.write("- Population Centers dataset")
    
    st.subheader("Filtering Rules")
    st.write("Only operational hospitals with valid latitude/longitude were considered.")

# TAB 2: Static Maps & Department Analysis
with tab2:
    st.header("Static Maps & Department Analysis")
    
    st.subheader("District level Analysis")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("Map 1. Total public hospitals per district.")
        st.image("output/mapa1_hospitales_por_distrito.png",
                caption="Number of Hospitals by District")
        
    col1, col2 = st.columns(2)
    with col1:
        st.write("Map 2. Districts with zero hospitals.")
        st.image("output/mapa2_distritos_sin_hospitales.png",
                 caption="Districts with Zero Hospitals")
        
    with col2:
        st.write("Map 3. Top 10 districts with the highest number of hospitals.")
        st.image("output/mapa3_top10_distritos.png",
                 caption="Top 10 Districts with Highest Number of Hospitals")

    st.subheader("Department level Analysis")

    st.write("Department Summary Table")
    st.write("Aquí la tabla resumen por departamento.")
    
    col1, col2 = st.columns([1.8,1.2])
    with col1:
        st.write("Graph 1. Total public hospitals per Department.")
        st.image("output/grafico_hospitales_por_departamento.png",
                 caption="Number of Hospitals by Department")
    
    with col2:
        st.write("Map 4. Total public hospitals per Department.")
        st.image("output/mapa_hospitales_por_departamento.png",
                 caption="Number of Hospitals by Department",
                 width = 400)

# TAB 3: Dynamic Maps
with tab3:
    st.header("Dynamic Maps")
    
    st.subheader("National Choropleth + Markers")
    st.write("Mapa Folium con choropleth nacional y marcadores de hospitales.")
    # folium_map = folium.Map(location=[-9.19, -75.0152], zoom_start=5)
    # st_folium(folium_map, width=700, height=500)
    
    st.subheader("Proximity Maps for Lima & Loreto")
    st.write("Mapas de proximidad")
    # Ejemplo:
    # lima_map = folium.Map(location=[-12.0464, -77.0428], zoom_start=10)
    # st_folium(lima_map, width=700, height=500)
