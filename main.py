#import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# libraries for geospatial data manipulation
from shapely.wkt import loads
import geopandas as gpd

# add paths for script research
import sys
sys.path.append('./UI/')
sys.path.append('./Data/')

# import different pages and components of the dashboard
from carbon_dash import carbon_page
from land_dash import land_page
from species_dash import species_page
from components import card, info_map



# set the configuration parameter to the page
st.set_page_config(layout="wide")

# set title to the page
st.title("🌎 UN Environment Dashboard")

# modify css properties of streamlit elements
# center the title and increase size of selectbox text
title_alignment="""
<style>
#un-environment-dashboard {
  text-align: center;
  font-size: 65px;
}
.css-81oif8{
    font-size: 18px;
    font-weight: bold;
}
</style>
"""
# apply css changes using markdown
st.markdown(title_alignment, unsafe_allow_html=True)

# import the necessary data
country_df = pd.read_csv("./Data/proddata/country_info.csv")
carbon_df = pd.read_csv("./Data/proddata/carbon_data.csv")
land_df = pd.read_csv("./Data/proddata/land_data.csv")
spec_df = pd.read_csv("./Data/proddata/species_data.csv")

# create the geodataframe from dataframe
country_gdf = country_df.copy()
country_gdf["geojson"] = country_gdf['geojson'].apply(loads)
country_gdf = gpd.GeoDataFrame(country_gdf, geometry='geojson')


# add the map and country informations here
st.markdown("""<h3 style = "margin:0px; padding:6px"> 🗒 Information Section </h3>
<hr style="height : 0.5px; margin:10px">""", unsafe_allow_html=True)

country_option = info_map(country_df, country_gdf)

# create tabs for each pages

carbon_tab, land_tab, spec_tab = st.tabs(["💨Carbon Data", "🌾Land Data", "🐠 Species Data"])

with carbon_tab:
    carbon_page(country_df, country_option, carbon_df)

with land_tab:
    land_page(country_df, country_option, land_df)

with spec_tab:
    species_page(country_df, country_option, spec_df)