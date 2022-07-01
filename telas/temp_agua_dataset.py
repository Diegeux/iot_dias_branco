import streamlit as st
import pyrebase
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import time

def start_temp_agua_dataset():
    config = {
        "apiKey": "AIzaSyALp47c9KYsGN21KuYMLBiXztJzkTB9_RQ",
        "authDomain": "banmequer-devloide.firebaseio.com",
        "databaseURL": "https://banmequer-devloide.firebaseio.com",
        "projectID": "banmequer-devloide",
        "storageBucket": "banmequer-devloide.appspot.com",
        "messagingSenderId": "61021516767"
        }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('diego.ijcpm2017@gmail.com', 123456)
    db = firebase.database()
    st.title("Datasets")
    #print(datetime.datetime.now())

    x = 1
    z = 1
    temperatura = []
    n_agua = []
    data = []
    texto_temperatura = st.empty()
    texto_temperatura_df = st.empty()
    botao_download_temperatura = st.empty()
    texto_agua = st.empty()
    texto_agua_df = st.empty()
    botao_download_agua = st.empty()
    texto_geral = st.empty()
    texto_geral_df = st.empty()
    botao_download_geral = st.empty()
    


    while x == z:
        zx = datetime.datetime.now()
        date_time = zx.strftime("%H:%M:%S")
        temperatura_base = db.child('iot_m_dias').child('f_fortaleza').child('temperatura').get(user['idToken'])
        n_agua_base = db.child('iot_m_dias').child('f_fortaleza').child('n_agua').get(user['idToken'])
        n_agua.append(n_agua_base.val())
        temperatura.append(temperatura_base.val())
        data.append(date_time)
        array_n_agua=np.array(n_agua)
        array_temperatura=np.array(temperatura)
        array_data=np.array(data)  
        dataset_n_agua = pd.DataFrame(array_n_agua, columns=['Nível água (mA %)'])
        dataset_temperatura=  pd.DataFrame(array_temperatura, columns=['Temperatura (°C)'])
        dataset_data =  pd.DataFrame(array_data, columns=['Hora-Minuto-Segundo'])

        df_temperatura = pd.concat([dataset_temperatura, dataset_data], axis=1, join='inner')
        df_agua = pd.concat([dataset_n_agua, dataset_data], axis=1, join='inner')
        df_geral = pd.concat([dataset_temperatura, dataset_n_agua, dataset_data], axis=1, join='inner')
        #df_geral
        
        texto_temperatura_df.dataframe(df_temperatura)
        texto_temperatura.write("Dataset temperatura em função do tempo")
        
        def convert_df_temperatura(df):
            return df.to_csv().encode('utf-8')
        csv = convert_df_temperatura(df_temperatura)
        botao_download_temperatura.download_button("Download dataset temperatura (.csv)",csv,"temperatura_dataset.csv","text/csv",key='download-csv')
        
        texto_agua_df.dataframe(df_agua)
        texto_agua.write("Dataset nível da água em função do tempo")
        def convert_df_agua(df):
            return df.to_csv().encode('utf-8')
        csv = convert_df_agua(df_agua)
        botao_download_agua.download_button("Download dataset nível da água (.csv)",csv,"nivel_agua_dataset.csv","text/csv",key='download-csv')
        
        texto_geral_df.dataframe(df_geral)
        texto_geral.write("Dataset geral em função do tempo")

        def convert_df_geral(df):
            return df.to_csv().encode('utf-8')
        csv = convert_df_geral(df_geral)
        botao_download_geral.download_button("Download dataset temperatura e água (.csv)",csv,"temperatura_nivel_agua_dataset.csv","text/csv",key='download-csv')
        
        time.sleep(5)






        

