import streamlit as st
import datetime
import numpy as np
import pandas as pd
import requests

html_path = 'https://github.com/Blandalytics/sp_roundup_spec_sheets/blob/main/7_1_25_spec_sheet.html?raw=true'

with open(html_path,'r') as f: 
    html_data = f.read()

st.html(html_data)
