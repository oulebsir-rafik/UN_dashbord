# in this script we are going to save the functions needed to make some components
# of our streamlit web app
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

def card(text_dict):
    """ This function uses streamlit to create card
    text_dict : represent the text to be added to the card in form of python dict
    """
    for key in text_dict.keys():
        #st.markdown("""<h5 style="display:inline;"> {title} : </h5> 
                        #<h6 style="display:inline;"> {text} </h6>""".format(title = key, text = text_dict[key][0]),
                        #unsafe_allow_html = True)

        st.markdown("**{title} :**  {text}".format(title = key, text = text_dict[key][0]))

def info_map(country_df, country_geo_df, key_page):
    """ this function uses streamlit to create a map and information card using dataframes and geodataframes"""
    # divide the layout into columns
    col1, col2 = st.columns([2, 4]) 

    # get the list of countries in the dataset
    country_list = country_df["country_alpha_name"].unique()

    # add dropdown menu
    country_option = col1.selectbox("Select a Country", options = country_list, 
                    index = 125, key = key_page + "_selectbox")

    # filter the data using the result of the selectbox
    country_selected = country_df[country_df["country_alpha_name"] == country_option]
    country_info = country_selected[["iso_name","region", "subregion", "capital", 
                "area", "population", "wiki"]].to_dict(orient='list')
    
    # print all information of the country in a form of a card
    with col1:
        card(country_info)
    
    # get the latitude and longitude of the country selected
    map_loc = [country_df[country_df["country_alpha_name"] == country_option].iloc[0,5],
            country_df[country_df["country_alpha_name"] == country_option].iloc[0,6]]

    country_map = country_geo_df[~country_geo_df.is_empty].explore("iso_name",
                    m = folium.Map(location=map_loc, zoom_start=4),
                    legend=False)

    with col2:
        map_comp = st_folium(country_map, width = 700, height=400, key = key_page + "_map")

    return country_option