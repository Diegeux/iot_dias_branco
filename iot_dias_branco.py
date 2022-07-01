import streamlit as st
import telas.bi as bi
import telas.home as home
import telas.temp_agua_dataset as temp_agua_dataset

st.sidebar.title("Seja bem-vindo")
selection = st.sidebar.selectbox('Menu',['Início','Visualizar Dataset','Inteligência de Mercado'])
if selection == 'Início':
    home.start_home()
if selection == 'Visualizar Dataset':
    temp_agua_dataset.start_temp_agua_dataset() 
if selection == 'Inteligência de Mercado':
    bi.start_bi()        