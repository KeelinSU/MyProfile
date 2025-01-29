# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
##cd into directory where python script is saved, then run file via streamlit
##to run streamlit from terminal: streamlit run app.py

import streamlit as st

st.title("Streamlit is amazing!")

st.title("Never use spaces in folder and file names.")

st.title("Hello world")

st.write("This is my first web app.")

# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

