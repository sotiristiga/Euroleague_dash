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
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n, sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction)
from itables.streamlit import interactive_table
from itables import to_html_datatable
from streamlit.components.v1 import html
from plotly.subplots import make_subplots


st.set_page_config(layout='wide',page_title="Players Ratings",page_icon="🏀")
st.sidebar.write("If an error message appears, please refresh the page")
def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

download_image('https://raw.githubusercontent.com/sotiristiga/Euroleague_dash/refs/heads/main/eurologo.png','eurologo.png')
st.image(Image.open("eurologo.png"),width=100)
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
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
        return "Second Round"
def fixture_format4(Fixture):
    if Fixture <= 17:
        return "First Round"
    elif Fixture > 17 and Fixture <= 34:
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
        if Fixture <= 17:
            return "First Round"
        elif Fixture > 17 and Fixture <= 34:
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

All_Seasons_results=pd.concat([euroleague_2016_2017_results,euroleague_2017_2018_results,euroleague_2018_2019_results,euroleague_2019_2020_results,euroleague_2020_2021_results,euroleague_2021_2022_results,euroleague_2022_2023_results,euroleague_2023_2024_results,euroleague_2024_2025_results])

st.sidebar.markdown('''
  * ## [Filters](#filters)
  * ## [Teams Ratings](#teams-ratings)
  * ## [Players Ratings](#players-ratings)
  

''', unsafe_allow_html=True)
st.header("Filters")
f1,f2,f3,f4,f5=st.columns(5)
with f1:
    selected_season = st.selectbox("Season:",['2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021','2021-2022', '2022-2023', '2023-2024','2024-2025','2025-2026','All'],index=8)
with f2:
    selected_phase = st.selectbox("Phase:",['Regular Season', 'Play In','Play offs', 'Final Four','All'],index=4)
with f3:
    selected_round = st.selectbox("Round:",['First Round', 'Second Round','PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final', 'All'],index=12)
with f4:
    selected_ha = st.selectbox("Home or Away games:",['A', 'H', 'All'],index=2)
with f5:
    selected_wl = st.selectbox("Result:",['W', 'L','All'],index=2)

def team_rating_stat_higher(dataset,stat):
    dataset1=dataset[["Team",stat]].sort_values(stat,ascending=True).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Team.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating '+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset

def team_rating_stat_lower(dataset,stat):
    dataset1=dataset[["Team",stat]].sort_values(stat,ascending=False).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Team.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating '+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset

def games_format(HA, Fixture, Season, Team, Against):
    if HA == "H":
        return Fixture + " / " + Season + ' / ' + Team + ' - ' + Against
    elif HA == "A":
        return Fixture + " / " + Season + ' / ' + Against + ' - ' + Team


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def period_win_format(S, C):
    if S > C:
        return 1
    else:
        return 0


def result_format(Win):
    if Win == 1:
        return "W"
    elif Win == 0:
        return "L"


def period_win_res_win_format(S, C, result):
    if S > C and result == "W":
        return 1
    else:
        return 0


home_team = (All_Seasons_results[['Fixture', "Phase", "Home", "Away", "Home_Points", "Away_Points",
                                  "Q1H", "Q2H", "Q3H", "Q4H", 'EXH', "Q1A", "Q2A", "Q3A", "Q4A", 'EXA', 'Season',
                                  'Round', 'Home_win', 'idseason']]
             .rename(columns={"Home": 'Team', "Away": 'Against', "Home_Points": 'Scored', "Away_Points": "Conceed",
                              "Q1H": 'Q1S', "Q2H": 'Q2S', "Q3H": 'Q3S', "Q4H": 'Q4S', 'EXH': 'EXS', "Q1A": 'Q1C',
                              "Q2A": 'Q2C', "Q3A": 'Q3C', "Q4A": 'Q4C', 'EXA': 'EXC', 'Home_win': 'Win'}))

home_team['HA'] = "H"
away_team = (All_Seasons_results[['Fixture', "Phase", "Home", "Away", "Home_Points", "Away_Points",
                                  "Q1H", "Q2H", "Q3H", "Q4H", 'EXH', "Q1A", "Q2A", "Q3A", "Q4A", 'EXA', 'Season',
                                  'Round', 'Away_win', 'idseason']]
             .rename(columns={"Home": 'Against', "Away": 'Team', "Home_Points": 'Conceed', "Away_Points": "Scored",
                              "Q1H": 'Q1C', "Q2H": 'Q2C', "Q3H": 'Q3C', "Q4H": 'Q4C', 'EXH': 'EXC', "Q1A": 'Q1S',
                              "Q2A": 'Q2S', "Q3A": 'Q3S', "Q4A": 'Q4S', 'EXA': 'EXS', 'Away_win': 'Win'}))
away_team['HA'] = "A"

period_points = pd.concat([home_team, away_team])

period_points["FHS"] = period_points["Q1S"] + period_points["Q2S"]
period_points["FHC"] = period_points["Q1C"] + period_points["Q2C"]
period_points["SHS"] = period_points["Q3S"] + period_points["Q4S"]
period_points["SHC"] = period_points["Q3C"] + period_points["Q4C"]
period_points["results"] = period_points["Win"].apply(result_format)
period_points['EXS'].replace(0, np.nan, inplace=True)
period_points['EXC'].replace(0, np.nan, inplace=True)





finalstats = All_Seasons.groupby(['idseason', 'Team'])[['PTS', 'F2M',
                                                        'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                        'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                        'PIR', 'Possesions']].sum().reset_index()
finalstats['2P(%)'] = 100 * (finalstats['F2M'] / finalstats['F2A'])
finalstats['3P(%)'] = 100 * (finalstats['F3M'] / finalstats['F3A'])
finalstats['FT(%)'] = 100 * (finalstats['FTM'] / finalstats['FTA'])
finalstats['Offensive Rating'] = 100 * (finalstats['PTS'] / finalstats['Possesions'])
finalstats['EFG(%)'] = 100 * (finalstats['F2M'] + 1.5 * finalstats['F3M']) / (finalstats['F2A'] + finalstats['F3A'])
finalstats['TS(%)'] = 100 * (finalstats['PTS']) / (
            2 * (finalstats['F2A'] + finalstats['F3A'] + 0.44 * finalstats['FTA']))
finalstats['FT Ratio'] = finalstats['FTA'] / (finalstats['F3A'] + finalstats['F2A'])
finalstats['AS-TO Ratio'] = finalstats['AS'] / finalstats['TO']
finalstats['TO Ratio'] = 100 * (finalstats['TO'] / finalstats['Possesions'])
finalstats['AS Ratio'] = 100 * (finalstats['AS'] / finalstats['Possesions'])
finalstats = finalstats[
    ['idseason', 'Team', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR',
     'TR',
     'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
     'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)

finalstats_opp = All_Seasons.groupby(['idseason', 'Against'])[['PTS', 'F2M',
                                                               'F2A', 'F3M', 'F3A', 'FTM', 'FTA', 'OR',
                                                               'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF',
                                                               'RF',
                                                               'PIR', 'Possesions']].sum().reset_index()

finalstats_opp['2P(%)'] = 100 * (finalstats_opp['F2M'] / finalstats_opp['F2A'])
finalstats_opp['3P(%)'] = 100 * (finalstats_opp['F3M'] / finalstats_opp['F3A'])
finalstats_opp['FT(%)'] = 100 * (finalstats_opp['FTM'] / finalstats_opp['FTA'])
finalstats_opp['Offensive Rating'] = 100 * (finalstats_opp['PTS'] / finalstats_opp['Possesions'])
finalstats_opp['EFG(%)'] = 100 * (finalstats_opp['F2M'] + 1.5 * finalstats_opp['F3M']) / (
            finalstats_opp['F2A'] + finalstats_opp['F3A'])
finalstats_opp['TS(%)'] = 100 * (finalstats_opp['PTS']) / (
            2 * (finalstats_opp['F2A'] + finalstats_opp['F3A'] + 0.44 * finalstats_opp['FTA']))
finalstats_opp['FT Ratio'] = finalstats_opp['FTA'] / (finalstats_opp['F3A'] + finalstats_opp['F2A'])
finalstats_opp['AS-TO Ratio'] = finalstats_opp['AS'] / finalstats_opp['TO']
finalstats_opp['TO Ratio'] = 100 * (finalstats_opp['TO'] / finalstats_opp['Possesions'])
finalstats_opp['AS Ratio'] = 100 * (finalstats_opp['AS'] / finalstats_opp['Possesions'])
finalstats_opp = finalstats_opp[
    ['idseason', 'Against', 'PTS', 'F2M', 'F2A', '2P(%)', 'F3M', 'F3A', '3P(%)', 'FTM', 'FTA', 'FT(%)', 'OR', 'DR',
     'TR',
     'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR', 'Possesions', 'Offensive Rating', 'EFG(%)',
     'TS(%)', 'FT Ratio', 'AS-TO Ratio', 'TO Ratio', 'AS Ratio']].round(1)
finalstats_opp = finalstats_opp.add_prefix('opp ').rename(
    columns={'opp Against': 'Team', 'opp idseason': 'idseason'})

gamesstats = pd.merge(finalstats, finalstats_opp)
allstats_in_a_game = pd.merge(period_points, gamesstats, on=['idseason', 'Team'])



if "All" in selected_ha:
    selected_ha = ['A', 'H']
    All_Seasons_filter=All_Seasons.loc[All_Seasons['HA'].isin(selected_ha)]
    allstats_in_a_game1 = allstats_in_a_game.loc[allstats_in_a_game['HA'].isin(selected_ha)]
    select_ha=''
else:
    All_Seasons_filter=All_Seasons.loc[All_Seasons['HA']==selected_ha]
    allstats_in_a_game1 = allstats_in_a_game.loc[allstats_in_a_game['HA'] == selected_ha]
    select_ha = selected_ha

if "All" in selected_season:
    selected_season = ['2016-2017', '2017-2018', '2018-2019', '2019-2020','2020-2021','2021-2022', '2022-2023','2023-2024','2024-2025','2025-2026']
    All_Seasons_filter=All_Seasons_filter.loc[All_Seasons_filter['Season'].isin(selected_season)]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Season'].isin(selected_season)]
    select_season = ''
else:
    All_Seasons_filter=All_Seasons_filter.loc[All_Seasons_filter['Season']==selected_season]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Season'] == selected_season]
    select_season = selected_season

if "All" in selected_wl:
    selected_wl = ['W', 'L']
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['results'].isin(selected_wl)]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['results'].isin(selected_wl)]
    select_wl = ''
else:
    All_Seasons_filter= All_Seasons_filter.loc[All_Seasons_filter['results'] == selected_wl]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['results'] == selected_wl]
    select_wl = selected_wl

if "All" in selected_phase:
    selected_phase = ['Regular Season', 'Play In','Play offs', 'Final Four']
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Phase'].isin(selected_phase)]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Phase'].isin(selected_phase)]
    select_phase = ''
else:
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Phase'] == selected_phase]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Phase'] == selected_phase]
    select_phase = selected_phase

if "All" in selected_round:
    selected_round = ['First Round', 'Second Round', 'PI 1', 'PI 2', 'PO 1', 'PO 2', 'PO 3', 'PO 4','PO 5', 'Semi Final', 'Third Place', 'Final']
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Round'].isin(selected_round)]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Round'].isin(selected_round)]
    select_round = ''
else:
    All_Seasons_filter = All_Seasons_filter.loc[All_Seasons_filter['Round'] == selected_round]
    allstats_in_a_game1 = allstats_in_a_game1.loc[allstats_in_a_game1['Round'] == selected_round]
    select_round = selected_round













def null_replace(x):
    if x==' ':
        return 0
    else:
        return x



st.header("Teams Ratings")

avgteamstats = allstats_in_a_game1.groupby('Team')[['Q1S',
                                                    'Q2S', 'Q1C', 'Q2C', 'FHS', 'FHC', 'Q3S', 'Q4S', 'Q3C', 'Q4C',
                                                    'SHS', 'SHC', 'EXS', 'EXC',
                                                    'PTS', 'opp PTS', 'AS', 'opp AS', 'F2M', 'F2A', 'opp F2M',
                                                    'opp F2A',
                                                    'F3M', 'F3A', 'opp F3M', 'opp F3A', 'FTM', 'FTA', 'opp FTM',
                                                    'opp FTA',
                                                    'OR', 'DR', 'TR', 'opp OR', 'opp DR', 'opp TR', 'ST', 'opp ST',
                                                    'TO', 'opp TO', 'BLK', 'BLKR', 'PF', 'RF',
                                                    'PIR', 'opp PIR', 'Possesions',
                                                    'opp Possesions']].mean().reset_index().round(2)

avgteamstats['2P(%)'] = 100 * (avgteamstats['F2M'] / avgteamstats['F2A'])
avgteamstats['3P(%)'] = 100 * (avgteamstats['F3M'] / avgteamstats['F3A'])
avgteamstats['FT(%)'] = 100 * (avgteamstats['FTM'] / avgteamstats['FTA'])
avgteamstats['opp 2P(%)'] = 100 * (avgteamstats['opp F2M'] / avgteamstats['opp F2A'])
avgteamstats['opp 3P(%)'] = 100 * (avgteamstats['opp F3M'] / avgteamstats['opp F3A'])
avgteamstats['opp FT(%)'] = 100 * (avgteamstats['opp FTM'] / avgteamstats['opp FTA'])
avgteamstats['Offensive Rating'] = 100 * (avgteamstats['PTS'] / avgteamstats['Possesions'])
avgteamstats['EFG(%)'] = 100 * (avgteamstats['F2M'] + 1.5 * avgteamstats['F3M']) / (
            avgteamstats['F2A'] + avgteamstats['F3A'])
avgteamstats['TS(%)'] = 100 * (avgteamstats['PTS']) / (
        2 * (avgteamstats['F2A'] + avgteamstats['F3A'] + 0.44 * avgteamstats['FTA']))
avgteamstats['FT Ratio'] = avgteamstats['FTA'] / (avgteamstats['F3A'] + avgteamstats['F2A'])
avgteamstats['AS-TO Ratio'] = avgteamstats['AS'] / avgteamstats['TO']
avgteamstats['TO Ratio'] = 100 * (avgteamstats['TO'] / avgteamstats['Possesions'])
avgteamstats['AS Ratio'] = 100 * (avgteamstats['AS'] / avgteamstats['Possesions'])
avgteamstats['Defensive Rating'] = 100 * (avgteamstats['opp PTS'] / avgteamstats['opp Possesions'])
avgteamstats['opp EFG(%)'] = 100 * (avgteamstats['opp F2M'] + 1.5 * avgteamstats['opp F3M']) / (
        avgteamstats['opp F2A'] + avgteamstats['opp F3A'])
avgteamstats['opp TS(%)'] = 100 * (avgteamstats['opp PTS']) / (
        2 * (avgteamstats['opp F2A'] + avgteamstats['opp F3A'] + 0.44 * avgteamstats['opp FTA']))
avgteamstats['opp FT Ratio'] = avgteamstats['opp FTA'] / (avgteamstats['opp F3A'] + avgteamstats['opp F2A'])
avgteamstats['opp AS-TO Ratio'] = avgteamstats['opp AS'] / avgteamstats['opp TO']
avgteamstats['opp TO Ratio'] = 100 * (avgteamstats['opp TO'] / avgteamstats['opp Possesions'])
avgteamstats['opp AS Ratio'] = 100 * (avgteamstats['opp AS'] / avgteamstats['opp Possesions'])
colsplus = ['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
            'FTA', 'OR', 'DR', 'TR', 'BLK', 'RF', 'ST', '2P(%)', '3P(%)', 'FT(%)', 'EFG(%)', 'TS(%)', 'FT Ratio',
            'AS-TO Ratio',
            'AS Ratio', 'opp TO Ratio', 'Offensive Rating']

colsminus = ['BLKR', 'PF', 'opp PTS', 'opp AS', 'opp F2M', 'opp F2A', 'opp 2P(%)', 'opp F3M', 'opp F3A',
             'opp 3P(%)',
             'opp FTM', 'opp FTA', 'opp FT(%)', 'opp OR', 'opp DR', 'opp TR', 'opp ST', 'Defensive Rating',
             'opp EFG(%)', 'opp TS(%)',
             'opp FT Ratio', 'opp AS-TO Ratio', 'opp AS Ratio', 'TO Ratio']

teams_ratings1 = team_rating_stat_higher(avgteamstats, "PTS")
for i in colsplus:
    df2 = team_rating_stat_higher(avgteamstats, i)
    teams_ratings1 = pd.merge(teams_ratings1, df2)

teams_ratings2 = team_rating_stat_lower(avgteamstats, "TO")
for i in colsminus:
    df3 = team_rating_stat_lower(avgteamstats, i)
    teams_ratings2 = pd.merge(teams_ratings2, df3)
teams_ratings = pd.merge(teams_ratings1, teams_ratings2)

offense_rating_data = teams_ratings[
    ['Team', 'Rating PTS', 'Rating AS', 'Rating TO', 'Rating OR', 'Rating BLKR', 'Rating RF', 'Rating F2M',
     'Rating F2A',
     'Rating 2P(%)', 'Rating F3M', 'Rating F3A', 'Rating 3P(%)', 'Rating FTM', 'Rating FTA', 'Rating FT(%)',
     'Rating FT Ratio',
     'Rating EFG(%)', 'Rating TS(%)', "Rating Offensive Rating", 'Rating AS-TO Ratio', "Rating AS Ratio",
     'Rating opp DR', 'Rating opp ST',
     'Rating TO Ratio', 'Rating opp TO Ratio']].melt(id_vars='Team').groupby('Team')[
    'value'].mean().reset_index().rename(columns={"value": "Offense"})

defense_ratings_data = teams_ratings[
    ['Team', 'Rating ST', 'Rating DR', 'Rating PF', 'Rating BLK', 'Rating opp PTS', 'Rating opp AS',
     'Rating opp F2M', 'Rating opp F2A', 'Rating opp 2P(%)', 'Rating opp F3M', 'Rating opp F3A', 'Rating opp 3P(%)',
     'Rating opp FTM', 'Rating opp FTA', 'Rating opp FT(%)', 'Rating opp OR', 'Rating Defensive Rating',
     'Rating opp EFG(%)', 'Rating opp TS(%)',
     'Rating opp FT Ratio', 'Rating opp AS-TO Ratio', 'Rating opp AS Ratio']].melt(id_vars='Team').groupby('Team')[
    'value'].mean().reset_index().rename(columns={"value": "Defense"})

total_ratings_data = teams_ratings.melt(id_vars='Team').groupby('Team')['value'].mean().reset_index().rename(
    columns={"value": "Overall"})

ratings_team = pd.merge(pd.merge(offense_rating_data, defense_ratings_data), total_ratings_data)

interactive_table(ratings_team.round(0).set_index('Team').sort_values('Overall',ascending=False),
                  paging=False, height=900, width=4000, showIndex=True,
                  classes="display order-column nowrap table_with_monospace_font", searching=True,
                  fixedColumns=True, select=True, info=False, scrollCollapse=True,
                  scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                  columnDefs=[{"className": "dt-center", "targets": "_all"}])

st.header("Players Ratings")
computestats=All_Seasons_filter.groupby('Player')[['PTS','MIN','F2M', 'F2A','F3M', 'F3A','FTM', 'FTA','OR', 'DR', 'TR', 'AS', 'ST', 'TO', 'BLK', 'BLKR', 'PF', 'RF', 'PIR','Team_PTS','Team_F2M', 'Team_F2A','Team_F3M', 'Team_F3A','Team_FTM', 'Team_FTA','Team_OR', 'Team_DR', 'Team_TR', 'Team_AS', 'Team_ST', 'Team_TO', 'Team_BLK', 'Team_PF','Team_opp_PTS','Team_opp_F2M', 'Team_opp_F2A','Team_opp_F3M', 'Team_opp_F3A','Team_opp_FTM', 'Team_opp_FTA','Team_opp_OR', 'Team_opp_DR', 'Team_opp_TR', 'Team_opp_AS', 'Team_opp_ST', 'Team_opp_TO', 'Team_opp_BLK', 'Team_opp_PF']].mean().round(1).reset_index()


computestats['P2']=100*(computestats['F2M']/computestats['F2A'])
computestats['P2']=computestats['P2'].fillna(0)
computestats['P3']=100*(computestats['F3M']/computestats['F3A'])
computestats['P3']=computestats['P3'].fillna(0)
computestats['PFT']=100*(computestats['FTM']/computestats['FTA'])
computestats['PFT']=computestats['PFT'].fillna(0)
computestats['POS']=0.96*(computestats['F2A']+computestats['F3A']-computestats['OR']+computestats['TO']+0.44*computestats['FTA'])
computestats['ORA']=100*(computestats['PTS']/computestats['POS'])
computestats['ORA']=computestats['ORA'].fillna(0)
computestats['EFG']=100*(computestats['F2M']+1.5*computestats['F3M'])/(computestats['F2A']+computestats['F3A'])
computestats['EFG']=computestats['EFG'].fillna(0)
computestats['TS']=100*(computestats['PTS'])/(2*(computestats['F2A']+computestats['F3A']+0.44*computestats['FTA']))
computestats['TS']=computestats['TS'].fillna(0)
computestats['FTR']=computestats['FTA']/(computestats['F3A']+computestats['F2A'])
computestats['FTR']=computestats['FTR'].fillna(0)
computestats['ASTOR']=computestats['AS']/computestats['TO']
computestats['ASTOR']=computestats['ASTOR'].fillna(0)
computestats['TOR']=100*(computestats['TO']/computestats['POS'])
computestats['TOR']=computestats['TOR'].fillna(0)
computestats['ASR']=100*(computestats['AS']/computestats['POS'])
computestats['ASR']=computestats['ASR'].fillna(0)
computestats['USG'] = 100 * (((computestats['F3A'] + computestats['F2A']) + 0.44 * computestats['FTA'] + computestats['TO']) * (40)) / (computestats['MIN'] * (computestats['Team_F2A'] +computestats['Team_F3A'] + 0.44 * computestats['Team_FTA'] + computestats['Team_TO']))
computestats['USG']=computestats['USG'].fillna(0)
computestats['ORP'] = (100 * computestats['OR']) / (computestats['Team_OR'] + computestats['Team_opp_OR'])
def player_rating_stat_higher(dataset,stat):
    dataset1=dataset[["Player",stat]].sort_values(stat,ascending=True).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Player.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating '+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset

def player_rating_stat_lower(dataset,stat):
    dataset1=dataset[["Player",stat]].sort_values(stat,ascending=False).reset_index()
    dataset1.drop("index",axis=1,inplace=True)
    final_dataset=dataset1.reset_index() >> mutate(Rating=(100*(X.index+1)/X.Player.nunique()),Rating1=(100-(100-X.Rating.round(0))*0.5).round(0))
    final_dataset.rename(columns={'Rating1':'Rating '+ stat},inplace=True)
    final_dataset.drop(["index","Rating",stat],axis=1,inplace=True)
    return final_dataset


player_rating_stat_higher(computestats,'PTS')

colsplus=['AS', 'F2M', 'F2A', 'F3M', 'F3A', 'FTM',
       'FTA', 'OR', 'DR', 'TR',  'BLK',  'RF', 'ST', 'P2', 'P3', 'PFT','ORA','EFG','TS','FTR','ASTOR','ASR','USG','ORP']


colsminus=[ 'BLKR',
       'PF','TOR' ]

players_ratings1=player_rating_stat_higher(computestats,"PTS")
for i in colsplus:
    df2=player_rating_stat_higher(computestats,i)
    players_ratings1=pd.merge(players_ratings1,df2)

players_ratings2=player_rating_stat_lower(computestats,"TO")
for i in colsminus:
    df3=player_rating_stat_lower(computestats,i)
    players_ratings2=pd.merge(players_ratings2,df3)


players_ratings=pd.merge(players_ratings1,players_ratings2)




offense_rating_data=players_ratings[['Player','Rating PTS', 'Rating AS', 'Rating TO', 'Rating OR', 'Rating BLKR', 'Rating RF', 'Rating F2M', 'Rating F2A',
     'Rating P2', 'Rating F3M', 'Rating F3A', 'Rating P3','Rating FTM', 'Rating FTA', 'Rating PFT', 'Rating FTR',
     'Rating EFG', 'Rating TS', "Rating ORA",'Rating ASTOR','Rating TOR', "Rating ASR", 'Rating ORP']].melt(id_vars='Player').groupby('Player')['value'].mean().reset_index().rename(columns={"value":"Offense"})


defense_ratings_data = players_ratings[
    ['Player','Rating ST', 'Rating DR', 'Rating PF', 'Rating BLK']].melt(id_vars='Player').groupby('Player')['value'].mean().reset_index().rename(columns={"value":"Defense"})


total_ratings_data = players_ratings.melt(id_vars='Player').groupby('Player')['value'].mean().reset_index().rename(columns={"value":"Overall"})

ratings=pd.merge(pd.merge(offense_rating_data,defense_ratings_data),total_ratings_data)

interactive_table(ratings.round(0).set_index('Player').sort_values('Overall',ascending=False),
                      paging=False, height=900, width=4000, showIndex=True,
                      classes="display order-column nowrap table_with_monospace_font", searching=True,
                      fixedColumns=True, select=True, info=False, scrollCollapse=True,
                      scrollX=True, scrollY=1000, fixedHeader=True, scroller=True, filter='bottom',
                      columnDefs=[{"className": "dt-center", "targets": "_all"}])
