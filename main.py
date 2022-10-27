import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from shapely.wkt import loads
import geopandas as gpd

import sys
sys.path.append('./UI/')
sys.path.append('./Data/')

from carbon_dash import carbon_page
from land_dash import land_page

# set the configuration parameter to the page
st.set_page_config(layout="wide")

# set title to the page
st.title("UN data dashboard")

# import the necessary data
country_df = pd.read_csv("./Data/proddata/country_info.csv")
carbon_df = pd.read_csv("./Data/proddata/carbon_data.csv")
land_df = pd.read_csv("./Data/proddata/land_data.csv")

# create the geodataframe from dataframe
country_gdf = country_df.copy()
country_gdf["geojson"] = country_gdf['geojson'].apply(loads)
country_gdf = gpd.GeoDataFrame(country_gdf, geometry='geojson')


carbon_tab, land_tab = st.tabs(["💨Carbon Data", "🌾Land Data"])

with carbon_tab:
    carbon_page(country_df, country_gdf, carbon_df)

with land_tab:
    land_page(country_df, country_gdf, land_df)