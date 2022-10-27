# in this script we are going to create a dashboard for carbon footprint using UN dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
from components import card, info_map

def carbon_page(country_df, country_gdf, carbon_df):
    # create the map and informations part
    country_option = info_map(country_df, country_gdf, "carbon_page")
    # get the UN name of country selected
    UN_name = country_df[country_df["country_alpha_name"] == country_option].iloc[0,0]
    
    # filter the carbon data using the country UN name
    df_plot = carbon_df[carbon_df["Country"] == UN_name]
    # create the plolty line figures
    emission_fig = px.line(df_plot, x = "Year", y = "Emissions (thousand metric tons of carbon dioxide)",
    title = "Emissions (thousand metric tons of carbon dioxide) - " + country_option)

    emission_capita_fig = px.line(df_plot, x = "Year", y = "Emissions per capita (metric tons of carbon dioxide)",
    title = "Emissions per capita (metric tons of carbon dioxide) - " + country_option)

    # create the columns to stack plolty charts
    col11, col12 = st.columns([2,2])

    # affect plotly charts
    col11.plotly_chart(emission_fig)
    col12.plotly_chart(emission_capita_fig)
