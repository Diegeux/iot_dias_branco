import streamlit as st
import pyrebase
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import time

def start_bi():
    
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
    st.title("Inteligência de Mercado")

    x = 1
    z = 1
    temperatura = []
    data = []
    n_agua = []
    grafico_temperatura = st.empty()
    fx_ideal = st.empty()
    grafico_agua = st.empty()
    status_agua_1 = st.empty()
    status_agua_2 = st.empty()
    status_agua_3 = st.empty()
    status_agua_4 = st.empty()
    status_agua_5 = st.empty()
    grafico_geral = st.empty()
    sobra1 = st.empty()
    sobra2 = st.empty()

    while x == z:
        zx = datetime.datetime.now()
        date_time = zx.strftime("%H:%M:%S")
        temperatura_base = db.child('iot_m_dias').child('f_fortaleza').child('temperatura').get(user['idToken'])
        n_agua_base = db.child('iot_m_dias').child('f_fortaleza').child('n_agua').get(user['idToken'])
        temperatura.append(temperatura_base.val())
        n_agua.append(n_agua_base.val())
        data.append(date_time)
        array_temperatura=np.array(temperatura)
        array_data=np.array(data)  
        array_n_agua=np.array(n_agua)
        dataset_n_agua = pd.DataFrame(array_n_agua, columns=['Nível água (mA %)'])
        dataset_temperatura=  pd.DataFrame(array_temperatura, columns=['Temperatura (°C)'])
        dataset_data =  pd.DataFrame(array_data, columns=['Hora-Minuto-Segundo'])

        df_temperatura = pd.concat([dataset_temperatura, dataset_data], axis=1, join='inner')
        df_agua = pd.concat([dataset_n_agua, dataset_data], axis=1, join='inner')
        df_geral = pd.concat([dataset_temperatura, dataset_n_agua, dataset_data], axis=1, join='inner')
        
        #dfgeral = pd.concat([dataset_temperatura, dataset_data], axis=1, join='inner')
        #dfgeral['Data']= dfgeral['Data'].astype(float)
        #print(dfgeral)
        #grafico.dataframe(dfgeral)
        #grafico.line_chart(dfgeral['Temp'])
    
        line_fig = px.line(df_temperatura, x="Hora-Minuto-Segundo", y="Temperatura (°C)", title="Temperatura em função do tempo",width=800, height=440)
        grafico_temperatura.plotly_chart(line_fig, use_container_width=False, sharing='streamlit')
        fx_ideal.write("Temperatura ideal: 7 °C a 10°C")
        line_fig = px.line(df_agua, x="Hora-Minuto-Segundo", y="Nível água (mA %)", title="Nível da água em função do tempo",width=800, height=440)
        grafico_agua.plotly_chart(line_fig, use_container_width=False, sharing='streamlit')
        status_agua_1.write('Menor que 20%: Nível baixo da água')
        status_agua_2.write("Entre 30% e 69%: Nível ideal da água")
        status_agua_3.write("Acima de 80%: Nível alto da água")
        status_agua_4.write("Entre 20% e 29% : Atenção")
        status_agua_5.write("Entre 70% e 80% : Atenção")

        line_fig = px.line(df_geral, x="Hora-Minuto-Segundo", y=["Nível água (mA %)","Temperatura (°C)"], title="Nível da água em função do tempo",width=800, height=440)
        grafico_geral.plotly_chart(line_fig, use_container_width=False, sharing='streamlit')
        time.sleep(5)






        

