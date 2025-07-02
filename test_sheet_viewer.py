import streamlit as st
import datetime
import numpy as np
import pandas as pd
import requests

html_path = 'https://html-preview.github.io/?url=https://github.com/Blandalytics/sp_roundup_spec_sheets/blob/main/7_1_25_spec_sheet.html'

# with open(html_path,'r') as f: 
#     html_data = f.read()

st.html(html_path)
