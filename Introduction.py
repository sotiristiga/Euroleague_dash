

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from math import ceil
from datetime import date
from streamlit_dynamic_filters import DynamicFilters
import urllib.request
from PIL import Image
import time
st.set_page_config(layout='wide',page_title="Euroleague",page_icon="🏀")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('data:image/png;base64,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',
               'eurologo.svg')
st.image(Image.open("eurologo.svg"),width=400)
def fixture_format1(Fixture):
    if Fixture<=15:
        return "First Round"
    elif Fixture>15 and Fixture<=30:
        return "Second Round"
    elif Fixture==31:
        return "PO 1"
    elif Fixture == 32:
        return "PO 2"
    elif Fixture == 33:
        return "PO 3"
    elif Fixture == 34:
        return "PO 4"
    elif Fixture == 35:
        return "PO 5"
    elif Fixture==36:
        return "Semi Final"
    elif Fixture==37:
        return "Third Place"
    elif Fixture==38:
        return "Final"
def fixture_format2(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 30:
        return "Second Round"
    elif Fixture == 31:
        return "PO 1"
    elif Fixture == 32:
        return "PO 2"
    elif Fixture == 33:
        return "PO 3"
    elif Fixture == 34:
        return "PO 4"
    elif Fixture == 35:
        return "Semi Final"
    elif Fixture == 36:
        return "Third Place"
    elif Fixture == 37:
        return "Final"
def fixture_format3(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 34:
        return "Second Round"
def fixture_format4(Fixture):
    if Fixture <= 15:
        return "First Round"
    elif Fixture > 15 and Fixture <= 34:
        return "Second Round"
    elif Fixture == 35:
        return "PO 1"
    elif Fixture == 36:
        return "PO 2"
    elif Fixture == 37:
        return "PO 3"
    elif Fixture == 38:
        return "PO 4"
    elif Fixture == 39:
        return "PO 5"
    elif Fixture == 40:
        return "Semi Final"
    elif Fixture == 41:
        return "Third Place"
    elif Fixture == 42:
        return "Final"

def fixture_format5(Fixture):
        if Fixture <= 15:
            return "First Round"
        elif Fixture > 15 and Fixture <= 34:
            return "Second Round"
        elif Fixture == 35:
            return "PI 1"
        elif Fixture == 36:
            return "PI 2"
        elif Fixture == 37:
            return "PO 1"
        elif Fixture == 38:
            return "PO 2"
        elif Fixture == 39:
            return "PO 3"
        elif Fixture == 40:
            return "PO 4"
        elif Fixture == 41:
            return "PO 5"
        elif Fixture == 42:
            return "Semi Final"
        elif Fixture == 43:
            return "Third Place"
        elif Fixture == 44:
            return "Final"



lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

def metrics_customize(red,green,blue,iconname,sline,i):

    htmlstr = f"""<p style='background-color: rgb({red},{green},{blue}, 0.75); 
                        color: rgb(0,0,0, 0.75); 
                        font-size: 25px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 22px; 
                        margin-top: 0;'>{sline}</style></span></p>"""
    return htmlstr
euroleague_2016_2017_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_playerstats.csv")
euroleague_2016_2017_playerstats['idseason']=euroleague_2016_2017_playerstats['IDGAME'] + "_" + euroleague_2016_2017_playerstats['Season']
euroleague_2016_2017_playerstats[['Fixture', 'Game']] = euroleague_2016_2017_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2016_2017_playerstats['Fixture']=pd.to_numeric(euroleague_2016_2017_playerstats['Fixture'])
euroleague_2016_2017_playerstats['Round']=euroleague_2016_2017_playerstats['Fixture'].apply(fixture_format1)


euroleague_2017_2018_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_playerstats.csv")
euroleague_2017_2018_playerstats['idseason']=euroleague_2017_2018_playerstats['IDGAME'] + "_" + euroleague_2017_2018_playerstats['Season']
euroleague_2017_2018_playerstats[['Fixture', 'Game']] = euroleague_2017_2018_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2017_2018_playerstats['Fixture']=pd.to_numeric(euroleague_2017_2018_playerstats['Fixture'])
euroleague_2017_2018_playerstats['Round']=euroleague_2017_2018_playerstats['Fixture'].apply(fixture_format2)


euroleague_2018_2019_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_playerstats.csv")
euroleague_2018_2019_playerstats['idseason']=euroleague_2018_2019_playerstats['IDGAME'] + "_" + euroleague_2018_2019_playerstats['Season']
euroleague_2018_2019_playerstats[['Fixture', 'Game']] = euroleague_2018_2019_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2018_2019_playerstats['Fixture']=pd.to_numeric(euroleague_2018_2019_playerstats['Fixture'])
euroleague_2018_2019_playerstats['Round']=euroleague_2018_2019_playerstats['Fixture'].apply(fixture_format1)


euroleague_2019_2020_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_playerstats.csv")
euroleague_2019_2020_playerstats['idseason']=euroleague_2019_2020_playerstats['IDGAME'] + "_" + euroleague_2019_2020_playerstats['Season']
euroleague_2019_2020_playerstats[['Fixture', 'Game']] = euroleague_2019_2020_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2019_2020_playerstats['Fixture']=pd.to_numeric(euroleague_2019_2020_playerstats['Fixture'])
euroleague_2019_2020_playerstats['Round']=euroleague_2019_2020_playerstats['Fixture'].apply(fixture_format3)


euroleague_2020_2021_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_playerstats.csv")
euroleague_2020_2021_playerstats['idseason']=euroleague_2020_2021_playerstats['IDGAME'] + "_" + euroleague_2020_2021_playerstats['Season']
euroleague_2020_2021_playerstats[['Fixture', 'Game']] = euroleague_2020_2021_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2020_2021_playerstats['Fixture']=pd.to_numeric(euroleague_2020_2021_playerstats['Fixture'])
euroleague_2020_2021_playerstats['Round']=euroleague_2020_2021_playerstats['Fixture'].apply(fixture_format4)

euroleague_2021_2022_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_playerstats.csv")
euroleague_2021_2022_playerstats['idseason']=euroleague_2021_2022_playerstats['IDGAME'] + "_" + euroleague_2021_2022_playerstats['Season']
euroleague_2021_2022_playerstats[['Fixture', 'Game']] = euroleague_2021_2022_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2021_2022_playerstats['Fixture']=pd.to_numeric(euroleague_2021_2022_playerstats['Fixture'])
euroleague_2021_2022_playerstats['Round']=euroleague_2021_2022_playerstats['Fixture'].apply(fixture_format4)


euroleague_2022_2023_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_playerstats.csv")
euroleague_2022_2023_playerstats['idseason']=euroleague_2022_2023_playerstats['IDGAME'] + "_" + euroleague_2022_2023_playerstats['Season']
euroleague_2022_2023_playerstats[['Fixture', 'Game']] = euroleague_2022_2023_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2022_2023_playerstats['Fixture']=pd.to_numeric(euroleague_2022_2023_playerstats['Fixture'])
euroleague_2022_2023_playerstats['Round']=euroleague_2022_2023_playerstats['Fixture'].apply(fixture_format4)

euroleague_2023_2024_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_playerstats.csv")
euroleague_2023_2024_playerstats['idseason']=euroleague_2023_2024_playerstats['IDGAME'] + "_" + euroleague_2023_2024_playerstats['Season']
euroleague_2023_2024_playerstats[['Fixture', 'Game']] = euroleague_2023_2024_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2023_2024_playerstats['Fixture']=pd.to_numeric(euroleague_2023_2024_playerstats['Fixture'])
euroleague_2023_2024_playerstats['Round']=euroleague_2023_2024_playerstats['Fixture'].apply(fixture_format5)

euroleague_2024_2025_playerstats=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_playerstats.csv")
euroleague_2024_2025_playerstats['idseason']=euroleague_2024_2025_playerstats['IDGAME'] + "_" + euroleague_2024_2025_playerstats['Season']
euroleague_2024_2025_playerstats[['Fixture', 'Game']] = euroleague_2024_2025_playerstats['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2024_2025_playerstats['Fixture']=pd.to_numeric(euroleague_2024_2025_playerstats['Fixture'])
euroleague_2024_2025_playerstats['Round']=euroleague_2024_2025_playerstats['Fixture'].apply(fixture_format5)



euroleague_2016_2017_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2016_2017_results.csv")
euroleague_2016_2017_results['idseason']=euroleague_2016_2017_results['IDGAME'] + "_" + euroleague_2016_2017_results['Season']
euroleague_2016_2017_results[['Fixture', 'Game']] = euroleague_2016_2017_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2016_2017_results['Fixture']=pd.to_numeric(euroleague_2016_2017_results['Fixture'])
euroleague_2016_2017_results['Round']=euroleague_2016_2017_results['Fixture'].apply(fixture_format1)


euroleague_2017_2018_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2017_2018_results.csv")
euroleague_2017_2018_results['idseason']=euroleague_2017_2018_results['IDGAME'] + "_" + euroleague_2017_2018_results['Season']
euroleague_2017_2018_results[['Fixture', 'Game']] = euroleague_2017_2018_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2017_2018_results['Fixture']=pd.to_numeric(euroleague_2017_2018_results['Fixture'])
euroleague_2017_2018_results['Round']=euroleague_2017_2018_results['Fixture'].apply(fixture_format2)


euroleague_2018_2019_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2018_2019_results.csv")
euroleague_2018_2019_results['idseason']=euroleague_2018_2019_results['IDGAME'] + "_" + euroleague_2018_2019_results['Season']
euroleague_2018_2019_results[['Fixture', 'Game']] = euroleague_2018_2019_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2018_2019_results['Fixture']=pd.to_numeric(euroleague_2018_2019_results['Fixture'])
euroleague_2018_2019_results['Round']=euroleague_2018_2019_results['Fixture'].apply(fixture_format1)


euroleague_2019_2020_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2019_2020_results.csv")
euroleague_2019_2020_results['idseason']=euroleague_2019_2020_results['IDGAME'] + "_" + euroleague_2019_2020_results['Season']
euroleague_2019_2020_results[['Fixture', 'Game']] = euroleague_2019_2020_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2019_2020_results['Fixture']=pd.to_numeric(euroleague_2019_2020_results['Fixture'])
euroleague_2019_2020_results['Round']=euroleague_2019_2020_results['Fixture'].apply(fixture_format3)


euroleague_2020_2021_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2020_2021_results.csv")
euroleague_2020_2021_results['idseason']=euroleague_2020_2021_results['IDGAME'] + "_" + euroleague_2020_2021_results['Season']
euroleague_2020_2021_results[['Fixture', 'Game']] = euroleague_2020_2021_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2020_2021_results['Fixture']=pd.to_numeric(euroleague_2020_2021_results['Fixture'])
euroleague_2020_2021_results['Round']=euroleague_2020_2021_results['Fixture'].apply(fixture_format4)

euroleague_2021_2022_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2021_2022_results.csv")
euroleague_2021_2022_results['idseason']=euroleague_2021_2022_results['IDGAME'] + "_" + euroleague_2021_2022_results['Season']
euroleague_2021_2022_results[['Fixture', 'Game']] = euroleague_2021_2022_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2021_2022_results['Fixture']=pd.to_numeric(euroleague_2021_2022_results['Fixture'])
euroleague_2021_2022_results['Round']=euroleague_2021_2022_results['Fixture'].apply(fixture_format4)


euroleague_2022_2023_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2022_2023_results.csv")
euroleague_2022_2023_results['idseason']=euroleague_2022_2023_results['IDGAME'] + "_" + euroleague_2022_2023_results['Season']
euroleague_2022_2023_results[['Fixture', 'Game']] = euroleague_2022_2023_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2022_2023_results['Fixture']=pd.to_numeric(euroleague_2022_2023_results['Fixture'])
euroleague_2022_2023_results['Round']=euroleague_2022_2023_results['Fixture'].apply(fixture_format4)

euroleague_2023_2024_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2023_2024_results.csv")
euroleague_2023_2024_results['idseason']=euroleague_2023_2024_results['IDGAME'] + "_" + euroleague_2023_2024_results['Season']
euroleague_2023_2024_results[['Fixture', 'Game']] = euroleague_2023_2024_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2023_2024_results['Fixture']=pd.to_numeric(euroleague_2023_2024_results['Fixture'])
euroleague_2023_2024_results['Round']=euroleague_2023_2024_results['Fixture'].apply(fixture_format5)

euroleague_2024_2025_results=pd.read_csv(f"https://raw.githubusercontent.com/sotiristiga/euroleague/main/euroleague_2024_2025_results.csv")
euroleague_2024_2025_results['idseason']=euroleague_2024_2025_results['IDGAME'] + "_" + euroleague_2024_2025_results['Season']
euroleague_2024_2025_results[['Fixture', 'Game']] = euroleague_2024_2025_results['IDGAME'].str.split('_', n=1, expand=True)
euroleague_2024_2025_results['Fixture']=pd.to_numeric(euroleague_2024_2025_results['Fixture'])
euroleague_2024_2025_results['Round']=euroleague_2024_2025_results['Fixture'].apply(fixture_format5)


All_Seasons=pd.concat([euroleague_2016_2017_playerstats,euroleague_2017_2018_playerstats,euroleague_2018_2019_playerstats,euroleague_2019_2020_playerstats,euroleague_2020_2021_playerstats,euroleague_2021_2022_playerstats,euroleague_2022_2023_playerstats,euroleague_2023_2024_playerstats,euroleague_2024_2025_playerstats])

All_Seasons_res=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results,euroleague_2024_2025_results])

st.write("# Euroleague Stats from 2016-2017 to present")

kpi1, kpi2, kpi3, kpi4,kpi5 = st.columns(5)
with kpi1:
    st.markdown(lnk + metrics_customize(240,153,48,"","Total Games",All_Seasons['idseason'].nunique()), unsafe_allow_html=True)
    st.markdown(lnk + metrics_customize(240,153,48,"","Total Teams",All_Seasons['Team'].nunique()), unsafe_allow_html=True)
    st.markdown(lnk + metrics_customize(240,153,48, "", "Total Players", All_Seasons['Player'].nunique()),
        unsafe_allow_html=True)

with kpi2:
    st.markdown(lnk + metrics_customize(240,153,48, "", "Total Points", All_Seasons['PTS'].sum()),
                unsafe_allow_html=True)
    st.markdown(lnk + metrics_customize(240,153,48, "", "Total Assists", All_Seasons['AS'].sum()),
                unsafe_allow_html=True)
    st.markdown(lnk + metrics_customize(240,153,48, "", "Total Steals", All_Seasons['ST'].sum()),
                unsafe_allow_html=True)

with kpi3:
    st.markdown(
        lnk + metrics_customize(240,153,48, "", "Total 3P Points Made", All_Seasons['F3M'].sum()),
        unsafe_allow_html=True)
    st.markdown(
        lnk + metrics_customize(240,153,48, "", "Total 2P Points Made", All_Seasons['F2M'].sum()),
        unsafe_allow_html=True)
    st.markdown(
        lnk + metrics_customize(240,153,48, "", "Total Free Throws Points Made",
                                All_Seasons['FTM'].sum()),
        unsafe_allow_html=True)

with kpi4:
    st.markdown(
        lnk + metrics_customize(240,153,48, "", "Total Turnovers", All_Seasons['TO'].sum()),
        unsafe_allow_html=True)
    st.markdown(
        lnk + metrics_customize(240,153,48, "", "Total Blocks", All_Seasons['BLK'].sum()),
        unsafe_allow_html=True)
    st.markdown(
        lnk + metrics_customize(240,153,48, "", "Total Fouls",
                                All_Seasons['PF'].sum()),
        unsafe_allow_html=True)

