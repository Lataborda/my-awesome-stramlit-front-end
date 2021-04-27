import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image

# set the style for seaborn

image = Image.open('logo_scaling.png')
st.image(image)


st.title('Dashboard for find Flash Dryers costs per country')
sns.set_style('darkgrid')

st.markdown('**First step for the Cassava flour processing finacial assessment**')


def load_data():
	df = pd.read_csv('data/pricesf_dryer.csv', index_col='Flash Dryer Capacity and price')


	return df 


data = load_data()

# st.write(data)
if st.checkbox('Show data'):
	st.subheader('Show data')
	st.write(data)

numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
print(numeric_columns)



st.sidebar.subheader('Scatter plot setup')
Select_box1 = st.sidebar.selectbox(label='x axis', options=numeric_columns)

Select_box2 = st.sidebar.selectbox(label='y axis', options=numeric_columns)

# create scatterplot
sns.relplot(x=Select_box1, y=Select_box2, data=data)
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)


st.header('FLash Dryer prices per counstry')


sel_col, disp_col = st.beta_columns(2)



Flash_Dryer_Capacity = sel_col.slider('Select the Flash_Dryer_Capacity (Kg/hr) that you need', min_value=50, max_value=700, value=300, step=50)

User_country = sel_col.selectbox('In which country will the flash dryer be manufactured?', options=['DR. Congo','Nigeria','Colombia','Other'], index=0)


Price_1 = data[data['FD_capacity']==Flash_Dryer_Capacity]['FD_price_LT']
Price_2 = data[data['FD_capacity']==Flash_Dryer_Capacity]['FD_price_DRC']
Price_3 = data[data['FD_capacity']==Flash_Dryer_Capacity]['FD_price_NIG']

st.markdown('*Here is the price of the flash dryer according to the capacity you have chosen*')

if User_country == 'Colombia':
	st.subheader(Price_1)

elif User_country == 'Nigeria':
	st.subheader(Price_3)

elif User_country == 'DR. Congo':
	st.subheader(Price_2)


image = Image.open('logo_rtb.png')
st.image(image)

st.markdown('*Copyright (C) 2021 CIRAD & CIAT*')
st.markdown('**Authors: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Thierry Tran (thierry.tran@cirad.fr)**')











