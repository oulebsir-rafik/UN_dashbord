# in this script we are going to create a dashboard for species footprint using UN dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
from components import card, info_map

def species_page(country_df, country_option, spec_df):
    # get the UN name of country selected
    UN_name = country_df[country_df["country_alpha_name"] == country_option].iloc[0,0]
    
    # filter the species data using the country UN name
    df_plot = spec_df[spec_df["Country"] == UN_name]

    #---------------- First row -----------------------
    # create the plolty line figures
    invert_fig = px.line(df_plot, x = "Year", y = "Threatened Species: Invertebrates (number)",
    title = "Threatened Species: Invertebrates (number) - " + country_option)

    plant_fig = px.line(df_plot, x = "Year", y = "Threatened Species: Plants (number)",
    title = "Threatened Species: Plants (number) - " + country_option)

    # create the columns to stack plolty charts
    col11, col12 = st.columns([2,2])

    # affect plotly charts
    col11.plotly_chart(invert_fig)
    col12.plotly_chart(plant_fig)

    #-------------------- Second row ---------------------
    # create the plolty line figures
    vert_fig = px.line(df_plot, x = "Year", y = "Threatened Species: Vertebrates (number)",
    title = "Threatened Species: Vertebrates (number) - " + country_option)

    total_fig = px.line(df_plot, x = "Year", y = "Threatened Species: Total (number)",
    title = "Threatened Species: Total (number) - " + country_option)

    # create the columns to stack plolty charts
    col21, col22 = st.columns([2,2])

    # affect plotly charts
    col21.plotly_chart(vert_fig)
    col22.plotly_chart(total_fig)

