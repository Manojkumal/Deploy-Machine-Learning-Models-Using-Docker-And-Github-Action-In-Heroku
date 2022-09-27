import streamlit as st
import json
import requests
import math
headers = {
    'Content-Type': 'application/json'
    }
demo_api_url = "http://0.0.0.0:8501/predict"


st.title("Flight Price Prediction :airplane:")
total_stops = st.slider("Choose Total_Stops ",0,6)
Journey_day = st.slider("Choose Journey_day",1,30)
Journey_month = st.slider("Choose Journey_month",1,12)
Dep_hour = st.slider("Choose Departure_hours",1,12)
Dep_min = st.slider("Choose Departure_mins",1,60)
Arrival_hour = st.slider("Choose Arrival_hour",1,6)
Arrival_min = st.slider("Choose Arrival_min",0,60)
Duration_hours = st.slider("Choose Duration_hours",1,48)
Duration_mins = st.slider("Choose Duration_mins",1,60)
Airline_Air_India = st.select_slider("Choose AirIndia Airline",[0,1])
Airline_GoAir = st.select_slider("Choose GoAir Airline",[0,1])
Airline_IndiGo = st.select_slider("Choose IndiGo Airline",[0,1])
Airline_Jet_Airways = st.select_slider("Choose Jet_Airways Airline",[0,1])
Airline_Jet_Airways_Business = st.select_slider("Choose Jet_Airways_Business Airline",[0,1])
Airline_Multiple_carriers = st.select_slider("Choose Multiple_carriers Airline",[0,1])
Airline_Multiple_carriers_Premium_economy = st.select_slider("Choose carriers_Premium_economy Airline",[0,1])
Airline_SpiceJet = st.select_slider("Choose SpiceJet Airline",[0,1])
Airline_Trujet = st.select_slider("Choose Trujet Airline",[0,1])
Airline_Vistara = st.select_slider("Choose Vistara Airline",[0,1])
Airline_Vistara_Premium_economy = st.select_slider("Choose Premium_economy Airline",[0,1])
Source_Chennai = st.select_slider("Choose Source Chennai",[0,1])
Source_Delhi = st.select_slider("Choose Source Delhi",[0,1])
Source_Kolkata = st.select_slider("Choose Source Kolkata",[0,1])
Source_Mumbai = st.select_slider("Choose Source Mumbai",[0,1])
Destination_Cochin = st.select_slider("Choose Destination Cochin",[0,1])
Destination_Delhi = st.select_slider("Choose Destination Delhi",[0,1])
Destination_Hyderabad = st.select_slider("Choose Destination Hyderabad",[0,1])
Destination_Kolkata = st.select_slider("Choose Destination Kolkata",[0,1])
Destination_New_Delhi = st.select_slider("Choose Destination new_delhi",[0,1])


def api_call():
    new_data = {"total_stops":total_stops,"Journey_day":Journey_day,"Journey_month":Journey_month,"Dep_hour":Dep_hour,"Dep_min":Dep_min,"Arrival_hour":Arrival_hour,"Arrival_min":Arrival_min,"Duration_hours":Duration_hours,"Duration_mins":Duration_mins,
    "Airline_Air_India":Airline_Air_India,"Airline_GoAir":Airline_GoAir,"Airline_IndiGo":Airline_IndiGo,"Airline_Jet_Airways":Airline_Jet_Airways,Airline_Jet_Airways_Business:Airline_Jet_Airways_Business,"Airline_Multiple_carriers":Airline_Multiple_carriers,
    "Airline_Multiple_carriers_Premium_economy":Airline_Multiple_carriers_Premium_economy,"Airline_SpiceJet":Airline_SpiceJet,"Airline_Trujet":Airline_Trujet,"Airline_Vistara":Airline_Vistara,"Airline_Vistara_Premium_economy":Airline_Vistara_Premium_economy,
    "Source_Chennai":Source_Chennai,"Source_Delhi":Source_Delhi,"Source_Kolkata":Source_Kolkata,"Source_Mumbai":Source_Mumbai,"Destination_Cochin":Destination_Cochin,"Destination_Delhi":Destination_Delhi,"Destination_Hyderabad":Destination_Hyderabad,
    "Destination_Kolkata":Destination_Kolkata,"Destination_New_Delhi":Destination_New_Delhi}

    payload = json.dumps({
        "data":new_data
    
    })
    demo_api_response = requests.request("POST", demo_api_url, headers=headers, data=payload)
    final_demo_api_response = json.loads(demo_api_response.text)
    if final_demo_api_response is not None:
        st.write("The Flight Price is : ","{:.2f}".format(final_demo_api_response))
    else:
        st.write("something is wrong!! Please Check")
st.button('predict',on_click=api_call)
    






