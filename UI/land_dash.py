# in this script we are going to create a dashboard for land footprint using UN dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
from components import card, info_map

def land_page(country_df, country_option, land_df):
    # get the UN name of country selected
    UN_name = country_df[country_df["country_alpha_name"] == country_option].iloc[0,0]
    
    # filter the land data using the country UN name
    df_plot = land_df[land_df["Country"] == UN_name]
    # create the plolty line figures
    land_area_fig = px.line(df_plot, x = "Year", y = "Land area (thousand hectares)",
    title = "Land area (thousand hectares) - " + country_option)

    arable_fig = px.line(df_plot, x = "Year", y = "Arable land (thousand hectares)",
    title = "Arable land (thousand hectares) - " + country_option)

    forest_fig = px.line(df_plot, x = "Year", y = "Forest cover (thousand hectares)",
    title = "Forest cover (thousand hectares) - " + country_option)

    crop_fig = px.line(df_plot, x = "Year", y = "Permanent crops (thousand hectares)",
    title = "Permanent crops (thousand hectares) - " + country_option)

    #---------------------------First row---------------------------------
    # create the columns to stack plolty charts
    col11, col12 = st.columns([2,2])

    # affect plotly charts
    col11.plotly_chart(land_area_fig)
    col12.plotly_chart(arable_fig)

    #---------------------------Second row---------------------------------
    col21, col22 = st.columns([2,2])

    # affect plotly charts
    col21.plotly_chart(forest_fig)
    col22.plotly_chart(crop_fig)
