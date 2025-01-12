import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
from PIL import Image

img = Image.open("ride-sharing-app-development.jpg")
st.set_page_config(page_title = 'Dynamic pricing RideShare', page_icon = img,layout = 'wide')
st.image("ride-sharing-app-development.jpg", caption="Dynamic Pricing")



def app():
    colored_header(
    label = 'Welcome to Data :red[Prediction] page 👋🏼',
    color_name = 'red-70',
    description = 'Dynamic Pricing RideShare'
)
    
@st.cache_data
def Ride_df():
        df = pd.read_csv('New_Ride')
        return df
df=Ride_df()

df.drop(['price'],axis = 1, inplace = True)
 
with st.sidebar:
             
        distance = st.selectbox(
                "**Select Distance**",
                options = df['distance'].unique(),
            )
        drivers_available = st.selectbox(
                "**Select Drivers_Available**",
                options = df['drivers_available'].unique(),
            )
        
        ride_requests= st.selectbox(
                "**Select ride_requests**",
                options = df['ride_requests'].unique(),
            )

        
        peak_hour = st.radio(
                "**Select peak_hour**",
                options = df['peak_hour'].unique(),
                horizontal = False
            )

        temperature = st.selectbox(
                "**Select Temperature**",
                options = df['temperature'].unique(),
            )
        
        precipitation= st.radio(
                "**Select precipitation**",
                options = df['precipitation'].unique(),
                horizontal = True
            )
        visibility= st.selectbox(
                "**Select visibility**",
                options = df['visibility'].unique(),
            )
        event_nearby= st.radio(
                "**Select event_nearby**",
                options = df['event_nearby'].unique(),
                horizontal = True
            )
with open('GradientBoost_model.pkl', 'rb') as file:
            model = pickle.load(file)
        
with st.form(key = 'form',clear_on_submit=False):
 button = st.form_submit_button('**Predict**',use_container_width = True)

if button == True:
 result = model.predict([[ distance, drivers_available,ride_requests,peak_hour,temperature, precipitation,visibility,event_nearby]]) 
 st.markdown(f"## :green[*Predicted Price for the ride is {result[0]}*]")
        
        
