import pandas as pd
import streamlit as st
from datetime import time, datetime, timedelta
from PIL import Image
import csv
import plotly.express as px
import plotly.graph_objects as go
from st_pages import Page, show_pages
import base64

def gambar(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def bg():
    img1 = gambar("img/bg_1.jpg")
    img2 = gambar("img/bg_2.jpg")

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url(data:image/jpeg;base64,{img1});
    background-size: cover;
    background-position: center;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img2}");
    background-size: cover;
    background-position: center;         
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
