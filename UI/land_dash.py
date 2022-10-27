# in this script we are going to create a dashboard for carbon footprint using UN dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
from components import card, info_map

def land_page(country_df, country_gdf, land_df):
    # create the map and informations part
    country_option = info_map(country_df, country_gdf, "land_page")
    # get the UN name of country selected
    UN_name = country_df[country_df["country_alpha_name"] == country_option].iloc[0,0]
    
    # filter the carbon data using the country UN name
    df_plot = land_df[land_df["Country"] == UN_name]
    # create the plolty line figures
    arable_fig = px.line(df_plot, x = "Year", y = "Arable land (% of total land area)",
    title = "Arable land (% of total land area) - " + country_option)

    forest_fig = px.line(df_plot, x = "Year", y = "Forest cover (% of total land area)",
    title = "Forest cover (% of total land area) - " + country_option)

    # create the columns to stack plolty charts
    col11, col12 = st.columns([2,2])

    # affect plotly charts
    col11.plotly_chart(arable_fig)
    col12.plotly_chart(forest_fig)
