from PIL import Image
import streamlit as st

def start_home():
    #st.title("IOT Dias Branco")
    #st.write("-Present and Future through one click-")
    #st.write("This is a Business Intelligence System which is able to show you data in the present and in the future and provide insights to make decisions. You will in your hands options such as Analytics and Prediction. Enjoy it as well as you may!")
    image = Image.open('telas/img_home.png')
    st.image(image, caption='')
    